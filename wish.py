time_input = float(input("Enter the time now:"))
time = int(time_input)

if (time < 12.00):
    print("Good Morning")
elif(time < 18.00):
    print("Good Afternoon")
elif(time < 21.00):
    print("Good Evening")
elif(time < 24.00):
    print("Good Night")
else:
    print("Time does not exist")
    
