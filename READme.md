#  Authentication API

#### Author: [Kiptoo Rotich](https://github.com/kiptoo-rotich)

## Screenshot
### Login
![login](https://user-images.githubusercontent.com/48821300/141445194-76184596-f9bc-4995-95c8-228b266f3dd4.png)


### Register
![Register](https://user-images.githubusercontent.com/48821300/141445253-8ffbf80f-4957-431d-97dd-61dd02ab3322.png)


## Description
This is anauthentication API with register and login endpoints.


## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.9 manage.py runserver`
* Run `http://127.0.0.1:8000/` to find login data.
* Run `http://127.0.0.1:8000/registerAPI` to find register data.

## Login end point
```bash
`https://authapi27.herokuapp.com/`
```
## Register user end point
```bash
`https://authapi27.herokuapp.com/registerAPI`
```

## Getting started

### Prerequisites
* python3.9
* virtual environment
* pip
* postgresql
  

#### Clone the Repo and rename it to suit your needs.
```bash
git clone `https://github.com/kiptoo-rotich/AuthAPI/`
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='gallery'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations news
python3.8 manage.py sqlmigrate news 0001
python3.8 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test projects`
        
## Built With

* [Python3.8](https://docs.python.org/3/)
* Django==3.2.9
* Postgresql 
* Boostrap
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license)