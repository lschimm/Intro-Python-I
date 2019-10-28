"""
A department store has departments in it, and each department can have one of more types of items in the inventory. You can query the store to see all the departments, and query each department to see all the items in that department

1. What are the nouns? These nouns tend to be classes. Find the "things"
  Store
  Depts
  Items
  Inventory

2. What are the verbs? What can we do to the nouns? These tend to be "methods" (function) on the class
* query items in the store
* query items in the dept

3. Look for "has-a" relationship. These tend to be attributes on the object
* store has depts
* dept has types of item in the inventory
* store has a type

4. Look for "is-a" relationship. These tend to indicate class hierarchy

"""


class Store:  # constructor begins function below
    def __init__(self, store_type, depts=[]):
        self.store_type = store_type
        self.depts = depts

    def add_dept(self, dept):  # method to add a store
        self.depts.append(dept)

    def __str__(self):  # for human consumption -- string method
        s = f"Store (type: {self.store_type})"

        for d in self.depts:
            s += f"    {d}\n"

        return s

    def __repr__(self):  # for programmer consumption -- represent method
        # return f'Store("{self.store_type}")'
        return f'Store({repr(self.store_type)}, ({repr(self.depts)})'


class Dept:
    def __init__(self, name, inventory=[]):
        self.name = name
        self.inventory = inventory

    def __repr__(self):  # for programmer consumption -- represent method
        # return f'Store("{self.store_type}")'
        return f'Dept({repr(self.name)}, ({repr(self.inventory)})'


class Item:
    pass


d0 = Dept("produce")
d1 = Dept("dairy")
d2 = Dept("bakery")

s = Store("grocery", [d0, d1, d2]) # instantiation

dn = input("Enter a department number: ")

dn = int(dn) # convert from str to num

print(s.depts[dn])