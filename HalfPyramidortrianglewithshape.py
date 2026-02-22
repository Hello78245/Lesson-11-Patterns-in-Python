print("Half Pyramid with triangles:")
n=int(input("Enter how many rows of the triangles should be there:"))
for i in range(n):
    print("*",end="")
    for j in range(i+1):
     print("Δ",end="")
    print()