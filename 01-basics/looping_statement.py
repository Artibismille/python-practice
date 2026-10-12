# Find the sum of numbers from 1 to n.

n = int(input())
total = 0
for i in range(1,n + 1):
      total = i+total
      print(i)
      
print("total=", total)

  
# Print the multiplication table of a number.

n = int(input())
for i in range(1,11):
    print(i*n)
  