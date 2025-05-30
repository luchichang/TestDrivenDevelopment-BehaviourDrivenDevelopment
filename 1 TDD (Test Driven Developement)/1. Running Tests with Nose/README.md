# Running unit test with Nose ( Python unit testing Framework)

## Description


## Setting up the Runtime Environment

 * Download & Install the Python Package, depending on your OS platform
 
  https://www.python.org/downloads/
 
 * install the PIP python Package manager
   
 * After Installation completed verify everything works fine by running, <br/>
      ``` bash
       python3 --version 
       pip --version
      ``` 
 * if the version number is displayed then the environment is set up

## Steps to Unittest using python builtin Module,

 * after cloning the repository,and navigated to the project path.
 * move to the first project by typing <br/>
     cd "TDD UnitTest Projects"/"1. Running Tests with Nose"/

 * invoke pythons default standard library module __Unittest__ by running
    ``` bash
      python3 -m unittest
    ```  
 * now the unittest module will be running and for every test pass there will be __.__ and for every error __E__

 * for more information about the each test add __-v__ verbose option in the previous command
    ``` bash
     python3 -m unittest -v
    ```
     
 (when viewing the output you may find some redundant function name is also displaying along with the output)
 we can handle this better by using Nose

       Nose is python testing framework used to extent python built in __unittest__ module, making it easier it write and test

## Steps to Unittest using python testing Framework __NOSE__ ,
 * install the Nose in python Package Manager __pip__

    ``` bash
     pip install nose
    ```
* verify nose is installed, by  running
    
    ``` bash
     pip show nose
    ```
(if nose library is installed command will display version, location)

 * now run unitest using nosetest

    
    ``` bash
     nosetests -v
    ```

## for making the better output
 * install pinocchio module for having the colored output, where green indicates the test is passed and red indicates test is failed 

 * install the __pinocchio__  python plugin library 

   ``` bash
     pip install pinocchio
   ``` 
 * once installed verify the download is completed by running 
   ``` bash
     pip show pinocchio
   ``` 
 (if the version and other details are displayed then plugin is installed sucessfully)

 * now run the __nosetest__ along with pinocchio plugin
   
  
   ``` bash
     nosetests --with-spec --spec-color
   ``` 
  (note: in the above command options are represented in kebab case. for more details on these cases do check my linkedin post 
  https://www.linkedin.com/feed/update/urn:li:activity:7246521659031986176/
    ) 

 * after running the nosetest with pinocchio plugin you can observe the better readability in output
 
     Note: In the output, green color indicates that all tests have passed. In case any test fails, the color for that test in the output will be red. Also note that you no longer need the -v because --with-spec already gives verbose output. 

## adding Test coverage along with nosetest
 * the __nosetest__ will run the test for described test cases and the __coverage__ tool will give a report of what are the lines are tested so that we can add test against the uncovered lines of our code
 
 * install __coverage__ tool

    ``` bash
     pip install coverage
   ``` 
 * next call the coverage through nose by adding the __--with-coverage__ parameter 

    ``` bash
     nosetests --with-spec --spec-color --with-coverage
   ```  
 (note: by running this above command you will get a detailed report about the code covered so that you can assure you have written testcases for all the code)

     One useful feature of the coverage tool is that it can report which lines of code are missing coverage. With that information, you know the lines for which you need to add more test cases so that your testing executes those missing lines of code.
 * to get the missing coverage report run the below commadn in the terminal 

  ``` bash
    coverage report -m 
  ``` 

  (note: there will be new column added with missing name which denotes the missed line )

  ## for command simplicity 

  * instead of writing the long command you can just configure the command in __setup.cfg__ file where you paste the following command

   ```
   [nosetests]
   verbosity=2
   with-spec=1
   spec-color=1
   with-coverage=1
   cover-erase=1
   cover-package=triangle
   [coverage:report]
   show_missing = True
   ```

* so that now just by running the __nosetests__ command you will get all the configured options 