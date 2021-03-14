n, B = list(map(int, input().strip().split()))
T = 0

# your code here
rec = []

for i in range(n):
    if (i + 1) % 2 == 0:
        rec.append(2**(i + 1) + 1)
    else:
        rec.append(3**(i + 1) + 1)

sum = 0
n2 = n
for i in rec:
    n2 -= 1
    sum += i**n2

t = range(1, 10001)
upper = max(t)
lower = min(t)
x = round((upper + lower) / 2)
step = 0
while True:
    step += 1
    if sum * x > B:
        upper = x
        x = round((upper + lower) / 2)
    elif sum * x < B:
        lower = x
        x = round((upper + lower) / 2)
    if abs(upper - lower) <= 4:
        re = sum * lower
        while (lower * sum - B) < 0:
            lower += 1
            re = sum * lower
        break
T = lower
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)
