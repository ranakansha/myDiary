# myDiary


In this tutorial, we’ll build a Blog application with Django that allows users to create, edit, and delete posts from scratch. The homepage will list all blog posts, and there will be a dedicated detail page for each individual post. Django is capable of making more advanced stuff but making a blog is an excellent first step to get a good grasp over the framework. The purpose of this chapter is to get a general idea about the working of Django.

# Pre-Requirements:


1.python install in your system and path set in envioment variable. 
2.Install and activate virtual enviorment.
3.Django3 install in your system.

## Creating And Activating A Virtual Environment


While building python projects, it’s a good practice to work in virtual environments to keep your project, and it’s dependency isolated on your machine. There is an entire article on the importance of virtual environments Check it out here: How To A Create Virtual Environment for Python

### Windows Users


cd Desktop
virtualenv django
cd django
Scripts\activate.bat

### Mac and Unix Users


mkdir django
cd django
python3 -m venv django
source django/bin/activate


Now you should see (django) prefixed in your terminal, which indicates that the virtual environment is successfully activated, if not then go through the guide again.

##  Installing Django In The Virtual Environment


If you have already installed Django, you can skip this section and jump straight to the Setting up the project section. To Install Django on your virtual environment run the below command

pip install Django
This will install the latest version of Django in our virtual environment. To know more about Django installation read: How To Install Django

Note – You must install a version of Django greater than 2.0

## Setting Up The Project


1.Django 3 install and make sure enviorment is activated.
2.clone the project from github into django setup.
3.open cmd on project location.
4.run command : ###  python manage.py runserver.


Here is a sneak peek of what i did.
