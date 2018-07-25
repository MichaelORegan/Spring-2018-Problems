# Michael O'Regan
# 25.07.2018
# objective: to write a function to mulitply 2 numbner without using * or /
# from Q 11,13 = 143, 5, 123 = 615

def sumultiply(x , y):
    total = 0               
    # total will become the answer
    for i in range(y):
        # we want the addition of x to be done y times
        total = total + x
    return total    
        
print(sumultiply(10,10))
print(sumultiply(11,13))
print(sumultiply(5,123))