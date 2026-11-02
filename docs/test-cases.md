# Test Cases

| ID | Area | Test case | Steps | Expected result | Automated |
|---|---|---|---|---|---|
| TC-01 | Login | Login with valid user | Enter `standard_user` + correct password, click Login | Product page "Products" is shown | `test_login.py` |
| TC-02 | Login | Login with wrong password | Enter `standard_user` + wrong password | Error: username and password do not match | `test_login.py` |
| TC-03 | Login | Locked user cannot log in | Enter `locked_out_user` + correct password | Error: user has been locked out | `test_login.py` |
| TC-04 | Login | Login with empty username | Leave username empty, enter password | Error: Username is required | `test_login.py` |
| TC-05 | Cart | Add one product | Log in, add Backpack | Cart badge shows 1 | `test_cart.py` |
| TC-06 | Cart | Add two products | Add Backpack and Bike Light | Cart badge shows 2 | `test_cart.py` |
| TC-07 | Cart | Remove product | Add Backpack, then remove it | Cart badge disappears | `test_cart.py` |
| TC-08 | Products | Sort by price low to high | Choose "Price (low to high)" | Prices are in rising order | `test_cart.py` |
| TC-09 | Checkout | Complete a purchase | Add product, checkout, fill in info, finish | "Thank you for your order!" | `test_checkout.py` |
| TC-10 | Checkout | Checkout without first name | Leave first name empty, click Continue | Error: First Name is required | `test_checkout.py` |

Smoke tests (most critical): TC-01, TC-05, TC-09.
