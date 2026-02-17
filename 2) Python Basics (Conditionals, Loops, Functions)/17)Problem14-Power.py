# Problem 14: Power Function: Calculate a^b without using ** operator.

def Power(a,b):
    r = 1 
    for i in range(b):
        r = r * a
    return r

print(Power(5,3))