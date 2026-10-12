# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Example of a dictionary
phonebook = {
    "Oscar": "0814547780",
    "John": "987-654-3210",
    "Tina": "0812957439"
}
print ("My phonebook is: ", phonebook)

# To access the values of a dictionary we use the key name inside square brackets:
print("Tina's phone number is: ", phonebook["Tina"])
print("===================================")
player = {
    "name":"Lionel Messi",
    "age":39,
    "teams": ["Barcelona", "PSG", "Inter Miami","Argentina"],
    "more":{
        "Children":3,
        "networth":4.5,
        "citizenship":("Us","Spain","Argentina")
    }
}
# Task : print out "Argentina".
student_profile ={
    "name":"oscar",
    "age":35,
    "subject":["python","Database","networking"],
    "details":{
        "phone number":"0814547780",
        "Location":"Namibia",
        "marks":{
            "python":85,
            "Database":78,
            "Networking":90}}}

# 1.2 print student name
#1.3 print "Database" from the list
#1.4 print student location
#1.5 print student's python marks
#1.6 print student networking marks
print(student_profile["name"])
print(student_profile["subject"][1])
print(student_profile["details"]["Location"])
print(student_profile["details"]["marks"]["python"])
print(student_profile["details"]["marks"]["Networking"])

