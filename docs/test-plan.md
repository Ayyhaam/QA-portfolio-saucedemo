# Test Plan – SauceDemo web shop

## 1. Purpose
Verify that the most important user flows in the SauceDemo web shop work: login, shopping cart and checkout. The tests are automated so they can be run again after every change (regression testing).

## 2. System under test
- **Application:** [SauceDemo](https://www.saucedemo.com) – a public demo web shop made for test practice
- **Browser:** Chromium (via Playwright)

## 3. Scope
| In scope | Out of scope |
|---|---|
| Login (valid and invalid) | Performance and load testing |
| Add / remove products in the cart | Security testing |
| Sorting of products | Other browsers than Chromium |
| Checkout flow | Mobile layout |

## 4. Test levels and types
- **Test level:** System testing (end-to-end through the user interface)
- **Test types:** Functional testing, positive and negative tests, regression testing
- **Test techniques:** Equivalence partitioning (valid / invalid / locked user), error guessing (empty fields)

## 5. Test data
Public demo accounts from the SauceDemo start page: `standard_user`, `locked_out_user`. No real personal data is used.

## 6. Tools
| Tool | Used for |
|---|---|
| Python + pytest | Writing and running the tests |
| Playwright | Controlling the browser |
| GitHub Actions | Running all tests automatically on every push (CI) |
| GitHub Issues | Bug reports |

## 7. Risks
| Risk | Impact | Mitigation |
|---|---|---|
| The demo site changes its HTML | Tests fail even though there is no bug | Locators are kept in page objects, so they are fixed in one place |
| The demo site is down | Tests cannot run | Re-run later; check the site manually |

## 8. Entry and exit criteria
- **Start:** The site is reachable and the test environment is installed.
- **Done:** All test cases are run. All smoke tests pass. Failed tests are analysed and reported as bugs if they are real defects.
