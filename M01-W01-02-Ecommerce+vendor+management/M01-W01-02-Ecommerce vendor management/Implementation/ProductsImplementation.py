from pprint import pprint

from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel


class ProductsImplementation(Products):

    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username
        self.check_add_product = False
        self.login_check = self.vendor_session.check_login(self._username)
        self.product_details = None
        self.all_products = None

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        if self.login_check:
            self.check_add_product = self.product_model.add_product(product_name, product_type, available_quantity, unit_price)
            if self.check_add_product:
                return True
            else:
                return False
        else:
            print("User not logged in. Please login.")
            return False
        # check if the vendor is logged in, then add the product and return True else Return False
            
    def search_product_by_name(self, product_name):
        if self.login_check:
            self.product_details = self.product_model.search_product(product_name)
            if self.product_details:
                print("Product found!")
                return self.product_details
            else:
                return False
        else:
            print("User not logged in. Please login.")
            return False

        # Search if the product is available in the dictionary if the vendor is authorized to access else return False
        # If product is available then return product

    def get_all_products(self):
        if self.login_check:
            self.all_products = self.product_model.all_products()
            if self.all_products:
                print("Displaying all products:")
                return self.all_products
            else:
                return False
        else:
            print("User not logged in. Please login.")
            return False
        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products 

