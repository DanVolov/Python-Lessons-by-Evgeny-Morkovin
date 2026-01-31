import os
#os.mkdir('Новая папка')
#os.makedirs('1/2/3/4',exist_ok=True)
#os.rmdir('Новая папка')
#os.rmdir('1/2/3/4')
#os.rmdir('1/2/3')
#os.rmdir('1/2')
#os.rmdir('1')

print(os.path.exists('time1r.py'))
if not os.path.exists('2'):
    os.mkdir('2')

print(os.getcwd())
print(os.listdir(os.getcwd()))

for i in range(1, 101): #1...100
    if os.path.exists(f'Новая папка {i}'):
        #os.mkdir(f'Новая папка {i}')
        for j in range(1, 6): #1...5
            #with open(f'Новая папка {i}/{j}.py', 'w') as f:
                #f.write('print("Hello World!")')
            os.unlink(f'Новая папка {i}/{j}.py')
        os.rmdir(f'Новая папка {i}')
