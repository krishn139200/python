                    # love chack game
def check(n,string):
    c=0
    re=0
    for _ in range(len(string)):
        if string[c]==n:
            re+=1
        c+=1
    return re
first_name=input("enter boy name: ")
seconand_name=input("enter girl name: ")
compair = first_name+seconand_name
lowercase=compair.lower()
word=["t","r","u","e","l","o","v","e"]
c=0
add=0
add1=0
for argu in word:
    argu=check(argu,lowercase)
    print(argu)
    word[c]=argu
    if c<=3:
        add=add+argu
    else:
        add1=add1+argu
    c+=1
result=add*10+add1

print(result,"%")

    

    



