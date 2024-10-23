from typing import Optional

def get_full_name(first_name: str, last_name: str):
    return f"{first_name.title()} {last_name.title()}"

print(get_full_name(first_name="pedro", last_name="ruviaro"))

def get_name_with_age(name: str, age: int) -> str:
    return name + " has " + str(age) + " years old"  # f"{name} has {age}"

print(get_name_with_age("john", 28))


def process_list(items: list[str]) -> str:
    response = ""
    for item in items:
        response = response + " " + item
    return response 

print(process_list(["Banana", "Apple", "Orange"]))


def process_dict(obj: dict[str, int]):
    for item_name, item_price in obj.items():
        return item_name, item_price

products = {
    "apple": "2",
    "pear": 10
}

print(process_dict(products))


def union_func(x: str | int):
    pass

def option_func(par: Optional[str] = None):
    if par is not None:
        print(par)
    else:
        print("No pars...")

option_func()
option_func("Hello")

def option_func2(par: str | None = None):
    if par is not None:
        print(par)
    else:
        print("No pars...")

option_func2()
option_func2("Hello")



def say_hi(name: str | None):
    print(f"Hey {name}!")

say_hi(name=None)
say_hi("Hello")

# Classes
class Person():
    def __init__(self, name: str) -> None:
        self.name = name

def person_name(person: Person):
    return person.name.title()

user = Person(name='John Doe')
person_name(user)