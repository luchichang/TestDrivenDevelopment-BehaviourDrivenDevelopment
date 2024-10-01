# Running unit test with Nose ( Python unit testing Framework)

## Description


## Setting up the Runtime Environment

 * Download & Install the Python Package, depending on your OS platform
 
  https://www.python.org/downloads/
 
 * install the PIP python Package manager
   
 * After Installation completed verify everything works fine by running,
    python3 --version 
    pip --version 
 * if the version number is displayed then the environment is set up

## Steps,

 * after cloning the repository,and navigated to the project path.
 * move to the first project by typing
     cd "TDD UnitTest Projects"/"1. Running Tests with Nose"/

 * invoke pythons default standard library module __Unittest__ by running

     python3 -m unittest  
 * now the unittest module will be running and for every test pass there will be __.__ and for every error __E__

 * for more information about the each test add __-v__ verbose option in the previous command

     python3 -m unittest -v 
 (when viewing the output you may find some redundant function name is also displaying along with the output)