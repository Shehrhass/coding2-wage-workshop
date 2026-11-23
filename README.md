# Coding 2 Wage Workshop

1. How do hourly wages differ across education groups in this sample?
2. Do these wage gaps vary with age?

## Data

The workshop uses an extract from the Annual Social and Economic Supplement to
the U.S. Current Population Survey (CPS).

- [Data dictionary](data/README.md)
- [Official survey release and documentation](https://www.census.gov/data/datasets/2005/demo/cps/cps-asec-2005.html)

## Setup

```bash
git clone https://github.com/ulrichwohak/coding2-wage-workshop.git
cd coding2-wage-workshop
uv sync --locked
```

The [starting CSV](data/raw/cps_asec_2005_workshop.csv) comes with the clone.

Open [workshop.ipynb](workshop.ipynb) in VS Code and select the
workshop’s `.venv` kernel, or launch JupyterLab with `uv run jupyter lab`.
Open the notebook at the repository root so the relative data path works.

## Checkpoints

Checkpoint CSVs announced in class appear under `checkpoints/`. From the
workshop folder, `git pull --ff-only` retrieves released files.

## AI Attribution

The workshop materials were prepared with assistance from OpenAI language models.
