#-------Q1--------

#variable contain string 

str = 'Print only the words that start with s in this sentence'
y=str.split(' ')
for i in y:
    if i[0]=="s":
        print(i)
