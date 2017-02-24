#!/usr/bin/python
# Queue.py

""" Queue Class
Implement a growable and shrinkable queue with an array as
the underlying data structure

IMPORTANT: Do not use the python's built-in Queue functionality.
Python has Queue functionality built into its lists. You will
receive no credit for using any built in Queue functionality.
"""

import string


class Queue:

    def __init__(self, initial_capacity):
    """init: queue * num -> .
    purpose: initialize queue
    consumes: a queue and a number
    Produces: nothing
    Raises: InvalidInputException:  initial_capacity negative or null
    Example: Queue(9) -> An Empty Queue with space for 9 elements
    """
        pass

    def size(self):
    """size: queue -> num
    purpose: returns number of items currently in queue
    consumes: a queue
    Produces: the number of items in the queue
    Example: size() -> 9
    """
        return 0

    def is_empty(self):
    """is_empty: queue -> bool
    purpose: tell whether the queue is empty or not
    consumes: a queue
    Produces: boolean
    Example: is_empty() -> false
    """
        return False

    def enqueue(self,any):
    """enqueue: queue * any -> .
    purpose: add an arbitrary type to the end of the queue
    consumes: a queue and an arbitrary type
    Produces: nothing
    Example: enqueue("sarah") -> the string sarah is added to the end of the queue
    """
        pass

    def dequeue(self):
    """dequeue: queue -> any
    purpose: removes and returns first item in queue
    (throws EmptyQueueException if empty)
    consumes: a queue
    Produces: first element in the queue
    Raises: EmptyQueueException: trying to dequeue from empty queue
    Example: dequeue() -> "sarah"
    """
        return None

    def front(self):
    """front: queue ->  any
    purpose: returns first item in queue without removing it (throws empty queue exception if empty)
    consumes: a queue
    Produces: the first item in the queue
    Raises: EmptyQueueException: trying to find element from empty queue
    Example: front() -> "sarah"
    """
        return None

    def capacity(self):
    """capacity: queue -> num
    purpose: returns how many elements the queue can hold
    consumes: a queue
    Produces: number of elements the queue can hold
    Example: capacity() -> 16
    """
        return 0



class EmptyQueueException(Exception):
"""EmptyQueueException: Exception -> stack trace
purpose: produce stack trace when an error is encountered due to an empty queue
consumes: an exception
Produces: stack trace
Example: raise EmptyQueueException
"""
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidInputException(Exception):
"""InvalidInputException: Exception -> stack trace
purpose: produce stack trace when an error is encountered due to an invalid input
consumes: an exception
produces: stack trace
Example: raise InvalidInputException
"""
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
