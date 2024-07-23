

# degree=int(input("what is your degree"))
# if degree>100:
#     print("invalid degree")
# elif degree>=90 :
#     print ("A")
# elif degree>=80:
#     print ("B")
# elif degree>=70:
#     print ("c")
# elif degree>=60:
#     print ("D")
# elif degree<=59:
#     print("F")d
# num1=int(input("what is the first number"))
# num2=int(input("what is the second number"))   
# operator=(input("Entar an operator (+  -  *  /  %)" ))
# if operator== "+":
#     print(num1+num2)
# elif operator=="-":
#     print(num1-num2)
# elif operator=="*":
#     print(num1*num2)
# elif operator=="/":
#     print(num1/num2)
# elif operator=="%":
#     print(num1%num2)
# age=int(input("Enter your age"))
# income=int(input("Enter  your income"))
# employment=(input("Are you an employee"))
# creditscore=(input("Enter  your credit score"))
# Additionalcriteria=(input("Do you have any outstanding loans"))
# loan=int(input("how much do you want the loan"))
# reason=""
# if age>18 and income>(loan/12) and employment==("yes")and Additionalcriteria==("yes") and (loan/12)<income:
#     print("u can make a loan")
# else:
#     print("u cant make a loan")
# if age<18:
#     print(reason+"you need to be 18 first")
# if income<(loan/12):
#     print(reason+"your income is less than the required")
# if employment==("no"):
#     print(reason+"u need to have a job first")
purchaseamount=int(input("Enter the total of purchase amount"))
years=int(input("how many years "))
complaints=int(input("how many complaints have you filed "))
purchase=int(input("how many purchases"))
bonus=""
discount1=(complaints*2)/100
if years>10:
    bonus=0.1
if years>=6 and years<=10:
    bonus=0.08
if years<6:
    bonus=0.05
if purchase>=20:
    discount=(1.05*bonus)
else:
    discount=0


newdiscount=bonus-discount1
check_negative=bonus+discount-discount1
if check_negative<0:
            newdiscount=discount  
newdiscount=int(newdiscount*100)
print("the discount  :"+str(newdiscount)+"%")
newamount=(1-newdiscount/100)*purchaseamount
print("the net purshace is : {}".format(newamount))
