print("Welcome to TestApplication version 0.1 (Build 2.fbl_Testapplication(orangera1n).211214-1958")
x=int(input("How many days since an incident:"))
if x<0:
  print("Sorry, that is not a number, but it is a poop emoji")
elif x<10:
  print("Your safety is not great")
elif x>10 and x<30:
    print("Your safety is not too bad")
else:
  print("Your safety is good")