def grid(n):
    table = n
    res = [] 
    for x in range (1, table):
        row = []
        for y in range(1,11):
            row.append(x * y) 
        res.append(row) 
    return res 

def asd():
  n = int(input("here: "))
  finalresult = grid(n+1)
  for x in finalresult:
    for y in x:
      print(y,end="\t")
    print()


asd()