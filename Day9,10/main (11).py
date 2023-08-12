n = input()
n = n[::-1]
print(n)



sum = 0

for i in range(1, len(n) + 1):
    a=n[i - 1]
    sum += i ** int(a)

print(sum)