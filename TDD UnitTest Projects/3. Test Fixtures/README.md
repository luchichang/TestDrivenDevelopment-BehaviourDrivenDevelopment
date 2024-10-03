# Test Fixtures for the Flask Web Application

## Description,
      adding the Text fixtures for the flask web application using SqlAlchemy toolkit and performs basic account creation, update and delete operations

## Pre Requisite 
  * Happy Paths
      happy path verifies that whether function returns  the expected value when Positive outcome is tested
  * Sad Paths
      Sad Path checks whether the funciton responds appropriately to the exceptions without breaking when Negative Outcome is tested
  * Test Fixtures
      Test fixtures establishes a known initial state before and after each test </br>
      Test fixtures are helpful for many testing situations. such creating mock data object, loading the database with a known dataset. </br>
      Testfixtures operates at three levels of specificity, </br>
          * __Module Level__ </br>
         ``` python
          def setUpModule():             # runs once before any tests
          def tearDownModule():          # runs once after all tests
         ```
          * __TestCase Level__ </br>
          ``` python
           @classmethod
           def setUpClass(cls):       # runs once before test case
           @classmethod
           def tearDownClass(cls):    # runs once after test case
         ```
         
          * __Test Level__ </br>

          ``` python
               def setUpModule():             # runs once before any tests
               def tearDownModule():          # runs once after any tests
          ```
         
