#wap to take user input email and validate wether it is correct or not.
#wap to take user input mark percentage and find their division.



email = input("Enter your email:")

if '@' in email and '.com' in email:
    print("the email is correct ")
else:
    print("the email is incorrect ")




mark = int(input("Enter your mark:"))

if mark<40:
    print("Fail")
elif mark>=40 and mark<=49:
    print("Pass")
elif mark>=50 and mark<=59:
    print("Third Division")
elif mark>=60 and mark<=69:
    print("Second Division")
elif mark>=70 and mark<=79:
    print("First Division")
elif mark>=80 and mark<=89:
    print("Distinction")
else:
    print("A Grade")                    





