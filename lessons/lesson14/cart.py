class Product:
    def __init__(self, name, category, price, unit):
        self.name = name
        self.category = category
        self.price = price
        self.unit = unit

    # determine whether the Product is edible
    def is_edible(self):
        if self.category != "Household products":
            return True
        else:
            return False

    # calculate the price for a certain quantity of the Product
    def price_total(self, quantity):
        return self.price * quantity


class Cart:
    """
    create a Cart object
    cart_contents is a list that contains lists with Product objects and their quantities
    """
    def __init__(self, cart_contents):
        self.cart_contents = cart_contents

    # return a total price of all products placed in the cart, takes in account product quantity
    def total(self):
        cart_total_price = 0
        for product in self.cart_contents:
            # return self.cart_contents[0].price * self.cart_contents[1]
            cart_total_price += product[0].price * product[1]
        return cart_total_price

    # determine whether everything in the cart is edible
    # if at least one item is not edible this will return False
    def totally_edible(self):
        for product in self.cart_contents:
            if not product[0].is_edible():
                return False
        return True


#
def run():
    """
    function that runs the code for testing:
    """
    # create 3 Product objects
    bread = Product('Bread', 'Food', 10.23, 'item')
    toilet_paper = Product('Toilet paper', 'Household products', 10.10, 'item')
    vodka = Product('Vodka', 'Alcohol', 65.00, 'item')
    # add them to the cart
    cart = Cart([[bread, 2], [toilet_paper, 8], [vodka, 2]])
    # test price_total method of the Product class by checking the price of three items of bread
    print(bread.price_total(3))
    # return the total price for every object in the cart, take in account quantity
    print(cart.total())
    # see if everything in the cart is edible
    print("Is everything in the cart edible? {}".format(cart.totally_edible()))


run()
