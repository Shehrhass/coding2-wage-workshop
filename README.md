# Coding 2 Wage Workshop

1. How do expected weekly wages differ across education groups?
2. Do those wage gaps vary with age?

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

Open [code/workshop.ipynb](code/workshop.ipynb) in VS Code and select the
workshop’s `.venv` kernel. For JupyterLab, run `uv run jupyter lab` from the
repository root.

## Checkpoints

Checkpoint CSVs announced in class appear under `data/`. From the
workshop folder, `git pull --ff-only` retrieves released files.

## AI Attribution

The workshop materials were prepared with assistance from OpenAI language models.
