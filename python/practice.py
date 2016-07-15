
#a = 25
#b = 36
#dog = "ralph"
#cat = "whiskers"

#print a * b
#print dog + " hates " + cat

#first = "BARACK"
#last = "OBAMA"
#age = 53

#print ("The president is: " + first.capitalize() + " " +
#    last.lower())

#name = "Bill"
#age = 16

#print "Name: " + name + " Age: " + str(age)
#age = str(age)
#print type(age)

#left_number = raw_input("Enter a number: ")
#right_number = raw_input("Enter a number: ")

#if (not left_number.isdigit()) or (not right_number.isdigit()):
    #print "Bad input! please enter an integer"
    #exit(1)
#left = int(left_number)
#right = int(right_number)
#total = left + right

#print "The sum is: " + str(total)

#truefact = 5
#myguess = int(raw_input("Enter a number between 1 and 10: "))
# if myguess == truefact:
#    print "You are correct"
#else:
#    print "Try again!"





#right_number = int(raw_input("Enter a number: "))

#print "The sum is: " + str(int(left_number) + int(right_number))

#first = raw_input("First name: ")
#last = raw_input("Last name: ")

#print "Your full name is: " + first + " " + last

#phone_number =  raw_input("What is your phone number? ")

#if (len(phone_number) !=13):
#    print "Bad format, wrong length."
#    exit(1)

#if (phone_number[0] != "(" or phone_number[4] != ')'):
#    print "Bad format, area code not encased in parenthesis"
#    exit(1)
#if (not phone_number[1:4].isdigit()):
#    print "Bad fomrat, area code is not digits."
#    exit(1)
#if (not phone_number[8] != "-"):
#    print "No Dash."
#    exit(1)
#if (not phone_number[5:8].isdigit()) or (not phone_number[9:].isdigit()):
#    print "Bad digits."
#    exit(1)
#print "Your phone number is valid."
#for count in range(1, 1 0):
#    print count
#count = 1
#while count < 10:
#    print count
#    count = count + 1
#for count in range(2, 10, 2):
#    print count

#count = 1
#while count <=  10 :
    #print count
    #count += 1
#else:
#    print "count is " + str(count)
#students = ["gaby", "john", "larry", "sergey", "jose"]
#/if "sergey" not in students:
#//    print "where is Sergy"
#//else:
 #  print "welcome Sergey"
#
#for student in students[0::2]:
#    print "Student: " + student

#numbers = [2, 52, 19, 46, 1000]
#i = numbers()
#while i < 5
#    numbers[i] + 10
#    numbers[i] / 2
#    print numbers[i]
#    i + 1
#else:
#    print "All done!"
#    exit(1)
##    one = "hello"
#    two = "world"
#    three = one + two

#fruit =raw_input("What is your favorite fruit?")
#if fruit == "apples":
#    print "Hey, I like apples too."

#making place holders

#age = int(raw_input("How old are you? "))
#years = 10
#print "You will be " + str(int(age) + 10) + " in 10 years."

#print "You will be {param_1} in {param_2} years.".format(param_1=age + years,
#pararm_2 = years)


fave= raw_input("What\'s you favorite food? ")
fave=fave.upper()
vowels = ["A", "E", "I", "O", "U"]
for c in vowels:
    fave = fave.replace(c, c * 3)
print fave
