n=int(input())
if n!=1:
    for i in range(2,n):
        z=n%i
        if z==0:
            print("číslo není prvočíslo")
            break
    if z!=0:
        print("číslo je prvočíslo")
if n==1:
    print("Jedna není prvočíslo, nevím co zkoušíš")
input()