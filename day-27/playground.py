# # arguments (tuple)
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total


# print(add(3, 5, 6))


# keyword arguments (dictionary)
def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiple']
    return n


print(calculate(2, add=3, multiple=5))


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')


my_car = Car(make='Ferrari')

print(my_car.make)
