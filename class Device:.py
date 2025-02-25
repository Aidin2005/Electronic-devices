class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty

    def show_info(self):
        print(f"Device: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months")

    def reduce_stock(self, amount):
        if self.stock >= amount:
            self.stock -= amount
            print(f"Stock updated. Remaining {self.name}: {self.stock}")
        else:
            print(f"Not enough stock for {self.name}. Only {self.stock} left.")

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery = battery

    def show_info(self):
        print(f"Smartphone: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months, Screen: {self.screen_size} inches, Battery: {self.battery} hours")

class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram, processor):
        super().__init__(name, price, stock, warranty)
        self.ram = ram
        self.processor = processor

    def show_info(self):
        print(f"Laptop: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months, RAM: {self.ram} GB, Processor: {self.processor} GHz")

class Tablet(Device):
    def __init__(self, name, price, stock, warranty, resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.resolution = resolution
        self.weight = weight

    def show_info(self):
        print(f"Tablet: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months, Resolution: {self.resolution}, Weight: {self.weight} grams")


class Cart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, device, quantity):
        if device.stock >= quantity:
            self.items.append((device, quantity))
            self.total += device.price * quantity
            print(f"Added {quantity} {device.name}(s) to cart.")
        else:
            print(f"Cannot add {quantity} {device.name}(s). Only {device.stock} in stock.")

    def show_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your cart:")
            for item in self.items:
                print(f"{item[1]} x {item[0].name} - ${item[0].price * item[1]}")
            print(f"Total: ${self.total}")

    def checkout(self):
        if not self.items:
            print("Cart is empty. Nothing to checkout.")
        else:
            print("Checking out...")
            for item in self.items:
                item[0].reduce_stock(item[1])
            print(f"Total amount to pay: ${self.total}")
            self.items = []
            self.total = 0
            print("Thank you for shopping with us!")



def main():
    #  devices
    devices = [
        Smartphone("iPhone 13", 799, 10, 12, 6.1, 24),
        Smartphone("Samsung Galaxy S21", 699, 15, 12, 6.2, 20),
        Laptop("MacBook Pro", 1999, 5, 24, 16, 3.2),
        Laptop("Dell XPS 13", 1299, 8, 12, 8, 2.8),
        Tablet("iPad Pro", 999, 12, 12, "2732x2048", 682),
        Tablet("Samsung Galaxy Tab S7", 649, 7, 12, "2560x1600", 498),
        Smartphone("Google Pixel 6", 599, 8, 12, 6.4, 22),
        Laptop("HP Spectre x360", 1499, 6, 12, 16, 3.0),
        Tablet("Microsoft Surface Pro 8", 1299, 5, 12, "2880x1920", 891),
        Smartphone("OnePlus 9", 729, 12, 12, 6.55, 25),
        Laptop("Lenovo ThinkPad X1", 1699, 4, 12, 16, 3.1),
        Tablet("Amazon Fire HD 10", 149, 20, 6, "1920x1200", 465),
        Smartphone("Xiaomi Mi 11", 749, 7, 12, 6.81, 20),
        Laptop("Asus ROG Zephyrus", 1999, 3, 12, 32, 3.5),
        Tablet("Lenovo Tab P11 Pro", 499, 9, 12, "2560x1600", 485),
        Smartphone("iPhone SE", 399, 10, 12, 4.7, 15),
        Smartphone("Samsung Galaxy A52", 499, 12, 12, 6.5, 18),
        Laptop("Acer Swift 3", 899, 7, 12, 8, 2.4),
        Laptop("Razer Blade 15", 2499, 2, 12, 32, 4.0),
        Tablet("Huawei MatePad Pro", 799, 6, 12, "2560x1600", 460)
    ]

    cart = Cart()

    while True:
        print("\n--- Electronic Store ---")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Devices:")
            for i, device in enumerate(devices):
                print(f"{i + 1}. ", end="")
                device.show_info()
            device_choice = int(input("Enter device number to add to cart: ")) - 1
            if 0 <= device_choice < len(devices):
                quantity = int(input("Enter quantity: "))
                cart.add_item(devices[device_choice], quantity)
            else:
                print("Invalid device number.")

        elif choice == "2":
            cart.show_cart()
            checkout = input("Do you want to checkout? (yes/no): ").lower()
            if checkout == "yes":
                cart.checkout()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()