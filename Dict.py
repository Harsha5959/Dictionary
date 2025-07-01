# Create a dictionary from two lists:

keys = ['id', 'name', 'age']
values = [101, 'John', 25]
a=dict(zip(keys,values))    #Using built in functions
print(a)


keys = ['id', 'name', 'age']
values = [101, 'John', 25]
a={}
for i in range(len(keys)):
    a[keys[i]]=values[i]
print(a)


# Create a dictionary to store student name and age.

Student={"Name":"Harsha","Age":21}
print(Student)


# Create an empty dictionary and add key-value pairs one by one.

a={}
a.update({"Name":"Harsha"})
a["Age"]=21
print(a)


l = []
for i in range(2):
    temp = {}
    temp['name'] = input('enter the name   ')
    temp['pin']  = input("enter the pin   ")
    temp['city']  = input('enter the city  ')
    l.append(temp)
print(l) 


# Get the value of key "salary" from this dictionary:

employee = {'name': 'John', 'age': 30, 'salary': 50000}
print(employee["salary"])
print(employee.get("salary"))

# Remove the last inserted key-value pair from the dictionary using an appropriate method

employee = {'name': 'John', 'age': 30, 'salary': 50000}
employee.popitem()
print(employee)


# Define packing and unpacking in Python. Also, provide one example for both packing and unpacking.

student=("Harsha",21,"AIML")
print(student)

# Unpacking

student=("Harsha",21,"AIML")
a,b,c=student
print(a)
print(b)
print(c)
