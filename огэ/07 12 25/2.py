n = int(input())
sum = 0
for i in range(n):
    x = int(input())
    if x % 9 == 5:
        sum += x
print(sum)