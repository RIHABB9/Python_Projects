class Cart (object):
    def __init__(self):
        self.items = {} # item name -> (price, quantity)

    def add_item(self, name, price, quantity):
        name = name.strip().lower()
        if name in self.items:
            # item exist already -> update its qty
            current_price, current_quantity = self.items[name]
            self.items[name] = (price, current_quantity + quantity)
            print(f"Updated '{name}' with new quantity: {current_quantity + quantity}") 
        else:
            # item doesn't exist (new)
            self.items[name] = (price, quantity)
            print(f"Added '{name}' to cart")

    def remove_item(self, name):
        name = name.strip().lower()
        if name in self.items:
            del self.items[name]
            print(f"'{name}' removed from cart.")
        else:
            print(f"'{name}' is not in the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("--- Shopping Cart ---")
            print("Item\tPrice\tQuantity")
            for name, (price, quantity) in self.items.items():
                print(f"{name}\t{price:.2f}\t{quantity}")

    def get_total(self):
        total = 0
        for price, quantity in self.items.values():
            total += (price * quantity)
        print(f"Total price: ${total:.2f}")

    def clear_cart(self):
        self.items.clear()
        print("Cart has been cleared.")

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value must be positive.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def show_menu():
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Get Total")
    print("5. Clear Cart")
    print("6. Exit")

# Main program
cart = Cart()

while True:
    show_menu()
    while True:
        try:
            choice = int(input("Choose an option: "))
            if choice not in range(1,7):
                raise ValueError
        except ValueError as e:
            print(e)
            continue
        else:
            break

    if choice == 1:
        print("Enter item details: ")
        name = input("Item name: ").strip().lower()
        price = get_valid_float("Price: ")
        quantity = get_valid_int("Quantity:")
        cart.add_item(name, price, quantity)

    elif choice == 2:
        name = input("Enter item name to remove: ").strip().lower()
        cart.remove_item(name)

    elif choice == 3:
        cart.view_cart()

    elif choice == 4:
        cart.get_total()

    elif choice == 5:
        cart.clear_cart()

    elif choice == 6:
        print("Thanks for shopping. Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 6.")
