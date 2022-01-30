# Back-end Contacts

> Flask API to manage contacts.

## 🧬 Built with

* Python 3.9
* Flask
* PostgreSQL

## 💻 Requirements

Before you start, make sure you have the following resources:

* Python 3.9
* PostgreSQL
* A virtual environment to run the application
* A PostgreSQL database

## 🚀 Setting up

Run the following commands:

- Creating virtual environment
```
python3.9 -m venv env
```

- Create a .env file with your settings, e.g.:
```
FLASK_ENV=development
DATABASE_URL="postgresql://user:pass@localhost/contacts"
```

- Migration commands:
```
flask db init
flask db migrate
flask db upgrade
```

## 🗃 Initializing

To run the API, run the command:

```
flask run
```
