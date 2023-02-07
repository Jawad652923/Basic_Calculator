#basic calculator
num_1 = float(input("Enter your 1st number: "))
num_2 = float(input("Enter your 2nd number: "))
print("what operation you want to do.")
print("1:Addition,2:subtraction,3:multiplication,4: division")
method_to_use = float(input("select operator :"))
if method_to_use == 1:
    print(num_1 + num_2)
elif method_to_use == 2:
    print(num_1 - num_2)
elif method_to_use == 3:
    print(num_1 * num_2)
elif method_to_use == 4:
    print(num_1 / num_2)
else:
    print("sorry we dont do any further operation thanks for using this calculator")
print("Thanks for using this calculator")