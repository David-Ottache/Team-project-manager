def add_to_cart(item_name, price, *args, **kwargs):
    # Apply discounts (If any)
    final_price = price
    for discount in args:
        final_price -= (final_price * discount/100)

    #Build the item details string
    details = ", ".join([f"{key}={value}" for key, value in kwargs.items()])

    return final_price, details    


def main():
    cart = [] #To store all the cart items
    total_cost = 0 #To calculate total cost

    print("Welcome to the Shopping Cart Program created by Otteez!")

    while True:
        item_name = input("\n Enter Item name (or 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break

        # Get Item price and ensure it's a valid number
        try:
            price = float(input("Enter item price: ").strip())
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            continue
        # Get discounts

        discounts_input = input("Enter discounts(if any, separated by spaces): ").strip()
        discounts = [float(discount) for discount in discounts_input.split() if discount.isdigit()]

        #check if item already exists in the cart
        if any(item['name'] == item_name for item in cart):
            print(f"item '{item_name}' is already in the cart. Skipping duplicate.")
            continue
        
        # Add item to cart
        final_price, item_details = add_to_cart(item_name, price, *discounts, **details)
        cart.append({'name': item_name, 'price': final_price, 'details': item_details})
        total_cost += final_price
        print(f"Item added: {item_name} - Final Price: ${final_price:.2f}")
    
    # Display cart summary
    print("\n--- Cart Summary ---")
    for item in cart:
        print(f"{item['name']} - ${item['price']:.2f} ({item['details']})")
    print(f"Total Cost: ${total_cost:.2f}")


# Run the program
if __name__ == "__main__":
    main()


