#------------Q7--------
def rever_str(str):
    new_str=''
    x=len(str)
    while x:
        x-=1
        new_str+=str[x]
    print(new_str)

str="Hello"
rever_str(str)
