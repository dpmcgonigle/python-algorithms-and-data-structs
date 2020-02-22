#! /usr/bin/env python
"""
linkedlist/__init__.py

This file will hold the main linked list classes.

Created by Dan McGonigle on 10/09/2019
"""
import operator
from abc import ABC, abstractmethod
from node import SinglyLinkedNode
from utils import listtype

#   ABSTRACT BASE CLASS FOR LINKEDLIST
###############################################################################################################
class LinkedList(ABC):
    """
    This is an abstract class that multiple types of linked lists will inherit from.

    Attributes:
        head (Node):    The first node of the linked list.

    Methods:
        insert (None):  Adds a node to the linked list.
        delete (None):  Deletes a node from the linked list.
        find   (Node):  Finds a node based on a given value.
        length (int):   Returns the length of the LinkedList
    """    
    def __init__(self):
        """Constructor for LinkedList abstract base class.  No paramters, defaults head Node to None."""
        self.head = None
        super().__init__()

    @abstractmethod
    def insert(self):
        """Adds a Node to the LinkedList.  To be implemented in all child classes."""
        pass

    @abstractmethod
    def delete(self):
        """Adds a Node to the LinkedList.  To be implemented in all child classes."""
        pass

    @abstractmethod
    def find(self):
        """Finds a Node in the LinkedList.  To be implemented in all child classes."""
        pass

    @property
    @abstractmethod
    def length(self):
        """Returns the length of the LinkedList.  To be implemented in all child classes."""
        pass

    def print(self):
        """Prints all of the values in the linked list."""
        ref = self.head
        counter = 0
        while ref:
            counter += 1
            print("List item %d: %s" % (counter, str(ref.get_value())))
            ref = ref.next
#   END LinkedList class
###############################################################################################################

#   SinglyLinkedList
###############################################################################################################
class SinglyLinkedList(LinkedList):
    """
    Class for unordered singly-linked list. New nodes are added to the end of the list.

    Attributes:
        head (Node):    The first node of the linked list.

    Methods:
        insert      (None):  Adds a node to the linked list.
        delete      (None):  Deletes a node from the linked list.
        find        (Node):  Finds a node based on a given value.
        length      (int):   Returns the length of the LinkedList
    """
    def __init__(self, items=None):
        """
        Constructor for SinglyLinkedList class.  

        Parameters:
            items   (list):     If provided, serves as the items to load into the linked list. 
                                If none, the SinglyLinkedList initializes as empty.
        """
        super().__init__()
        if not items:
            self.head = None
        else:
            assert isinstance(items, list) and len(items) > 0, "SinglyLinkedList(): constructor arg items needs to be a list."
            for item in items:
                self.insert(item)

    def insert(self, item):
        """
        Adds a Node to the end of the LinkedList.

        Parameters:
            value:              Item to be stored in a Node within the linked list.
        """
        if self.head:
            ref = self.head
            while ref.next:
                ref = ref.next
            ref.next = SinglyLinkedNode(item)
        else:
            self.head = SinglyLinkedNode(item)

    def delete(self, value):
        """
        Deletes all Nodes from the LinkedList with a given value.

        Parameters:
            value:              Item value whose Node we wish to delete from the linked list.
        """
        #   Delete head node until it doesn't contain the value we wish to delete
        while self.head.data == value:
            self.head = self.head.next if self.head.next else None
        #   Keep checking next node's value to see if we need to delete that node
        ref = self.head
        while ref.next:
            if ref.next.data == value:
                ref.next = ref.next.next if ref.next.next else None
            else:
                ref = ref.next

    def find(self, value):
        """
        Finds all Nodes in the LinkedList with a given value and returns a list of tuple index-value pairs.
        Note that if the list contains objects, the find and delete methods are probably not going to work unless you use references.

        Parameters:
            value:              Item value whose index and Node we wish to return.
        """
        founditems = []
        counter = 0
        ref = self.head
        #   Check head
        if ref.data == value:
            founditems += [(counter,ref)]
        #   Iterate through rest of list
        while ref.next:
            ref = ref.next
            counter += 1
            if ref.data == value:
                founditems += [(counter,ref)]
        return founditems

    def length(self):
        """Returns the length of the LinkedList."""
        counter = 0
        ref = self.head
        while ref:
            counter += 1
            ref = ref.next
        return counter

