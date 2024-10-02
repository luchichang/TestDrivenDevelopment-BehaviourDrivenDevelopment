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
   
  (note: here options are represented in kebab case. for more details on these cases do check my linkedin post 
  https://www.linkedin.com/feed/update/urn:li:activity:7246521659031986176/
    ) 
   ``` bash
     nosetests --with-spec --spec-color
   ``` 