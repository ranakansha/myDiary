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

1.login page for blog

![Screenshot (245)](https://user-images.githubusercontent.com/51478832/91122518-278acc00-e6b8-11ea-8c90-3d07e675467c.png)


2. signup page for blog

![Screenshot (246)](https://user-images.githubusercontent.com/51478832/91122536-33768e00-e6b8-11ea-97e4-ce62d3919ba9.png)

3.home page of my blog
![Screenshot (247)](https://user-images.githubusercontent.com/51478832/91122545-38d3d880-e6b8-11ea-8c3e-b7e01dba9af9.png)

4.post homepage for my blog

![Screenshot (248)](https://user-images.githubusercontent.com/51478832/91122554-3d988c80-e6b8-11ea-853f-45139dc069ca.png)

5.edit post page.

![Screenshot (249)](https://user-images.githubusercontent.com/51478832/91122556-3f625000-e6b8-11ea-9470-7389430c0439.png)
![Screenshot (250)](https://user-images.githubusercontent.com/51478832/91122568-44bf9a80-e6b8-11ea-85fa-aa217dd9671f.png)
![Screenshot (251)](https://user-images.githubusercontent.com/51478832/91122572-4721f480-e6b8-11ea-9389-395e5c331840.png)