#   END SinglyLinkedList class
###############################################################################################################

#   OrderedSinglyLinkedList
###############################################################################################################
class OrderedSinglyLinkedList(SinglyLinkedList):
    """
    Class for unordered singly-linked list. New nodes are added to the end of the list.

    Attributes:
        head (Node):    The first node of the linked list.

    Methods:
        insert      (None):  Adds a node to the linked list.
        delete      (None):  Deletes a node from the linked list.
        find        (Node):  Finds a node based on a given value.
        length      (int):   Returns the length of the LinkedList
    """
    def __init__(self, items=None, key=None, reverse=False):
        """
        Constructor for SinglyLinkedList class.  

        Parameters:
            items   (list):     If provided, serves as the items to load into the linked list. Must all be numeric, or all of same obj type.
                                If none, the SinglyLinkedList initializes as empty.
            index   (str):      If a list of objects is provided, an index to a numeric property will need to be provided as well.
        """
        super().__init__()
        if reverse:
            self.comparison_op = operator.gt
        else:
            self.comparison_op = operator.lt
        self.key=None
        if not items:
            self.head = None
        else:
            assert isinstance(items, list) and len(items) > 0, "OrderedSinglyLinkedList(): constructor arg items needs to be a list."
            self.itemtype = listtype(items)
            assert self.itemtype not in [None, "mixed"], "OrderedSinglyLinkedList(): item list arg not homogenous."
            if self.itemtype not in [float, str]:
                self.key = key
                assert self.key is not None, "OrderedSinglyLinkedList(): itemtype %s requires a key for ordering." % str(self.itemtype)
            for item in items:
                self.insert(item)

    def insert(self, item, key=None):
        """
        Adds a Node to the LinkedList in order based on the value being inserted.

        Parameters:
            item:               Item to be stored in a Node within the linked list.
            key:                If the itemtype is not a number or string, an attribute name needs to be passed.
        """
        #   Need to set itemtype and key if not already set (i.e. new list)
        if not self.itemtype:
            self.itemtype = listtype([item])
        if not self.key:
            self.key = key
        value = self.get_value(item)

        if self.head:
            if self.comparison_op(value , self.head.get_value(key=self.key)):
                #   Put the new node at the beginning of the list
                node = SinglyLinkedNode(item)
                node.next = self.head
                self.head = node
                return
            
            #   Iterate through the list to find out where we go
            ref = self.head
            while ref.next:
                if self.comparison_op(value , ref.next.get_value(key=self.key)):
                    node = SinglyLinkedNode(item)
                    node.next = ref.next
                    ref.next = node
                    return
                ref = ref.next
            ref.next = SinglyLinkedNode(item)
        else:
            self.head = SinglyLinkedNode(item)

    def delete(self, value):
        """
        Deletes all Nodes from the LinkedList with a given value.

        Parameters:
            value:              Item value whose Node we wish to delete from the linked list.
        """
        #   Delete head node until it doesn't contain the value we wish to delete
        while self.get_value(self.head.data) == value:
            self.head = self.head.next if self.head.next else None
        #   Keep checking next node's value to see if we need to delete that node
        ref = self.head
        while ref.next:
            if self.get_value(ref.next.data) == value:
                ref.next = ref.next.next if ref.next.next else None
            else:
                ref = ref.next

    def find(self, value, key=None):
        """
        Finds all Nodes in the LinkedList with a given value and returns a list of tuple index-value pairs.

        Parameters:
            value:              Item value whose index and Node we wish to return.
        """
        founditems = []
        counter = 0

        ref = self.head
        #   Check head
        if self.get_value(ref.data) == value:
            founditems += [(counter,ref)]
        #   Iterate through rest of list
        while ref.next:
            ref = ref.next
            counter += 1
            if self.get_value(ref.data) == value:
                founditems += [(counter,ref)]
        return founditems

    def length(self):
        """Returns the length of the LinkedList."""
        counter = 0
        ref = self.head
        while ref:
            counter += 1
            ref = ref.next
        return counter

    def get_value(self,item):
        """Returns value of item(node) based on data type.  Object requires self.key to be set."""
        if self.itemtype not in [float, str]:
            value = getattr(item, self.key)
        else:
            value = item
        return value
#   END OrderedSinglyLinkedList class
###############################################################################################################
