'''
функции


range(), print(), input(), max() min() map()


def имя_функции([gараметры]):
    инструкции
'''

def hello():
    print('hello')


hello()
hello()
hello()


def sr(a=0,b=0,c=0):
    print((a + b + c) / 3) #(5+0+0)/3

sr(1,2,3)
sr(5,6,7)
sr()
sr(5)
sr(5,6)


#5!=1*2*3*4*5=120
#4!=1*2*3*4=

'''
n=5
1 2 3 4 5
range(1, n+1)
'''





#анонимные ф-ции
d = lambda a,b: a + b
print(d(1,2))

filter = lambda n: (n % 5 == 0 and n % 4 != 0) or (n % 6 == 0)
filter_2 = lambda n: True if n % 9 == 0 else False

for i in range(1000):
    if filter(i) and filter_2(i):
        print(i)


#функции декораторы

def decorator(func):
    def wrapper(*args, **kwargs):
        print('*******')
        res = func(*args, **kwargs)
        print('*******')
        return res
    return wrapper


@decorator
def s():
    print('hello')

s()

@decorator
def factorial(n): #N=5
    '''
        n=5
        range(1, 6) = 1 2 3 4 5
    '''
    a = 1
    for i in range (1,n+1): #i=1  i=2 i=3 i=4 i=5
        a = a * i #a=1*1=1  a=1*2=2 a=2*3=6 a=24  a=120
    return a

print(factorial(5))
print(factorial(4))

'''
def
lambda
декораторы
'''