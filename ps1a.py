n, B = list(map(int, input().strip().split()))
T = 0

# your code here
rec=[]

for i in range(n):
  if (i+1)%2==0:
    rec.append(2**(i+1)+1)
  else:
    rec.append(3**(i+1)+1)

sum=0
n2=n
for i in rec:
  n2-=1
  sum+=i**n2

step=0
t=range(1,10001)
for i in t:
  step+=1
  if i*sum>B:
    break
T=i*sum
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)