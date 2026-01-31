'''
списки list []
кортеж tuple ()
словари dict {}
множества set {}
'''

numbers = [6, 9, 3, 41, 5, 6, 7, 8, 9, 10]
#          0  1  2   3
#                                  -2   -1
print(numbers[3])
print(numbers[-1])

numbers[0] = 10
print(numbers)
#функции
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

#методы
numbers.append(10)
print(numbers)
numbers.extend(['user1', 'user2', 'user3'])
print(numbers)
numbers.remove('user1')
print(numbers)
numbers.pop()
print(numbers)
print(numbers.count(10))
#numbers.clear()
#print(numbers)



a = [1,2,3]
b = a.copy()
b[0] = 4
print(a)

a.insert(1, 5) #[1,5,2,3]
print(a)
a.reverse()
print(a)
a.sort(reverse=True)
print(a)


#кортеж
s = (1,2,3,4,5,6,7,8,9,10)
#s[0] = 1
h = (1,)
print(type(h))
a1 = (1,2,3,4,5)
a,b,c,d,e = a1
print(e)

x1,y1,z1 = [1,2,6]
print(x1,y1)


n = (1,2,3,4)
#n[4] = 5
n = list(n)
n[3] = 5
n = tuple(n)
print(n)



def ss():
    h = tuple(range(1,10))
    return h

print(ss())

print(list(range(1,10)))


#dict
a = [1,2]
b = {'a':1,'b':2}
print(b['b'])
user = {'login': 'user1', 'password': '1234', 'age': 33}
user_ = ['user1', '1234', 33]

u = {}
u['login'] = 'user2'
print(u)
u['login'] = 'user3'
print(len(u))
#print(u['password'])
print(u.get('login', 'error'))


users = {'login': 'user1', 'password': '', 'age': 33}
users.pop('login')
print(users)
print(users.keys())
print(users.values())

