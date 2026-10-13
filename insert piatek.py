

slowo = input()
if len(slowo)<5:
    print("za krotkie")

else: 
    x = len(slowo)
    x -= 1
    while x >= 0:
        print(slowo[x])
        x -= 1