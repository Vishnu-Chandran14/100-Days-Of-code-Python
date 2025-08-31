# 100-Days-Of-code-Python
--Documenatation of Python Course-Learning 100 days of code

print("Welcome to the tip calculator!\n")

Bill_Amount = float(input("What was the total bill?\n"))

Tips = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
Tips_Amount = float(Tips*0.01)
People = int(input("How many people to split the bill?\n"))
Split_Amount = round(((Bill_Amount + (Bill_Amount*Tips_Amount))/ People),2)
print(f"Each person should pay: ${Split_Amount}.")
