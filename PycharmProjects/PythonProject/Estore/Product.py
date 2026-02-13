class Product():
    def __init__(self, product_id, product_name, price, description, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.description = description
        self.__category = category
