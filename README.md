# Coding 2 Wage Workshop

1. How do hourly wages differ across education groups in this sample?
2. Do these wage gaps vary with age?

Build the analysis in stages during class. Use the [short data dictionary](data/README.md)
to interpret the education codes, weekly wages and hours. We’ll discuss which
records can support an hourly wage comparison before fitting any models.

## Set up the workshop

Clone the workshop as a separate repository. Run the following in a terminal:

```bash
git clone https://github.com/ulrichwohak/coding2-wage-workshop.git
cd coding2-wage-workshop
uv sync --locked
uv run python scripts/fetch_data.py
```

The fetch command downloads the public Census archive (about 30 MB) and
creates `data/raw/cps_asec_2005_workshop.csv`. Run it from the workshop folder.
It checks and reuses a valid copy of the archive on subsequent runs.

Open [workshop.ipynb](workshop.ipynb) in VS Code and select the
workshop’s `.venv` kernel, or launch JupyterLab with `uv run jupyter lab`.
Open the notebook at the repository root so the relative data path works.

## Continue from a checkpoint

When a checkpoint is announced in class, run `git pull --ff-only` from the
workshop folder. Under `checkpoints/`, open the README for the announced
stage and add its loading cell to your notebook. Checkpoints are optional.

## AI Attribution

The workshop materials were prepared with assistance from OpenAI language models.
In class, build and explain your own analysis. Verify any code or interpretation
an AI tool suggests.
