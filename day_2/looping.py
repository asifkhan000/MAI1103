looping = open("nishu.txt.txt",'rt')
khan = open("khan.txt.txt",'wt')
for i in looping:

    khan.write(i)
    


looping.close()
khan.close()
