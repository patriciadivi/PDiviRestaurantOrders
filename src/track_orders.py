from src.analyze_log import mostRequestedByMaria, orderNotPlaced


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orderQuantity = []
        self.ordersComplete = []

    def __len__(self):
        return len(self.orderQuantity)

    def add_new_order(self, customer, order, day):
        self.ordersComplete.append(
            {"client": customer, "requests": order, "day": day}
        )
        self.orderQuantity.append('successfully created')

    def get_most_ordered_dish_per_customer(self, customer):
        return mostRequestedByMaria(self.ordersComplete, customer)

    def get_never_ordered_per_customer(self, customer):
        return orderNotPlaced(self.ordersComplete, 'requests', customer)

    def get_days_never_visited_per_customer(self, customer):
        return orderNotPlaced(self.ordersComplete, 'day', customer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
