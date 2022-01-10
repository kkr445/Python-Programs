#Getting Input
def input_matrix(m,n):
  l=[] 
  for i in range(0,m):
    print("\nEnter the row one by one")
    a=[]
    for j in range(0,n):
      a.append(int(input("Enter element:")))
    l.append(a)
  return l

#Display function
def display(a):
  for i in range(len(a)):
    for j in range(len(a[0])):
      print(a[i][j],end=" ")
    print()

#Addition of 2 matrices
def addmatrix(a,b):
  r=[]
  for i in range(len(a)):
    r.append([a[i][j] + b[i][j] for j in range(len(a[0]))])
  display(r)


m = int(input("No. of rows: "))
n = int(input("No. of columns: "))

print("\nInput for the A")
a=input_matrix(m,n)
print("\nInput for the B")
b=input_matrix(m,n)
print("\nPrinting A matrix: ")
display(a)
print("\nPrinting B matrix: ")
display(b)
print("\nA+B = ")
addmatrix(a,b)

