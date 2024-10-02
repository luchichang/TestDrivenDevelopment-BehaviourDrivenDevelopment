# Writing Test Assertion for Stack programming

## Description
     Test Assertion is a python built-in function used to assert whether the function return true or false

## Environment Setup 
 * environment setup is discussed detaily in the first project. check it out!
 * once everything is done install the necessary packages for running the __nosetest__ which are in the ___requirements.txt___ file. by running the following command in terminal.

    ```bash
      pip install -r requirements.txt 
    ```  
 (INFO: if you're curious to know what are the packages are gonna be installed. do check it out in the ___requirements.txt___ file)


## Steps

  __WARN__: Before writing any code from the cloned or other projects, you should always check that the test cases are passing. Otherwise, if they fail, you won’t know if you broke the code or if someone or something else broke the code before you started.

 * Ensure you're in the correct directory
    
    ```bash
       cd "TDD UnitTest Projects"/"2. Writing Test Assertions"
    ``` 

 * now run the __nosetests__ command which is configured in the ***setup.cfg*** file. to check that the code runs correctly

    ```bash
      nosetests  
    ```  
 * as configured in setup.cfg file all the passed test are in green color and all the failed test in red color. now if you want to exit from the test at the first failing test case then run,

      ```bash
      nosetests --stop
    ``` 
 * by watching the console output, its clear that the test are not running in the linear order reason is. <br/>

   Nose runs tests in a pseudo-random order. This is to ensure that test cases do not affect the order of execution or depend on it to work.
