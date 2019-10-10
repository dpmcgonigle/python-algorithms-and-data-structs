#! /usr/bin/env python
"""
linkedlist/node.py

This file will hold the Node classes to be utilized in LinkedList structures.

Created by Dan McGonigle on 10/09/2019
"""
from abc import ABC, abstractmethod

class Node(ABC):
    """
    This is an abstract class that multiple types of Nodes that will be utilized by .

    Attributes:
        data:           The data held by this Node.

    Methods:
        get_data:       Returns the data being held within the node
    """    

    @abstractmethod
    def __init__(self):
        """Constructor for Node abstract base class.  No paramters, defaults head Node to None."""
        self.data = None
        super().__init__()

    @abstractmethod
    def get_data(self):
        pass

class SinglyLinkedNode(Node):
    """
    LinkedList Node for a singly-linked list.

    Attributes:
        data:
        next (Node):    Reference to the next node within the LinkedList.

    Methods:
        get_data:       Returns the data being held within the node.
    """
    def __init__(self, data):
        """Constructor for the singly-linked list Node class."""
        self.data = data
        self.next = None
        
    def get_data(self):
        """Returns data from the Node."""
        return self.data
