# Python - Flask REST API

Flask, 
flask-smorest and 
OpenAPI documentation (formerly known as Swagger) for the API.



**About flask-smorest:** (formerly known as flask-rest-api) Flask/Marshmallow-based REST API framework  
https://flask-smorest.readthedocs.io/en/latest/

### How to Install

1. ``python -m venv .env`` 

2. ``.env\Scripts\activate``

3. optional step, update pip: ``.env\Scripts\python.exe -m pip install --upgrade pip``

4. ``pip install -r requirements.txt``


### OpenAPI docs:  
http://127.0.0.1:5000/docs

OpenAPI redoc:   
http://127.0.0.1:5000/redoc


### TODO API  

**GET**  
``/todo/tasks``  
parameters:  
order_by -> created or task  
order -> asc, desc   
http://127.0.0.1:5000/todo/tasks?order_by=created&order=asc  
http://127.0.0.1:5000/todo/tasks?order_by=task&order=asc


**POST**  
``/todo/task``  
**GET**  
``/todo/tasks/{task_id}``  
**PUT**  
``/todo/tasks/{task_id}``  
**DELETE**   
``/todo/tasks/{task_id}``

