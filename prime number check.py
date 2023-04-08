n = int(input("Prime Check: "))

if n <= 1:
    print("Not prime")
    False
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print("Note prime")
        False
print("Prime")




