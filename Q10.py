#------------Q10-------
def gensquares(N):
    for i in range(1,N):
        i=i**2
        yield i

for x in gensquares(10):
	  print(x)
