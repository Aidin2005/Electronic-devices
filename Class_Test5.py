import unittest
from io import StringIO
from Class_Device import Device, Smartphone, Laptop, Tablet, Cart
import sys

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device = Device("Test Device", 100, 10, 12)
        self.smartphone = Smartphone("Test Phone", 500, 5, 24, 6.1, 20)
        self.laptop = Laptop("Test Laptop", 1500, 3, 24, 16, 3.2)
        self.tablet = Tablet("Test Tablet", 700, 8, 12, "2560x1600", 600)
        self.cart = Cart()
    
    def test_device_show_info(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.device.show_info()
        sys.stdout = sys.__stdout__
        self.assertIn("Test Device", captured_output.getvalue())

    def test_reduce_stock(self):
        self.device.reduce_stock(3)
        self.assertEqual(self.device.stock, 7)

    def test_reduce_stock_not_enough(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.device.reduce_stock(20)
        sys.stdout = sys.__stdout__
        self.assertIn("Not enough stock", captured_output.getvalue())

    def test_smartphone_show_info(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.smartphone.show_info()
        sys.stdout = sys.__stdout__
        self.assertIn("Test Phone", captured_output.getvalue())
    
    def test_cart_add_item(self):
        self.cart.add_item(self.device, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.total, 200)
    
    def test_cart_add_item_not_enough_stock(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.cart.add_item(self.device, 20)
        sys.stdout = sys.__stdout__
        self.assertIn("Cannot add", captured_output.getvalue())
    
    def test_cart_checkout(self):
        self.cart.add_item(self.device, 2)
        self.cart.checkout()
        self.assertEqual(self.cart.items, [])
        self.assertEqual(self.cart.total, 0)
        self.assertEqual(self.device.stock, 8)

if __name__ == "__main__":
    unittest.main()
