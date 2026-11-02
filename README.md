# QA Portfolio – Automated UI tests for SauceDemo

![UI tests](https://github.com/Ayyhaam/qa-portfolio-saucedemo/actions/workflows/tests.yml/badge.svg)

Automated end-to-end tests for the demo web shop [SauceDemo](https://www.saucedemo.com), written in **Python** with **Playwright** and **pytest**.
I made this project during my education as an IT test specialist (Frans Schartau, Stockholm) to practise test automation.

## What is tested
- **Login** – valid user, wrong password, locked user, empty username
- **Shopping cart** – add, add several, remove, sort by price
- **Checkout** – complete purchase, missing first name

10 test cases in total → see [docs/test-cases.md](docs/test-cases.md). The approach is described in the [test plan](docs/test-plan.md).

## Tools
| Tool | Purpose |
|---|---|
| Python 3 + pytest | Test framework |
| Playwright | Browser automation |
| Page Object Model | Locators and actions per page in `pages/`, tests in `tests/` |
| GitHub Actions | Runs all tests automatically on every push |

## Project structure
```
pages/          Page objects (login, products, checkout)
tests/          Test files + shared fixtures (conftest.py)
docs/           Test plan and test cases
.github/        CI workflow
```

## Run the tests yourself
```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest -v                 # all tests
pytest -v -m smoke        # only the most critical tests
pytest --headed           # watch the browser while the tests run
```

## Author
Ayham Jamali – IT test specialist student, looking for an internship (LIA) in testing / QA.
