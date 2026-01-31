n = int(input())
sum = 0
for i in range(n):
    x = int(input())
    if x % 5 == 3:
        sum += x
print(sum)