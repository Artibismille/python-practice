n = int(input("enter one number="))
m = int(input("enter second number ="))
p = int(input("enter third number ="))
# Check whether a number is positive, negative, or zero.
if n>0:
   print("positive")
elif n<0:
    print("negative")
else:
    print("zero")
    
# Check whether a number is even or odd.
if n%2==0:
    print("even")
else:
    print("odd")

#Find the greater of two numbers.
if n>m:
    print("first number is large")
elif n<m:
    print("second is large")
else:
    print("both are equal")
    
#Find the greatest of three numbers.
if n>=m and n>=p:
    print(f"{n} is large")
elif m>=n and m>=p:
    print(f"{m} is large")
elif p>=n and p>=m:
    print(f"{p} is large")

# Check whether a number is divisible by 5
    
if n%5==0:
    print(f"{n} is divisible by 5")
else:
    print("not divisible ")
    