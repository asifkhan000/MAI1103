#opening file
student = open("data.txt.txt",'wt')


#while loop
i = 1
while True:
    if(i<=2):
        khan = raw_input("enter name >>")
        salman = student.write(khan+"\n")
        i=i +1
    else:
         break                      


student.close()
