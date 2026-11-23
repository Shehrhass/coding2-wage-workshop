"""Download the March 2005 CPS public-use archive and build the workshop CSV."""

from __future__ import annotations

import hashlib
from pathlib import Path
from urllib.request import Request, urlopen
from zipfile import ZipFile

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
ARCHIVE = RAW / "source" / "asec2005_pubuse.zip"
SOURCE_URL = "https://www2.census.gov/programs-surveys/cps/datasets/2005/march/asec2005_pubuse.zip"
SOURCE_SHA256 = "a11dc20c6bf9304c8a29aaff38387c9fec0165e04bb8f09f9cbd87b9ed5312e9"


def fetch_archive() -> Path:
    if ARCHIVE.is_file() and hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() == SOURCE_SHA256:
        return ARCHIVE

    request = Request(SOURCE_URL, headers={"User-Agent": "Coding-2-CEU (wage workshop)"})
    with urlopen(request, timeout=120) as response:
        data = response.read()
    if hashlib.sha256(data).hexdigest() != SOURCE_SHA256:
        raise RuntimeError("The Census archive did not match its expected checksum.")

    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    ARCHIVE.write_bytes(data)
    return ARCHIVE


def read_cps_asec_people(path: Path) -> pd.DataFrame:
    """Read the fixed-width person fields used for the workshop."""
    # Census 2005 ASEC person record layout: (1-based start, field width).
    fields = {
        "PH-SEQ": (2, 5),
        "PPPOS": (7, 2),
        "A-AGE": (15, 2),
        "A-SEX": (20, 1),
        "A-HGA": (22, 2),
        "P-STAT": (26, 1),
        "WKSWORK": (171, 2),
        "HRSWK": (181, 2),
        "WSAL-VAL": (243, 6),
    }
    positions = [slice(start - 1, start - 1 + width) for start, width in fields.values()]
    with ZipFile(path) as archive, archive.open("asec2005_pubuse.pub") as records:
        rows = [
            [int(line[position]) for position in positions]
            for line in records
            if line.startswith(b"3")  # Person record; other lines are households or families.
        ]
    return pd.DataFrame(rows, columns=list(fields))


def prepare_wage_workshop(path: Path) -> pd.DataFrame:
    people = read_cps_asec_people(path)
    # CPS codes 40–42 (some college or associate) are outside the chosen groups.
    education_codes = {
        **dict.fromkeys(range(31, 40), 1),
        43: 2,
        44: 3,
        45: 3,
        46: 3,
    }
    education = people["A-HGA"].map(education_codes)
    sex = people["A-SEX"].map({1: "Male", 2: "Female"})
    keep = (
        people["P-STAT"].eq(1)
        & people["A-AGE"].between(25, 64)
        & education.notna()
        & sex.notna()
    )
    sample = people.loc[keep]
    # The survey uses 0 for weeks or hours when the work question does not apply.
    weeks_worked = sample["WKSWORK"].replace(0, np.nan)
    return pd.DataFrame({
        "record_id": sample["PH-SEQ"].astype(str) + "-" + sample["PPPOS"].astype(str),
        "age": sample["A-AGE"],
        "sex": sex.loc[keep],
        "education_code": education.loc[keep].astype(int),
        "weekly_hours": sample["HRSWK"].replace(0, np.nan),
        # Keep reported work with no wage and salary income as zero weekly pay.
        "weekly_wage": sample["WSAL-VAL"] / weeks_worked,
    })


def main() -> None:
    frame = prepare_wage_workshop(fetch_archive())
    output = RAW / "cps_asec_2005_workshop.csv"
    frame.to_csv(output, index=False)
    print(f"wrote {output.relative_to(ROOT)} ({len(frame):,} rows, {len(frame.columns)} columns)")


if __name__ == "__main__":
    main()
