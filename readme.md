[![Build Status](https://travis-ci.com/Kyeza/RentalMangementSystem.svg?branch=ft-auth)](https://travis-ci.com/Kyeza/RentalMangementSystem)

# Rental Management System

The Rental Management System supports and optimises all business processes in the property/House rental industry. The system is a web application, which means that the system is easy to update and maintain without distributing and installing new software.

## Getting Started

```
Clone project from github
    $ git clone https://github.com/Kyeza/RentalMangementSystem.git
```

### Prerequisites

What things you need to install the software and how to install them

```
1. Ensure system has Python 3.x installed including pip, which is a package manageer for python

2. With pip installed, install virtualenv 
    $ pip install vitualenv
    
    if using windows install virtualenvwrapper-win
    $ pip install virtualenvwrapper-win
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
1. Using the terminal navigate to project directory, and create a virtual enviroment
    $ mkvirtualenv envname
    $ workon envname
    
2. Install project dependency from the requirements.txt file
    $ pip install -r requirements.txt
    
3. Run migrations
    $ python manage.py makemigrations
    $ python manage.py migrate
    
4. Create super user to access the system
    $ python manage.py createsupersuser (Follow prompt to enter Username, Email, Password and Confirm Password)
    
5. run development server to access the system
    $ python manage.py runserver
```

Output

```
Enter url in browser
    $ localhost:port/rental_app e.g: localhost:8000
```


## Running the tests

Python unittest

### Break down into end to end tests

```
Testing for Api response status
Testing for system functionality forexample; user creation, property booking etc

To run test run the following command:
    $ python manage.py test
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Python](https://www.python.org/) - Language of development
* [Pip](https://pypi.org/project/pip/) - Dependency Management

## Contributing
Not yet available! <br>
Please read [CONTRIBUTING.md](#) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
Not yet available! <br>
We use [Git](https://git-scm.com/) for versioning. For the versions available, see the [tags on this repository](#). 

## Authors

* **Kyeza Arnold** - *Initial work* - [RentalMangementSystem](https://github.com/Kyeza/RentalMangementSystem)

See also the list of [contributors](#) who participated in this project.

## License

© 2019. All rights reserved.

## Acknowledgments

* Hat tip to google and stackoverflow :)
* Inspiration
* etc
