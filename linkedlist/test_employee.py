#! /usr/bin/env python
"""
linkedlist/test_employee.py

This is a simple employee class I made to test out the linked list's functionality of working with objects.

NOTE: run this script with the -i (interactive) option set to play around with the linked lists
    ex: python -i test_employees.py

Created by Dan McGonigle on 10/09/2019
"""
from __init__ import SinglyLinkedList, OrderedSinglyLinkedList

class Employee(object):
    """
    Dummy class for testing out whether the linked list classes work with objects.

    Attributes
        fname:  str
        lname:  str
        age:    int
    """    

    def __init__(self, fname: str, lname: str, age: int):
        """Constructor for test Employee class."""
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.age = int(age)

    def __str__(self):
        """Pretty print the Employee."""
        return "Employee: %s %s, Age: %d" % (self.fname, self.lname, self.age)

#   M   A   A   I   N   S
if __name__ == "__main__":
    emplist = [
        Employee(fname="Dan", lname="McGonigle", age="33"),
        Employee(fname="Dan", lname="McGonigle", age="71"),
        Employee(fname="Buster", lname="Rodriguez", age="4"),
        Employee(fname="Desiree", lname="Pombo", age="36"),
        Employee(fname="Cora", lname="Loo", age="8")
    ]

    numlist = [6,2,78,3,1,45]

    #ll = SinglyLinkedList(emplist)
    #print("SinglyLinkedList ll created.  dir(ll): %s\n" % str(dir(ll)))
    #oll_fname = OrderedSinglyLinkedList(items=emplist, key="fname")
    #print("OrderedSinglyLinkedList oll_fname created.  dir(oll_fname): %s\n" % str(dir(oll_fname)))
    oll_age = OrderedSinglyLinkedList(items=emplist, key="age")
    print("OrderedSinglyLinkedList oll_age created.  dir(oll_age): %s\n" % str(dir(oll_age)))
    oll_age_rev = OrderedSinglyLinkedList(items=emplist, key="age", reverse=True)
    print("OrderedSinglyLinkedList oll_age_rev created.  dir(oll_age_rev): %s\n" % str(dir(oll_age_rev)))
    #oll_num = OrderedSinglyLinkedList(items=numlist)
    #print("OrderedSinglyLinkedList oll_num created.  dir(oll_num): %s\n" % str(dir(oll_num)))
