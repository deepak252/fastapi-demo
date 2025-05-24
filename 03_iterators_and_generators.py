### Iterator
# iterator is an object in Python that lets you loop over a sequence of values, one element at a time, without needing to know the entire collection beforehand.

# An object that keeps state and produces the next value when you call next().
# It implements two methods:
# __iter__() → returns the iterator object itself
# __next__() → returns the next value or raises StopIteration

price = [1,2,3,9,8]

price_iter = price.__iter__()

print(price_iter.__next__())    # 1
print(price_iter.__next__())    # 2
print(price_iter.__next__())    # 3

while True:
    try:
        print(price_iter.__next__())    # 9 8
    except StopIteration:
        break


class InfiniteNaturalNumbers:
    def __init__(self) -> None:
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        num = self.num
        self.num+=1
        return num

itr2 = iter(InfiniteNaturalNumbers())

print(itr2.__next__())  # 1
print(itr2.__next__())  # 2
print(itr2.__next__())  # 3




### Generators
# A generator is a special type of iterator in Python that allows you to yield values one at a time, using the yield keyword, instead of returning them all at once.

print("Generators")
def return_values():
    yield 1
    yield 2
    yield "Three"

values = return_values()
print(values.__next__())    # 1
print(values.__next__())    # 2
print(values.__next__())   # Three 
# print(values.__next__())    # ERROR


## Example 2
def count_up_to(n):
    i = 1
    while i<=n:
        yield i

counter_gen = count_up_to(10)
print(next(counter_gen))    # 1
print(next(counter_gen))    # 2
print(next(counter_gen))    # 3

