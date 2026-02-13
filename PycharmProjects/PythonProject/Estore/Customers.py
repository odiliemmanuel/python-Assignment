from Estore.ShoppingCart import ShoppingCart


class Customers( ShoppingCart):

    def __init__(self, age, email, address, name, password, phone_number, billing_information, shopping_cart):
        self.__age = age
        self.__email_address = email
        self.__home_address = address
        self.__name = name
        self.__password = password
        self.__phone_number = phone_number
        self._BillingInformation = billing_information
        self.__ShoppingCart = shopping_cart
