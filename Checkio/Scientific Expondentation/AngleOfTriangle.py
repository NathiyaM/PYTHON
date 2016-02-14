import math
def checkio(a,b,c):
    b = (a**2 + c**2 - b**2)/(2*a*c)
    print(b)
    angleb = math.acosh((math.radians(b)))
    print(angleb)









if __name__ == '__main__':
    result = checkio(4,4,4)
    print(result)