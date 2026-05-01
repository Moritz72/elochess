# ♟️ elochess

[![CI](https://github.com/Moritz72/elochess/actions/workflows/ci.yml/badge.svg)](https://github.com/Moritz72/elochess/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/Moritz72/elochess/branch/main/graph/badge.svg)](https://codecov.io/gh/Moritz72/elochess)
[![Python 3.11](https://img.shields.io/badge/python-3.11+-blue)](https://img.shields.io/badge/python-3.11+-blue)
[![uv](https://img.shields.io/badge/dependency%20manager-uv-blue)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/badge/linting-ruff-blue)](https://github.com/astral-sh/ruff)
[![mypy](https://img.shields.io/badge/types-mypy-blue)](https://github.com/python/mypy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

`elochess` is a simple python package for calculating chess ratings.

## ✨ Rating Systems

* [FIDE Elo](https://en.wikipedia.org/wiki/Elo_rating_system) used by the [FIDE](https://en.wikipedia.org/wiki/FIDE)
* [Deutsche Wertungszahl](https://de.wikipedia.org/wiki/Deutsche_Wertungszahl) used by the [German Chess Federation](https://www.schachbund.de)
* [USCF Rating](https://www.uscfsales.com/blogs/chess-matches/understanding-the-uscf-chess-rating-system?srsltid=AfmBOoqF_EKwyGsBCQFddl7XJ9mgGjqz-lktlDT3AOnOnnXpmjNh0ses) used by the [US Chess Federation](https://new.uschess.org)

## 🎯 Accuracy

This project aims to replicate the exact official rating calulations.

For FIDE Elo and DWZ, the calculated ratings have been confirmed
to be accurate in a large number of real scenarios.

For USCF rating, the calculated ratings are an estimate
based on the "official" [Rating Estimator](https://www.uschess.org/index.php/Players-Ratings/Rating-Estimator-February-2023.html).
Here as well, it has been confirmed
to be accurate in a large number of real scenarios.
But keep in mind that this is a mere estimate of the real calculation
which can only be performed by knowing all results of all players.

## 📦 Installation

```bash
pip install elochess
```

For CLI support:

```bash
pip install elochess[cli]
```

For API support:

```bash
pip install elochess[api]
```

## 🚀 Usage

### 🐍 Python

```python
from elochess.elo import EloCalculator

current_rating = 1500
opponent_ratings = [1642, 1425, 1432]
score = 2.5

new_rating = EloCalculator.update_rating(
    current_rating,
    opponent_ratings,
    score
)
```

### 💻 CLI

```bash
elochess-cli update elo \
  --current 1500 \
  --opponent 1642 \
  --opponent 1425 \
  --opponent 1432 \
  --score 2.5
```

### 🌐 API

```bash
elochess-api
```

Then, check out the [OpenAPI Spec](https://swagger.io/specification/)
at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Furthermore, an instance of the API is deployed
in the [FastAPI cloud](https://fastapicloud.com)
at [elochess.fastapicloud.dev](https://elochess.fastapicloud.dev).

## 📄 License

This project is licensed under the [MIT License](LICENSE).
