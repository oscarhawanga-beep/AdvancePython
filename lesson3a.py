# conditional statements
# if .....else statement

number = int(input("Enter your number: "))
if number >0:
    print("The number is positive")
else:
    print("The number is negative")


print("===================================")
# create a dictionary with student's details like name, email, admissionNo and password. Prompt the student to enter the password for him to be able to access the student portal. By use of an if statement, check whether the entered password is correct to navigate him to the portal otherwise if the password entered is incorrect, pass a message to block the student from accessing the student portal.
student_portal ={
    "name":"Oscar",
    "email":"oscarhawanga@gmial.com",
    "addmission_number": "AVDSA1234",
    "password":"1234",
}
password = input("Enter your password to access the student portal: ")
if password == student_portal["password"]:
    print("Access granted to the student portal")
else:
    print("Access denied. Incorrect password.")