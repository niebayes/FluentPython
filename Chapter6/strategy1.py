import inspect

from Order1 import *
import promotions

promos = [func for name, func in 
              inspect.getmembers(promotions, inspect.isfunction)]

def best_promo(order):
    return max(promo(order) for promo in promos)

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]
print(Order(joe, cart, best_promo), Order(ann, cart, best_promo))

banana_cart = [LineItem('banana', 30, .5),
            LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, best_promo))

long_cart = [LineItem(str(item_code), 1, 1.0)
            for item_code in range(10)]
print(Order(joe, long_cart, best_promo))