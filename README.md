# gpa

# Introduction

The goal of this project is to build a GPA ( General Purpose Accounting or GPA System)

<!--
### Main features

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in as demo

* Procfile for easy deployments

* Separated requirements files

* SQLite by default if no env variable is set -->

# Usage

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:jolouie7/gpa.git
    $ cd gpa

Activate the virtualenv for your project.

Install project dependencies:

    $ pip install -r requirements/local.txt

Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver

> To Create a user type command "python manage.py createsuperuser"

Future:

- Change DB to postgres
