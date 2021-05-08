import random
f_name=input("who is going to buy today meal: ") #enter name after each name use ','
s_name=f_name.split(",")
random=random.randint(0,len(s_name))
print(random)
p_name=s_name[random]
print(p_name + " is going to buy today meal")
