x=("      hello world       ")
print("without striping: ",x)
y=x.lstrip()  # striping left side blank space
print("after left side striping: ",y)
w=x.rstrip()  # striping right side blank space
print("after right side striping: ",w)
z=x.strip()   # striping both side blank space
print("after both side striping: ",z)