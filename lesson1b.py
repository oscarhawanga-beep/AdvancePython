mylist =["Russia","Ukraine","UK","France","Belarus","italy","Germany"]
print(mylist)
# pop()  removes the item based on its index.
mylist.pop(3)
print(mylist)
# remove() removes the item based on its value.
mylist.remove("Belarus")
print(mylist)

# Create  two list with 3 iems each and then join the to list to make one big list.
bricks=["Russia","South Africa","Brazil"]
nato=["USA","UK","France"]
print(bricks + nato)

#tuple : its an immutable type of a list meaning: its unchangeable
presidents=("Uhuru","Ruto","Kenyatta","Mnagangwa","Ramaphosa")
print(presidents)
print(type(presidents))

# Multiple list print out My Name
list2 = [["James", "Tony","Bernard", "Jeremiah"], ["Joyce", "Mary", "Oscar", "Martha"], ["Brian", "Edward","Joseph", "Linet"]]
print(list2.index(["Oscar"]))
print(list2[1][2])
