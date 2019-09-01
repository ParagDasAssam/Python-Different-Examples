# write a program that calculates Damerau-Levenshtein distance between two strings

def dam_lev(a, b, i, j):
    la = len(a)
    lb = len(b)
    if i == 0 and j == 0:
        return 0
    else:
        res = la + lb + 1
        if i > 0:
            res = min (res, 1 + dam_lev(a, b, i-1, j))
        if j > 0:
            res = min (res, 1 + dam_lev(a, b, i, j-1))
        if i > 0 and j > 0:
            res = min (res, (a[i-1] != b[j-1]) + dam_lev(a, b, i-1, j-1))
            if i > 1 and j > 1 and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
                res = min (res, 1 + dam_lev(a, b, i-2, j-2))
        return res
        
w1 = input("Enter the first word: ")
w2 = input("Enter the second word: ")
print ("The distance between " + w1 + " and " + w2 + " is " + str(dam_lev(w1, w2, len(w1), len(w2))))
