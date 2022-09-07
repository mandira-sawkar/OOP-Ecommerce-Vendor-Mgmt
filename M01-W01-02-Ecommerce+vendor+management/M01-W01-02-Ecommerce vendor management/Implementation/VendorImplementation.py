from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()
        self.check_vendor = False
        self.check_logout = False

    def login(self, username, password):
        self.check_vendor = self.vendor_model.is_correct_vendor(username, password)
        if self.check_vendor:
            self.vendor_session.login(username)
            if self.vendor_session.check_login(username):
                print(f"User {username} logged in successfully!\n")
                return True
        else:
            print("Invalid username or password.")
            return False
        # Add you code here after verifying the vendor data exists in the dictionary

    def logout(self, username):
        if self.vendor_session.check_login(username):
            self.check_logout = self.vendor_session.logout(username)
            if self.check_logout:
                if not self.vendor_session.check_login(username):
                    print(f"User {username} logged out successfully!")
            else:
                print("Logout unsuccessful.")
        else:
            print("Incorrect username. Logout unsuccessful")
        # Add your code here to log out the current vendor
