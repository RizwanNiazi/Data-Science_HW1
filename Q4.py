#-------------Q4------
str = 'Print only the words that start with s in this sentence'
count=0
count1=0
for i in range(0,len(str)):
    if ord(str[i])>64 and ord(str[i])<91:
        count=count+1
    elif ord(str[i])>96 and ord(str[i])<123:
        count1=count1+1
print('Upper case letter :',count)
print('Lower case letter :',count1)
