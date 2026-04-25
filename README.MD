# elochess

[![CI](https://github.com/Moritz72/elochess/actions/workflows/ci.yml/badge.svg)](https://github.com/Moritz72/elochess/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/Moritz72/elochess/branch/main/graph/badge.svg)](https://codecov.io/gh/Moritz72/elochess)
[![Python 3.11](https://img.shields.io/badge/python-3.11+-blue)](https://img.shields.io/badge/python-3.11+-blue)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue)](https://github.com/astral-sh/ruff)
[![mypy](https://img.shields.io/badge/types-mypy-blue)](https://github.com/python/mypy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

`elochess` is a simple python package for calculating chess ratings.

## Rating Systems

- [FIDE Elo](https://en.wikipedia.org/wiki/Elo_rating_system)
used by the [FIDE](https://en.wikipedia.org/wiki/FIDE)

- [Deutsche Wertungszahl](https://de.wikipedia.org/wiki/Deutsche_Wertungszahl)
used by the [German Chess Federation](https://www.schachbund.de)

## Usage

```python
from elochess.elo import EloCalculator

current_rating = 1500
opponent_ratings = [1642, 1425, 1432]
score = 2.5

new_rating = EloCalculator.get_rating(
    current_rating,
    opponent_ratings,
    score
)
```
