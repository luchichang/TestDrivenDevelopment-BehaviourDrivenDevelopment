# Test coverage for the Flask Web Application

## Description
what will be the limit or boundary to the test to mention that all the code are perfectly tested it is possible with coverage package which shows the no of lines of code executed


## Pre-Requisites

### 1. Happy Paths
- **Happy Path**: Verifies that the function returns the expected value when a positive outcome is tested.

### 2. Sad Paths
- **Sad Path**: Ensures the function responds appropriately to exceptions without breaking when a negative outcome is tested.

### 3. Test Fixtures
- **Test Fixtures**: Establish a known initial state before and after each test. Test fixtures are useful for various testing situations, such as creating mock data objects and loading the database with a known dataset.

#### Test fixtures operate at three levels of specificity:

#### Module Level
Runs once before and after all tests in the module.

```python
def setUpModule():             # Runs once before any tests


def tearDownModule():          # Runs once after all tests
    
```

### TestCase Level
Runs once before and after the test case class.

``` python
@classmethod
def setUpClass(cls):           # Runs once before the test case class
    
@classmethod
def tearDownClass(cls):        # Runs once after the test case class

```

### Test Level
Runs before and after each individual test.

``` python

def setUp(self):               # Runs before each test


def tearDown(self):            # Runs after each test

```

## steps for performing the test coverage

* before modifying the ensure the code runs perfectly. by running the command in the terminal
   
   ``` bash
       nosetests
   ```
* now at the bottom of the console output you will encounter the coverage report of the tested module along with its code coverage percentage

* 
