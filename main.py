n=int(input("bir sayi: "))
b=int(input("bir sayi: "))

rec=[]
for i in range(n):
  if (i+1)%2==0:
    rec.append(2**(i+1)+1)
  else:
    rec.append(3**(i+1)+1)
print(rec)

sum=0
n2=n
for i in rec:
  n2-=1
  sum+=i**n2


t=range(1,10001)
for i in t:
  if i*sum>b:
    print(i,sum)
    break
upper=max(t)
lower=min(t)
x= (upper+lower)/2

while True:
  if sum*x>b:
    upper=sum*x
    x= (upper+lower)/2
    print(x)
  elif sum*x<b:
    lower=sum*x
    x= (upper+lower)/2
    print(x)
  if abs(upper-lower)<=10:
    re=sum*x
    print(x)
    break
print(re)
