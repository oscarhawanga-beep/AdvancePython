def greeting(name):
    print("Hello",name, "How have you been?")

greeting("John")
greeting(" Mary")

# Create a function that accepts parameters that is able to calculate the simple interest gained after a person inversted 75000 for 5 years and the rate was 6.5%. Formulae = si = (principal * rate * time) /100

def simple_interest(principal,rate,time):
    interest = (principal*rate*time)/100
    print("The interest gained is",interest)

simple_interest(2000,0.5,5)
