#String -> text
# int -> geheel getal
# float -> komma getal
# boolean -> true of false
import math
from re import A


x = '5'
y = 5
Z = 5.0

# leeftijd = input("leeftijd")  # geeft een string
# print('Syntra')
# print(5)


def print_leeftijd():
    leeftijd = input("leeftijd")  # geeft een string
    print(leeftijd)

#print_leeftijd()

def old_enough_to_drive(age):
    if age > 18:
        print("old enough to drive")
    else:
        print("not old enough to drive")


def calc_sqrt(getal):
    print(f"sqrt of getal is {math.sqrt(getal)}")

calc_sqrt(9)

nrs = [1,2,3,4,5,6,7,8,9,10]


def travel_list(nrs, limit):
    cnt = 0
    for i in nrs:
        if i < limit:
           cnt += 1
    print(cnt)

travel_list(nrs,6)






