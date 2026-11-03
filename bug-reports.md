# Bug Reports – SauceDemo (`problem_user`)

Found through **exploratory testing** with the demo account `problem_user` (password `secret_sauce`).
Environment for all bugs: www.saucedemo.com · Microsoft Edge · Windows 11.

| ID | Title | Severity | Status |
|---|---|---|---|
| BUG-01 | Some products cannot be added to the cart | High | Open |
| BUG-02 | Product images are wrong on the product list | Medium | Open |
| BUG-03 | Some products cannot be removed from the cart | Medium | Open |
| BUG-04 | Checkout cannot be completed – Last Name field does not work | Critical | Open |

---

## BUG-01: Some products cannot be added to the cart

**Severity:** High – the customer cannot buy these products.

**Steps to reproduce**
1. Log in as `problem_user`.
2. On the product list, click **Add to cart** on every product, one by one.

**Expected result**
Every click adds the product. The button changes to **Remove** and the cart badge goes up by 1.

**Actual result**
For some products nothing happens: the button does not change and the cart badge does not go up.
Affected products: *Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket, Test.allTheThings() T-Shirt (Red)*.

**Works with `standard_user`?** Yes.

---

## BUG-02: Product images are wrong on the product list

**Severity:** Medium – the customer cannot see what they are buying.

**Steps to reproduce**
1. Log in as `problem_user`.
2. Look at the product images on the product list.
3. Click on a product to open its detail page.

**Expected result**
Each product shows its own image, and the image on the list is the same as on the detail page.

**Actual result**
All products on the list show the same image (a dog). The image on the detail page is not the same as on the list.

**Works with `standard_user`?** Yes.

---

## BUG-03: Some products cannot be removed from the cart

**Severity:** Medium – the customer cannot change their order.

**Steps to reproduce**
1. Log in as `problem_user`.
2. Add *Sauce Labs Backpack* to the cart.
3. On the product list, click **Remove** on the same product.

**Expected result**
The product is removed, the button changes back to **Add to cart** and the cart badge goes down by 1.

**Actual result**
Nothing happens. The product stays in the cart.

**Works with `standard_user`?** Yes.

---

## BUG-04: Checkout cannot be completed – Last Name field does not work

**Severity:** Critical – no customer can finish a purchase. This blocks the main flow of the shop.

**Steps to reproduce**
1. Log in as `problem_user`.
2. Add *Sauce Labs Backpack* to the cart and open the cart.
3. Click **Checkout**.
4. Type `Anna` in **First Name**, `Svensson` in **Last Name** and `12345` in **Zip/Postal Code**.
5. Click **Continue**.

**Expected result**
The user comes to the overview page (*Checkout: Overview*) and can finish the order.

**Actual result**
When typing in **Last Name**, the text goes into the **First Name** field instead. Last Name stays empty.
After **Continue** the error *"Error: Last Name is required"* is shown, and the purchase cannot be completed.

**Works with `standard_user`?** Yes.
