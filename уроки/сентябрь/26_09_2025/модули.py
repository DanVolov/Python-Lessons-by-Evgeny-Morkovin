'''
math
random
datetime
time
os
json
sqlite3
tkinter

pandas
numpy

django
fastapi
flask

pyTelegramBotAPI
customtkinter
pygame

'''
import datetime
import random
print(random.randint(1, 100))

a = [1,2,3,4,5]
print(a)
random.shuffle(a)
print(a)
print(random.choice(a))

d = datetime.datetime.now()
print(d.strftime("%H:%M %d.%m.%Y"))
print(d.minute)
print(d.second)
print(d.microsecond)

time = datetime.time(10,0)
print(time)
