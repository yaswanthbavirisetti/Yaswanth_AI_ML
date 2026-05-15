def add_item_buggy(item, cart=[]):
    cart.append(item)
    return cart

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})

def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"TypeError caught: {e}")

def calculate_total(cart):
    total = sum(item["price"] * item["qty"] for item in cart["items"])
    return total * (1 - cart["discount"] / 100)

def main():
    print(add_item_buggy("apple"))
    print(add_item_buggy("banana"))
    print(add_item_buggy("milk", cart=["bread"]))
    print(add_item_buggy("eggs"))

    cart1 = create_cart("Alice", 10)
    cart2 = create_cart("Bob", 0)

    add_to_cart(cart1, "Laptop", 1000, 1)
    add_to_cart(cart1, "Mouse", 50, 2)

    add_to_cart(cart2, "Phone", 800, 1)

    print(cart1)
    print(f"Alice Total: {calculate_total(cart1)}")
    
    print(cart2)
    print(f"Bob Total: {calculate_total(cart2)}")

    update_price((100, 200), 150)

if __name__ == "__main__":
    main()
