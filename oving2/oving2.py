import math

def archimedesPI(iterations = 10):
    """Returns an estimate of Pi calculated with Archimedes' method"""
    if iterations >= 501:
        print("Choose a lower number")
        return None

    lengthOfSide = 1
    numberOfSides = 6

    for x in range(iterations):
        halfSide = lengthOfSide / 2
        a = math.sqrt(1 - (halfSide ** 2))
        b = 1 - a
        newSide = math.sqrt((b**2) + (halfSide**2))
        perimiter = numberOfSides* lengthOfSide
        pi = perimiter / 2
        lengthOfSide = newSide
        numberOfSides *= 2
    return pi

if __name__ = "__main__":
    print(archimedesPI(500))

