# this function is using boolean values

def can_vote(a):
    
    if age>=18:
        return True
    else:
        return False
age  = int(input("enter a one number="))
ans  = can_vote(age)
print(ans)


#  this  return function is using variable
def name(name):
    return name
p = name("arti")
print(p)