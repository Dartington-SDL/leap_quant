# leap_quant
Analysis of the LEAP service impact measures for domains 2 and 3

## Getting started
To run this project, you will need Poetry installed 
To install Poetry: 

```zsh
# You need pipx to ensure that your poetry install is clean
brew install pipx
```

```zsh
pipx install poetry
```

```zsh
# `poetry install` creates a venv for this project
# Ensure that you are in this project's directory in your terminal before running this
poetry install
```

```zsh
# Run the run_file with the created Venv
poetry run python run_file.py
```

## Running the Tests

```zsh
# This runs Pytest in watch mode
poetry run ptw
```
