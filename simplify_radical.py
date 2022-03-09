import math
def simplifyRadical(rad):
    '''
    Parameters
    ----------
    rad : square root
    Returns
    -------
    symplified square root
    '''
    squareList = [1]
    squareFactors = []
    mult = 1
    while max(squareList) < rad:
        squareList.append(mult**2)
        mult += 1
    for i in squareList:
        if rad%i == 0:
            squareFactors.append(i)
    del(squareFactors[0])
    newRad = rad/max(squareFactors)
    return (int(math.sqrt(max(squareFactors))), int(newRad))
rad = int(input('type in square root: '))
newRad = simplifyRadical(rad)
print(str(newRad[0]) + 'sqrt' + str(newRad[1]))
