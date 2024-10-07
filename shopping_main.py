
# Importing Item and ShoppingCart classes
from shopping_cart import ShoppingCart, Item
# Writing main script
def main():
    cart = ShoppingCart()
    while True:
        try:
            action = input("Choose action: add, remove, view, checkout: ").lower()
            if action not in ['add', 'remove', 'view', 'checkout']:
                raise ValueError
            if action == "add":
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                category = input("Enter item category: ")
                quantity = int(input("Enter quantity: "))
                cart.add_item(Item(name, price, category), quantity)
            elif action == "remove":
                name = input("Enter item name: ")
                cart.remove_item(name)
            elif action == "view":
                cart.view_cart()
            elif action == "checkout":
                cart.checkout()
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()