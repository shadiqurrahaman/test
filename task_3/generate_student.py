import json
import random
from requests.api import request
import schedule

from random import randint
from faker import Faker
import requests
fake = Faker()

# generate random studen


def getstudet():
    student = {}
    student["name"] = fake.name()
    student["age"] = randint(20,50)
    student["gender"] = random.choice(["Male","Female"])
    student["address"] = fake.address()
    student["contact"] = fake.phone_number()
    return student

def insert_studet():
    student = getstudet()
    url = 'http://127.0.0.1:2048/students/_doc?pretty'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, headers=headers, json=student)
    print(response.json())

def check_elasticserch():
    response = requests.get('http://127.0.0.1:2048?pretty')
    return response

def check_index():
    response = requests.get('http://127.0.0.1:2048/students?pretty')
    return response 
   
def create_index():
    response = requests.put('http://127.0.0.1:2048/students?pretty')
    return response

def create_index_schema():
    url = 'http://127.0.0.1:2048/students/_mapping?pretty'
    header = {'content-type': 'application/json'}
    data = {
        "properties": {
            "name":     { "type": "text"},
            "age":      { "type": "integer"},
            "gender":   { "type": "text"},
            "address":  { "type": "text"},
            "contact":  { "type": "text"}
        }
    }
    response = requests.put(url, headers=header, json=data)
    return response
def check_schema():
    response = requests.get("http://127.0.0.1:2048/students/_mapping?pretty")
    return response

    
# format the dictonary
# schedule.every(10).seconds.do(hello)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
    
