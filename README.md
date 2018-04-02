# Pylint Pytest

Additional string checkers for [Pylint](https://pylint.org).

## Install

```
git clone https://github.com/jgissend10/pylint-pytest.git
cd pylint-pytest
pip install .
```

## Usage

To use the pytest-fixture includes, run Pylint as follows:

```
pylint --load-plugins pylint-pytest foo.py
```