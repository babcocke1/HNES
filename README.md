## HNES
Repo name subject to change, general python repo for research related stuff
## For Development
# Github
You can clone/push/pull using CLI or using Github Desktop, if you are 
new to git I reccomend using gh desktop

For gh desktop just follow instructions on website
For cli you need to set up a private/public ssh key pair which I can help with
# Editor
I recommend using VSCode as your code editor
You can download VSCode here https://code.visualstudio.com/download 

# Python
You should be able to run Python from the command line, if you are on Windows and get an error that Python can't be found, 

Case 1:
You don't have Python

Solution:
Download Python

Case 2:
You have Python but downloaded through anaconda or something,

Solution:
You can either redownload python or mess with your system path variables
    
Check that it worked:

    $ Python3 --version
# Setting up pip
pip is what we will use to download Python packages
You can think of Python as a glue language. Most Python developers use it to tie together many existing libraries and packages for their projects.
Pure Python is much slower than languages like C++/Java/Rust but many Python packages are written in a faster language under the hood. Therefore if something is very computationally heavy, it is usually worth using a package. I do not see us needing many packages outside of sympy and numpy but we will see where the project goes! 

To get pip and check version:

    $ py -m pip install --upgrade pip
    $ py -m pip --version
# Working with virtualenv
We will keep track of our dependencies using a requirements.txt file at the root of the project directory. I then recommend downloading these
dependencies using virtualenv. You can technically just install them but using a virtualenv is best practice.

Get virtualenv:
    
    $ py -m pip install --user virtualenv

You then need to create a virtualenv at the root of the project dir (same place as requirements.txt). You can pick any name but I use venv
    
    $ py -m venv <name>

To use and check
    
    $ .\env\Scripts\activate
    $ where python
To install dependencies (finally)
    
    $ py -m pip install -r requirements.txt
To add dependencies
    
    $ pip install <dependency>
To update requirements
    
    $ pip freeze > requirements.txt

# About this guide
I tried to be thorough but idk what problems may arise so treat this as a guide but know that if you see some other way online that looks like it would work. Feel free to follow that. This readme is part of our repo which means that anyone can write to it if they wish so feel free to update with anything you found. I wrote this for windows but dont use windows so if my guide is not working please try and troubleshoot or do not hesitate to reach out to me for help! :) 