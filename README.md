# SauceDemo QA: Manual and Automated Testing

![Tests](https://github.com/SuyogSubedi21/sauce_demo/actions/workflows/tests.yml/badge.svg)
End to end QA of [saucedemo.com](https://www.saucedemo.com), a demo e-commerce site, covering manual test design, bug reporting and automated regression testing.

## What this project covers

• **Manual testing:** 14 test cases across login, products, sorting, cart and checkout, run against every built in user type
• **Bug reporting:** 8 documented bugs (b1 to b8) with steps to reproduce, expected vs actual results, severity and priority
• **Automation:** Playwright with pytest, organised by feature
• **CI:** GitHub Actions runs the full suite on every push and pull request

## Tech stack

Python, Playwright, pytest, uv, GitHub Actions

## Project structure

    docs/
      test_cases.xlsx       manual test cases and bug reports
    tests/
      conftest.py           shared login fixture
      test_login.py
      test_products.py
      test_cart.py
      test_checkout.py
    .github/workflows/
      tests.yml             CI pipeline

## Test strategy

• **Smoke tests** (`@pytest.mark.smoke`): the critical happy path for standard_user (login, add to cart, checkout)
• **Regression:** the full suite
• **Known bugs** are marked `xfail` with their bug ID, so the pipeline stays green and any new failure stands out

## Results

16 automated tests: 6 passed, 10 expected failures, all linked to known bugs.

| Bug | User | Issue | Severity |
|---|---|---|---|
| b1 | problem_user | Every product image is the same | Medium |
| b2 | performance_glitch_user | Login takes over 5 seconds | Medium |
| b3 | error_user | Sorting is broken | Medium |
| b4 | error_user | Only 3 of 6 products add to cart | High |
| b5 | error_user | Remove does nothing on products page | Medium |
| b6 | visual_user | Backpack shows the wrong image | Low |
| b7 | visual_user | Cart button is misaligned | Low |
| b8 | error_user | Finish at checkout does nothing | Critical |

## How to run

    uv sync
    uv run playwright install --with-deps chromium
    uv run pytest                          # full regression
    uv run pytest -m smoke                 # smoke tests only
    uv run pytest --headed --slowmo 500    # watch it in the browser

## Author

Suyog Subedi · [GitHub](https://github.com/SuyogSubedi21)