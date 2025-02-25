# UML
![image](https://github.com/user-attachments/assets/a88911ea-1f0a-4c6f-8712-e9b538b10202)


# Class test
<img width="508" alt="Screenshot 2025-02-25 at 5 13 16 PM" src="https://github.com/user-attachments/assets/3f8dcbcd-e485-4442-94b0-06c7e48c6372" />

# How It Works

### Device Classes:
There’s a base class called Device that stores common details like name, price, stock, and warranty.
Three subclasses (Smartphone, Laptop, Tablet) inherit from Device and add their own unique features (e.g., screen size for smartphones, RAM for laptops).
Shopping Cart:
The Cart class manages the items a user wants to buy.
Users can add or remove items, view their cart, and checkout.
During checkout, the stock of each device is updated.
Main Program:
A list of 20 devices is created (smartphones, laptops, and tablets).
A menu lets users:
View all devices.
Add devices to their cart.
View their cart and checkout.
Key Features

### Simple Menu: Users can interact with the program using a text-based menu.
Stock Management: The program reduces the stock of devices when they are purchased.
Basic Calculations: It calculates the total price of items in the cart.
Example Interaction

### The user selects "Show Devices" to see all available devices.
They choose a device (e.g., iPhone 13) and specify how many they want.
The device is added to their cart.
They can view their cart and checkout, which updates the stock and shows the total price.
# How to Run the Code

## Requirements
- Python 3.x installed (check with `python --version`)

## Setup
1. Navigate to the project directory:
   ```sh
   cd path/to/project
   ```
2. Run the main script:
   ```sh
   python store.py
   ```

## Running Tests
Execute tests with:
```sh
python -m unittest test_device.py
```

## Troubleshooting
- Ensure correct directory.
- Fix `ModuleNotFoundError` by verifying imports.

## Contributing
Fork and submit pull requests for improvements.


# Sample input/output.

When you run the program, it will look like this in the terminal:

```plaintext
--- Electronic Store ---
1. Show Devices
2. Show Cart
3. Exit
Enter your choice: 1

Available Devices:
1. Smartphone: iPhone 13, Price: $799, Stock: 10, Warranty: 12 months, Screen: 6.1 inches, Battery: 24 hours
2. Smartphone: Samsung Galaxy S21, Price: $699, Stock: 15, Warranty: 12 months, Screen: 6.2 inches, Battery: 20 hours
3. Laptop: MacBook Pro, Price: $1999, Stock: 5, Warranty: 24 months, RAM: 16 GB, Processor: 3.2 GHz
...

Enter device number to add to cart: 1
Enter quantity: 2
Added 2 iPhone 13(s) to cart.

--- Electronic Store ---
1. Show Devices
2. Show Cart
3. Exit
Enter your choice: 2

Your cart:
2 x iPhone 13 - $1598
Total: $1598

Do you want to checkout? (yes/no): yes
Checking out...
Stock updated. Remaining iPhone 13: 8
Total amount to pay: $1598
Thank you for shopping with us!

--- Electronic Store ---
1. Show Devices
2. Show Cart
3. Exit
Enter your choice: 3

Goodbye!
