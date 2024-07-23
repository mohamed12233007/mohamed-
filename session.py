def add(x,y):
   # print(x+y)
    return x+y

z=add(1,2)

print (z)
def subtract(x,y):
    #print(x-y)
    return x-y

a=subtract(2,2)
print(a)

def multiply(x,y):
    # print (x*y)
    return x*y
b=multiply(3,3)
print(b)


#WORKSHOP2

NAMES=["mohamed","hakem","omar"]
NUMS=[5,8,1]
def add (name,number) :
    NAMES.append(name)
    NUMS.append(number)
name="ali"
number=10
add(name,number)
print(NAMES)
print(NUMS)
def veiw_all_contact(name,numbers):
    print (NAMES)
    print (NUMS)
def remove(name,number):
    NAMES.remove (name)
    NUMS.remove (number)
remove(name,number)
print(NAMES)
print(NUMS)

    













