import random

nr = 100_000
leeftijd = 0 

a = 1
b = 2
c = 3
d = 4

vorige_plaats = None
nu = a
volgende_plaats = None

for i in range(nr):
    while True:
        volgende_plaats = random.randint(0,4)
        if volgende_plaats not in (nu, vorige_plaats):
            vorige_plaats = nu 
            nu = volgende_plaats
            if nu == d:
                leeftijd +=1
                break
            leeftijd += 1

print(f"{leeftijd/nr:.2f}")

