# from typing import List, Tuple, Dict, Union

# list1: List[int] = [1,2,3]
# tup1: Tuple[str, str, int] = ("Name", "email", 12)
# dict1: Dict[str, int] = {
#     "stock1": 3,
#     "stock2": 5,
# }
# list2: List[Union[int, float]] = []
# print(tup1[0])

# In Python 3.9+, you don't need to import things like List, Dict from typing—you can use built-in generics directly
# def sum_numbers(numbers: list[int]) -> int:
#     return sum(numbers)

list1: list[int] = [1,2,3]
tup1: tuple[str, str, int] = ("Name", "email", 12)
dict1: dict[str, int] = {
    "stock1": 3,
    "stock2": 5,
}
list2: list[int | float] = []

### Function
def func1(value: int) -> float | None:
    try:
        return float(value)
    except TypeError:
        return None
print(func1(20))


### Custom Types
Image = list[list[int]]
img1: Image = [[1,2,3], [4,5,]]
print(type(img1))   # <class 'list'>


from typing import Optional, List

class Job:
    def __init__(self, title: str, desc: Optional[str]) -> None:
        self.title = title
        self.desc = desc
    
    def __repr__(self) -> str:
        return self.title

job1 = Job(title="Team Lead", desc="sdf")
job2 = Job(title="SDE1", desc="asdf")

jobs:List[Job] = [job1, job2]
print(jobs)



### type for callback functions (Callable)
from typing import Callable


def smart_divide(func: Callable[[int, int], float | None]):
    def inner(a, b):
        if b==0:
            print("Division by 0")
            return None
        return func(a, b)
    
    return inner

@smart_divide
def divide(a, b):
    return a/b


print(divide(9, 2))

