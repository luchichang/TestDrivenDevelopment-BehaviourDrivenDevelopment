"""Implements a Stack data structure"""
# importing "any" Type  form the "typing" module for annotation purpose
from typing import Any


class Stack:
    """Implements a Stack data structure"""

    def __init__(self):
        """Constructor"""
        """INFO: "self" parameter is used to refer the instance of the class itself"""
        self.items = [] 
    
    def push(self, data: Any) -> None: 
        """Places an item onto the stack"""
        self.items.append(data) 
    
    def pop(self) -> Any:
        """Removes an item from the stack and returns it"""
        return self.items.pop() 
        
    def peek(self) -> Any:
        """Returns the item at the top of the stack without removing it"""
        return self.items[-1] 
        
    def is_empty(self) -> bool:
        """Returns True if the stack is empty, otherwise returns False"""
        return len(self.items) == 0
