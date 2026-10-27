# lab3_shopping_cart.py
# Practice: lists of dictionaries, *args, default args, lambda, sorted, map, filter

cart = [
    {"item": "Notebook", "price": 250, "qty": 4},
    {"item": "Pen", "price": 40, "qty": 10},
    {"item": "Bag", "price": 2200, "qty": 1},
    {"item": "Calculator", "price": 1500, "qty": 1},
]

def line_total(product):
    return product["price"] * product["qty"]

def bill_total(items, tax_percent=16, discount=0):
    """Total of all items, minus discount, plus tax."""
    subtotal = sum(line_total(p) for p in items)
    after_discount = subtotal - discount
    return after_discount + after_discount * tax_percent / 100

def count_items(*names):
    return len(names)

# Sort the cart by line total (largest first) with a lambda
for p in sorted(cart, key=lambda p: line_total(p), reverse=True):
    print(f"{p['item']:<11} {p['qty']:>3} x {p['price']:>5} = {line_total(p):>6}")

# map: list of item names in capitals
print("Items:", list(map(lambda p: p["item"].upper(), cart)))

# filter: only items costing 1000 or more each
expensive = list(filter(lambda p: p["price"] >= 1000, cart))
print("Expensive:", [p["item"] for p in expensive])

print("Bill with tax:", bill_total(cart))
print("Bill with Rs.500 discount:", bill_total(cart, discount=500))
print("Counted:", count_items("Pen", "Bag", "Eraser"))
