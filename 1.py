n=int(input())
print("dělitelé:")
print("|")
print("|")
print("V")
print()
for i in range(1,n+1):
    if n%i==0:
        print(i)
    else:
        continue
input()