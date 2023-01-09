file=open("thefile.txt","r")
count=0
a=file.read()
a=a.split()
for i in a:
    if i[0].lower()=="v":
        count=count+1
print("No of letters starting with v/V are",count)
file.close()