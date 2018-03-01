#  write a program that prints out all the elements of the list that are less than 5
def Less_then_5(lis1):
    for lis in lis1:
        if (lis < 5):
            print lis


lis1 = []


n = input("Enter numbers to be entered: ")
for a in range(n):
    var1 = input("Enter %d number: " % (a + 1))
    lis1.append(var1)

ent = input("Enter 1 for less 5 function\nEnter 2 for exit: ")
if ent == 1:
    Less_then_5(lis1)
else:
    print "Exit:"
