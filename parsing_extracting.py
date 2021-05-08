x="hello % i am krishna / and you"
pos=x.find("%")
npos=x.find("/")
y=x[pos+1:npos]
print(y)