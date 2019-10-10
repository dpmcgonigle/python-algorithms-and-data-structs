#! /usr/bin/env python
"""
linkedlist/utils.py

This file will hold helper functions to be utilized in LinkedList structures.

    LIST OF FUNCTIONS
        listtype            -           returns the object type within the list

Created by Dan McGonigle on 10/09/2019
"""
def listtype(lst):
    """Returns the type of objects/data contained in a simple Python list. If multiple incompatible types, returns 'mixed'."""
    if len(lst) < 1:
        return None
    if all(isinstance(x, (int, float)) for x in lst):
        return float
    objtype = type(lst[0])
    if all(isinstance(x, objtype) for x in lst):
        return objtype
    return "mixed"
