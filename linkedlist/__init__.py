#! /usr/bin/env python
"""
linkedlist/__init__.py

This file will hold the main linked list classes.

Created by Dan McGonigle on 10/09/2019
"""
from abc import ABC, abstractmethod
from node import SinglyLinkedNode

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
            print("List item %d: %s" % (counter, str(ref.get_data())))
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
        if not items:
            self.head = None
        super().__init__()

    def insert(self, value):
        """
        Adds a Node to the end of the LinkedList.

        Parameters:
            value:              Item to be stored in a Node within the linked list.
        """
        if self.head:
            ref = self.head
            while ref.next:
                ref = ref.next
            ref.next = SinglyLinkedNode(value)
        else:
            self.head = SinglyLinkedNode(value)

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
    def __init__(self, items=None):
        """
        Constructor for SinglyLinkedList class.  

        Parameters:
            items   (list):     If provided, serves as the items to load into the linked list. 
                                If none, the SinglyLinkedList initializes as empty.
        """
        #if not items:
        #    self.head = None
        super().__init__()

    def insert(self, value):
        """
        Adds a Node to the LinkedList in order based on the value being inserted.

        Parameters:
            value:              Item to be stored in a Node within the linked list.
        """
        if self.head:
            if value < self.head.get_data():
                #   Put the new node at the beginning of the list
                node = SinglyLinkedNode(value)
                node.next = self.head
                self.head = node
                return
            
            #   Iterate through the list to find out where we go
            ref = self.head
            while ref.next:
                if value < ref.next.get_data():
                    node = SinglyLinkedNode(value)
                    node.next = ref.next.next
                    ref.next = node
                    return
                ref = ref.next
            ref.next = SinglyLinkedNode(value)
        else:
            self.head = SinglyLinkedNode(value)

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

#   END OrderedSinglyLinkedList class
###############################################################################################################
