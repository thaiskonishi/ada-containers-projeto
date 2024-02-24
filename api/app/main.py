from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/employees")
async def get_employees():
    connection = mysql.connector.connect(
        user='root',
        password='RootPassword',
        host='mysql',
        port='3306',
        database='Company'
    )
    print('DB connected')
    cursor = connection.cursor(dictionary=True)
    cursor.execute('Select * FROM employees')
    employees = cursor.fetchall()
    datas = []
    for employee in employees:
        print(employee)
        data = {
            "first_name": employee["first_name"],
            "last_name": employee["last_name"],
            "email": employee["email"],
            "department": employee["department"]
        }
        datas.append(data)
    connection.close()
    print('DB closed')
    return { 'employees' : datas }

@app.post("/employees")
async def post_employees():

    connection = mysql.connector.connect(
        user='root',
        password='RootPassword',
        host='mysql',
        port='3306',
        database='Company'
    )
    print('DB connected')
    cursor = connection.cursor()
    first_name="Thais"
    last_name="Mal"
    department="IT"
    email="thais.mal@gmail.com"
    command = f'INSERT INTO employees (first_name, last_name, department, email) VALUES ("{first_name}","{last_name}","{department}","{email}")'
    cursor.execute(command)
    connection.commit()
    
    connection.close()
    print('DB closed')
    return { 'employees created!' }

