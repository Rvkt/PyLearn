# -*- coding: utf-8 -*-
"""PrBasics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nCKjep5NMGUfS94q-9Jgsk0s3hBFj-34

Reverse string
"""

def rev(x):
  return x[::-1]


string = input("Enter String: ")
gnirts = rev(string)
print(f'Reverse of {string} is {gnirts}.')

"""Python Iterators"""

# Tuple iteration
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Tuple iteration with for loop

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# String iteration

mystr = "red"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))

# String iteration with for loop
mystr1 = "string"

for x in mystr1:
  print(x)

# Create and stop an itertaion

month = []

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 12:
      x = self.a
      self.a += 1
      return str(x).zfill(2)
    else:
      raise StopIteration

# myclass = MyNumbers()
myiter = iter(MyNumbers())

for x in myiter:
  month.append(x)

print(month)

from datetime import date, datetime
now = datetime.now()
month = (now.strftime('%m').zfill(2))
print(month)

import calendar
from datetime import date, datetime

now = datetime.now()
year = now.strftime('%Y')
month_long = []

for i in range(1, 13):
    month_long.append(calendar.month_name[i]) # month_name is an array
for i in month_long:
    print(f'{year}{i[0:3].upper()}')

import calendar
from datetime import date, datetime

now = datetime.now()
year = now.strftime('%Y')
month_short = calendar.month_abbr[1:]

for i in month_short:
    print(f'{year}{i.upper()}')

from datetime import datetime
import calendar

now = datetime.now()
yr = now.strftime('%Y')
month = []
month2 = calendar.month_abbr[1:]
yearmonth = []
yearmonth2 = []

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 12:
      x = self.a
      self.a += 1
      return str(x).zfill(2)
    else:
      raise StopIteration
      
for x in iter(MyNumbers()):
    month.append(x)
for i in month:
    yearmonth.append(f'{yr}{i}')
for i in month2:
  yearmonth2.append(f'{yr}{i.upper()}')


for i in iter(yearmonth):
    print(i)
print(' ')
for i in iter(yearmonth2):
    print(i)