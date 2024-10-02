# Problem

Ofen the dependency installation is the longest running part of automated testing despite making no changes to dependencies.

# Solution

Cache the Python virtual environment, so you only re-install dependencies if the requirements change.

See below.

```yaml
# For code quality like unit and integration testing
# This workflow will install Python dependencies and run tests with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Software testing

on: ["push"]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
        with:
          ref: ${{ github.event.pull_request.head.sha || github.sha }}

      - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"

      # Separate restore and save steps for the virtualenv cache
      # See: https://adamj.eu/tech/2023/11/02/github-actions-faster-python-virtual-environments/
      - name: Restore cached virtualenv
        uses: actions/cache/restore@v4
        with:
          key: venv-${{ runner.os }}-${{ steps.setup_python.outputs.python-version }}-${{ hashFiles('requirements.txt') }}
          path: .venv

      - name: Install dependencies
        run: |
          python -m venv .venv
          source .venv/bin/activate
          python -m pip install -r requirements.txt
          echo "$VIRTUAL_ENV/bin" >> $GITHUB_PATH
          echo "VIRTUAL_ENV=$VIRTUAL_ENV" >> $GITHUB_ENV

      - name: Saved cached virtualenv
        uses: actions/cache/save@v4
        with:
          key: venv-${{ runner.os }}-${{ steps.setup_python.outputs.python-version }}-${{ hashFiles('requirements.txt') }}
          path: .venv

      - name: Test with pytest
        run: |
          PYTHONPATH=./scripts pytest -vv
```

Credits: Adam Johson via [GitHub Actions: Faster Python runs with cached virtual environments](https://adamj.eu/tech/2023/11/02/github-actions-faster-python-virtual-environments/)