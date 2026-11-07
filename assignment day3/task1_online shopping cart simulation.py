
# Assignment 3: Online Shopping Cart Simulation

# Shopping cart: List of dictionaries
shopping_cart = [
    {"name": "Laptop", "price": 60000, "category": "Electronics", "quantity": 1},
    {"name": "Watch", "price": 2000, "category": "Accessories", "quantity": 1},
    {"name": "Headphones", "price": 800, "category": "Electronics", "quantity": 4},
    {"name": "Mouse", "price": 400, "category": "Accessories", "quantity": 2},
    {"name": "Keyboard", "price": 1200, "category": "Electronics", "quantity": 1}
]


# Lambda function to check discount eligibility
is_discount_eligible = lambda price: price > 500


# Function to calculate total price
def calculate_total(cart):
    return sum(item["price"] * item["quantity"] for item in cart)


# Function to calculate the discount for an item
def calculate_discount(item):
    name = item["name"]
    price = item["price"]
    category = item["category"]
    quantity = item["quantity"]

    # Special condition: Watch gets a flat 20% discount
    if name.lower() == "watch":
        discount_rate = 20

    else:
        # Basic discount based on item price
        if price > 1000:
            discount_rate = 15
        elif price >= 500:
            discount_rate = 10
        else:
            discount_rate = 0

        # Extra 5% discount for Electronics
        if category.lower() == "electronics":
            discount_rate += 5

        # Extra 5% discount for quantity of 4 or more
        if quantity >= 4:
            discount_rate += 5

    # Maximum discount cap: 25%
    discount_rate = min(discount_rate, 25)

    # Lambda condition: items priced at 500 or less are not eligible
    # for the basic price-based discount, but category and quantity
    # bonuses can still apply under the rules above.
    discount_amount = price * quantity * discount_rate / 100

    return discount_rate, discount_amount


# Function to display cart items and discounts
def display_cart(cart):
    print("\n========== SHOPPING CART ==========")

    for item in cart:
        total_item_price = item["price"] * item["quantity"]
        print(
            f"Item: {item['name']}, "
            f"Price: Rs.{item['price']:.2f}, "
            f"Quantity: {item['quantity']}, "
            f"Subtotal: Rs.{total_item_price:.2f}"
        )


# Function to apply discounts and calculate final price
def apply_discounts(cart):
    total_discount = 0

    print("\n========== DISCOUNT DETAILS ==========")

    for item in cart:
        discount_rate, discount_amount = calculate_discount(item)
        total_discount += discount_amount

        print(
            f"{item['name']}: "
            f"{discount_rate}% discount = Rs.{discount_amount:.2f}"
        )

    return total_discount


# Main program
def main():
    display_cart(shopping_cart)

    # Total before discount
    total_before_discount = calculate_total(shopping_cart)

    # Calculate total discount
    total_discount = apply_discounts(shopping_cart)

    # Total after discount
    total_after_discount = total_before_discount - total_discount

    print("\n========== BILL SUMMARY ==========")
    print(f"Total price before discount: Rs.{total_before_discount:.2f}")
    print(f"Total discount:              Rs.{total_discount:.2f}")
    print(f"Total price after discount:  Rs.{total_after_discount:.2f}")


# Program execution
if __name__ == "__main__":
    main()
