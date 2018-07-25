# Michael O'Regan
# 25.07.2018

# simple interest calculation
# python p3simpleinterest.py

def simple_interest(p, r, t):
# p = principle r = rate t = time
    i = (p * (r/100)) * t
    si = p + i

    return round(si, 2)

print(simple_interest(1000, 3, 5))
print(simple_interest(1000, 7, 10))