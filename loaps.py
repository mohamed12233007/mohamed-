# fact(1) = 1
# fact(2) = 2*1

# fact(100) = 100*99*[98*....*1]

# take input from user
inp = int(input("please enter a number"))

fact = 1
for i in range(1,inp+1):
     print("fact old", fact)
     fact = fact * i
     print("fact new", fact)

# inp = 5
# 1 , fact(old) = 1, fact(new) = 1*1
# 2 , fact(old) = 1, fact(new) = 1*2
# 3 , fact(old) = 2, fact(new) = 2*34 , fact(old) = 6, fact(new) = 6*4


# take an int input
# print it till 0

# for i in range(1,inp):
#     spaces = inp//2 - i + 2
#     print(" "*spaces, end="")
#     print ("*"   *i)  








# num=int(input9enter the num)

# if num%3:
#     print ("fizz")
# elif num/5:
#     print ("buzz")
# elif num/3 and num/5:
#     print("fizz buzz")
# else:
#     print (num)












