# Q. Python Age Counting In the Python file, write a program to perform a GET request on
# the route https://coderbyte.com/api/challenges/json/age-counting which contains
# a data key and the value is a string which contains items in the format: key=STRING, age=INTEGER.
# Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value.
# Example
# Input: {"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}
# Output: 2


import requests
import numpy as np
import pandas as pd

# r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
# print(r.status_code)
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.text)
# print(len(r.json()['data']))

URL = 'https://coderbyte.com/api/challenges/json/age-counting'
r = requests.get(url=URL)
data = r.json()['data']

ages = data.split(",', '")
ag = ages[0].split(', ')

ages=[]
for x in range(1, len(ag)+1):
  if x%2 == 1:
    ages.append(ag[x])
# print(ages)
ega=[]
for age in ages:
  ega.append(int(age.split('=')[-1]))

counter = 0
for a in ega:
  if a>=50:
    counter+=1
print(counter)
