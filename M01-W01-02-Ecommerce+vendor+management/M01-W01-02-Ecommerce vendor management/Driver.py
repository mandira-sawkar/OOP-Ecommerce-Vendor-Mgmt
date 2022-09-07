from pprint import pprint

from Implementation.ProductsImplementation import ProductsImplementation
from Implementation.VendorImplementation import VendorImplementation
from Models.VendorSessionModel import VendorSessionModel

if __name__ == '__main__':

    vendor = VendorImplementation()

    login_res = vendor.login('Rossum', 'rossum_pw')
    if not login_res:
        print("Not Authorized Vendor")
    else:
        products = ProductsImplementation('Rossum')
        products.add_product("Lenovo Thinkpad", "Laptop", 40, 20000)
        products.add_product("Dell Inspiron", "Laptop", 40, 30000)
        products.add_product("Acer razor", "Laptop", 40, 25000)        
        products.add_product("Asus Tinker", "Laptop", 40, 20000)
        products.add_product("Lenovo Gaming", "Laptop", 40, 20000)

        search_product = products.search_product_by_name("Lenovo Gaming")
        if search_product:
            pprint(search_product)
            print()
        else:
            print("No product exists by the name\n")
        
        all_products = products.get_all_products()

        if all_products:
            pprint(all_products)
            print()
        else:
            print("No product is available to fetch.\n")
            
        vendor.logout("Rossum")
