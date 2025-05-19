class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if self._orders:
            total = sum(order.price for order in self._orders)
            return round(total / len(self._orders), 2) 
        return 0.0 
