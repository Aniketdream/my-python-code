x=int(input("enter a no"))
for i in range(2,x):
    if x%i==0:
       print("not prime")
       break
else:
    print("prime")
