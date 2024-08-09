# print("hello")

# a = 1
# b = 2 

# # Arthimetic operators
# print(a+b)
# print(a-b)
# print(a/b)
# print(a%b)


# # comparison operators

# a=2
# b=3

# # print(a=b)


# print(a==b) # True



# # # logical operators

# # a = 2 
# # b = 5

# # print(a and b)
# # print(a or b)


# # string manipulation

# name= "apple"
# # email = "apple@gmail.com"

# print(name.upper())


# name = "Ram is human"
# split_data = name.split("@")
# print(split_data[0])  # ['Ram', 'is', 'human']




# condition

# age=18
# if age>10:
#     print("you are adult")



#wap which take input as age and print they are old or not 

# age=int(input("enter your age:"))

# if age<=18:
#     print("young")
# elif age<=50:
#     print("adult")
# else:
#     print("old")





# name= input("enter your name :")
# age = input("Enter you age: ")

# print(name , age)
# print(f"your name is {name} and age is {age}")





#capitalize string


# name = "arun"



# print(name.capitalize())  # Arun



# print(name.upper())  # ARUN



# print(name.lower())  # arun





# print(name.title())  # Arun




# print(name.swapcase())  # aRuN




# print(name.replace("arun","bikram"))  # Output: bikram


# name = ["My ", "name ",  "is", "Arun"]
# sentence = " ".join(name)
# print(sentence)


# name = "my name is arun sunam"
# print(name.split())  




# name = "arun sunam"
# print(name.find("hello"))  # Output: 6
# print(name.find("sunam"))  # Output: -1



#replace
# sentence = " i love veg food"
# print(sentence)
# changed_sentence=sentence.replace("veg", "non-veg")
# print(changed_sentence)

#split

# user_email = "arunsunam@gmail.com"
# split_data_first = user_email.split('@')
# split_data_second = split_data_first[1]
# print(split_data_second.split('.'))


#strip

# data = "my name is arun"
# data_changed=data.upper()
# print(data_changed)



#type

# sentence = input("enter your sentence")
# print(type(sentence)) 
# num = input("Enter your num")
# print(type(num)) 
# print(f"your rollno is {num}")




#change type

# num = "45"
# print(type(num))
# change_value = int(num)
# print(type(change_value))




#condition

# age = int(input("type your age: "))



# if age<=18:
#     print("young")
# elif age<=50:
#     print("adult")
# else:
#     print("old")





# data="i am veg"
# if "veg" in data:
#     print("you can eat veg")
# else:
#     print("you can't eat veg")



#email validation

# email="arun@gmail.com"

# if '@'  not in email:
#     print("invalid email")
# else:
#     print("valid email")


# email="arungmail.com"

# if '@'   in email and '.com'  in email:
#     print("valid email")
# else:
#     print("invalid email")




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





