from unittest import TestCase

from stack import Stack

# creating the child class with testcase as a parent class

class TestStack(TestCase):
    """Test cases for stack"""

# NOTE: here self indicates the instance of the object similar to this in java
    def setUp(self):
        """setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None
    
    # def test_push(self):
    #     """Test pushing an item into the stack"""
    #     raise Exception("not implemented")

    def test_pop(self):
        """Test popping an item of off the stack"""
        raise Exception("not implemented")

    def test_peek(self):
        """Test peeking at the top the stack"""
        raise Exception("not implemented")

    def test_is_empty(self):
        """Test if the stack is empty"""
        raise Exception("not implemented")
    
    # def test_push(self):
    #     """Test pushing an item into the stack"""
    #     self.stack.push(8)
    #     self.stack.push(3)
    #     self.assertEqual(self.stack.peek(), 3)
    #     self.stack.pop()
    #     self.assertFalse(self.stack.is_empty())

    # def test_peek(self):
    #     """Test peeking at the top the stack"""
    #     self.stack.push(3)
    #     self.stack.push(5)
    #     self.assertEqual(self.stack.peek(), 5)


    # def test_pop(self):
    #     """Test popping an item of off the stack"""
    #     self.stack.push(5)
    #     self.stack.push(8)
    #     self.assertEqual(self.stack.pop(), 8)
    #     self.assertEqual(self.stack.peek(),5)
    #     self.stack.pop()
    #     self.assertTrue(self.stack.is_empty()) 
   
    # def test_is_empty(self):
    #     """Test if the stack is empty"""
    #     self.stack.push(5)
    #     self.assertFalse(self.stack.is_empty())
    #     self.stack.pop()
    #     self.assertTrue(self.stack.is_empty())
        

  
