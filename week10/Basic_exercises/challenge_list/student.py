

def enrollment_stats(list_of_universities):
    # Variables
    total_students = []
    total_tuition = []

    # Iterate through lists, adding values
    for u in list_of_universities: 
        total_students.append(u[1])
        total_tuition.append(u[2])    

    # Return variables
    return total_students, total_tuition


def mean(values):
    """Return the mean value in the list `values`"""
    sum = 0
    for i in values:
        sum += i
    return sum/len(values)


def median(values):
    """Return the median value of the list `values`"""
    sorted_list = sorted(values)

    if len(sorted_list) % 2 == 0:
        e_1 = sorted_list[len(sorted_list)//2]
        e_2 = sorted_list[len(sorted_list)//2 + 1]
        return (e_1 + e_2) / 2
    else:
        return sorted_list[len(sorted_list)//2 + 1]
    
    
universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]

totals = enrollment_stats(universities)

print("\n")
print("*****" * 6)
print(f"Total students:   {sum(totals[0]):,}")
print(f"Total tuition:  $ {sum(totals[1]):,}")
print(f"\nStudent mean:     {mean(totals[0]):,.2f}")
print(f"Student median:   {median(totals[0]):,}")
print(f"\nTuition mean:   $ {mean(totals[1]):,.2f}")
print(f"Tuition median: $ {median(totals[1]):,}")
print("*****" * 6)
print("\n")