# type-annotated assignment introduced in Python 3.6+ using type hints
## Also helps in suggestions for the variables eg. num1.<Suggestions for Integer>

num1: int = 12
str1: str = "Test"

# Note: Python is dynamically typed. This hint is not enforced at runtime unless you use additional tools.
# static type checker: "mypy"
def get_total(price1: int, price2: int) -> int:
    return price1+price2


print(get_total(2,3))