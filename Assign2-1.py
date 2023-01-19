#Generating first_name, last_name and full_name and generating a word leaving every other char in the full_name
first_name= input("Please enter first name : ")
last_name= input("Please enter last name : ")

def full_name(first_name,last_name):
    return first_name +" "+last_name

def string_alternative(full_name):
    new_str = ""
    for index in range(0,len(full_name),2):
                       new_str+=full_name[index]        
    return new_str               


print("User full name : ",full_name(first_name,last_name))

print("Alternate String : ",string_alternative(full_name(first_name,last_name)))
