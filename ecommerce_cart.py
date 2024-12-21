def calculate_total(cart_items):
    if not cart_items:
        return "The cart is empty."
    total_price = sum(cart_items.values())
    if len(cart_items) > 5:
        discount = total_price * 0.10
        total_price -= discount
        return f"Total price after 10% discount: {total_price:.2f}"

    return f"Total price: {total_price:.2f}"
cart_items = {'Laptop': 50000,'Headphones': 2000,'Mouse': 500,'Keyboard': 1500}
print(calculate_total(cart_items))
