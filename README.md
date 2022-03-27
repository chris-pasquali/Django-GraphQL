# Django-GraphQL

Install Pipenv:
  ```
  pip install pipenv
  ```
 Run environment:
  ```
    pipenv shell
  ```
 
 Install all dependencies:
   ```
   pip install -r requirements.tx
   ```
 
 Start Server:
 ```
 python manage.py runserver
 
 http://127.0.0.1:8000/graphql/
 ```
 
 Execute Query:
 ```
 query {
  person {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
 ```
