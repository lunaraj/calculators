import random
import math
import sys
calculations = 0
def factor(aValue, bValue, cValue, var):  
    '''
    input: a, b, and c values of the quadratic equation
    and the letter that is being used for a variable.
    output: the quadratic factored and the roots of 
    the quadratic if it can be factored. Returns whether
    the quadratic can be factored 
    '''
    global calculations
    bozo = ''
    #if aValue is negative it factors out negative 1
    if aValue < 0:
        aValue = -aValue
        bValue = -bValue
        cValue = -cValue
        bozo = '-'
    #the factors will multiply to multValue and add to addValue
    multValue = aValue * cValue
    addValue = bValue
    factor1 = 0
    factor2 = 0
    guesses = 0
    multiple = 0
    #finds the smallest number of a, b, and c value so can find the gcf of all three later. if difference of squares it doesn't count the bValue
    if bValue == 0:
        if abs(aValue) <= abs(cValue):
            divisor = abs(aValue)
        elif abs(cValue) < abs(aValue):
            divisor = abs(cValue)
    else: 
        if abs(aValue) <= abs(bValue) and abs(aValue) <= abs(cValue):
            divisor = abs(aValue)
        if abs(bValue) <= abs(aValue) and abs(bValue) <= abs(cValue):
            divisor = abs(bValue)
        if abs(cValue) <= abs(aValue) and abs(cValue) <= abs(bValue):
            divisor = abs(cValue)
    #factors out greatest common factor
    calculations += 7
    while divisor > 0:
        if aValue%divisor == 0 and bValue%divisor == 0 and cValue%divisor == 0:
            multiple = divisor
            break
        else:
            divisor -= 1
            calculations += 1
    if multiple > 1:
        multiple = str(multiple)
    else:
        multiple = ''
    #adds factors of multValue to list
    factorMult = []
    divisor = abs(multValue)
    while divisor > 0:
        if multValue%divisor == 0:
            factorMult.append(divisor)
            factorMult.append(-divisor)
        divisor -= 1
        calculations += 2
    length = len(factorMult)
    #finds the factors that will work
    while True:
        if factor1 + factor2 == addValue and factor1 * factor2 == multValue:
            break
        else:
            factor1 = factorMult[random.randint(0,length-1)]
            factor2 = factorMult[random.randint(0,length-1)]
            guesses += 1
            calculations += 2
        if guesses > abs(multValue*100):
            print('\n\n\nfactored form: none\n')
            return True
    #uses x method to divide factors
    divisor = aValue
    while divisor > 0:
        if aValue%divisor == 0 and factor1%divisor == 0:
            factor1Gcf = divisor
            break
        else:
            divisor -= 1
            calculations += 1
    divisor = aValue
    while divisor > 0:
        if aValue%divisor == 0 and factor2%divisor == 0:
            factor2Gcf = divisor
            break
        else:
            divisor -= 1
            calculations += 1
    if factor1 < 0:
        neg = ''
    else:
        neg = '+'
    if factor2 < 0:
        neg2 = ''
    else:
        neg2 = '+'
    aValue2 = str(int(aValue/factor1Gcf))
    aValue3 = str(int(aValue/factor2Gcf))
    aValue4 = int(aValue2)
    aValue5 = int(aValue3)
    if aValue3 == '1':
        aValue3 = ''
    if aValue2 == '1':
        aValue2 = ''
    firstFactor = int(factor1/factor1Gcf)
    secondFactor = int(factor2/factor2Gcf)
    print('\n\n\nfactored form: ' + bozo + multiple + '(' + aValue2 + var + neg + str(firstFactor) + ')' + '(' + aValue3 + var + neg2 + str(secondFactor) + ')')
    def gcfDivide(factor, aValue):
        gcf = math.gcd(abs(factor), aValue)
        factor = factor/gcf
        aValue = aValue/gcf
        if aValue == 1:
            return int(-factor)
        else:
            return str(int(-factor)) + '/' + str(int(aValue))
    root1 = gcfDivide(firstFactor, aValue4)
    root2 = gcfDivide(secondFactor, aValue5)
    print('roots: ' + str(root1) + ' and ' + str(root2))
    calculations += 10
    return False
def quadratics(aValue, bValue, cValue, var):
    global calculations
    isUnFactorable = factor(aValue, bValue, cValue, var)
    if isUnFactorable:
        def finddiscriminant(a, b, c):
            '''
            input: a b and c values of the quadratic.
            output: the discriminant of the quadratic.
            '''
            dis = b**2-(4*a*c)
            if dis < 0:
                return False
            else:
                return dis
        discriminant = finddiscriminant(aValue, bValue, cValue)
        calculations += 5
        if discriminant == False:
            sys.exit('no solutions')
        def simplifyDiscriminant(a, b, dis):
            '''
            input: a and b values, discriminant
            output: the radical with the discriminant is symplified
            '''
            global calculations
            squareList = [1]
            squareFactors = []
            mult = 1
            while max(squareList) < dis:
                squareList.append(mult**2)
                mult += 1
                calculations += 1
            for i in squareList:
                if dis%i == 0:
                    squareFactors.append(i)
            del(squareFactors[0])
            newDis = dis/max(squareFactors)
            return (int(math.sqrt(max(squareFactors))), int(newDis))
        newDis = simplifyDiscriminant(aValue, bValue, discriminant)
        gcf = math.gcd((2*aValue), bValue, newDis[0])
        neg = ''
        if aValue < 0:
            aValue = -aValue
            neg = '-'
        bozo = newDis[0]/gcf
        if neg == '-':
            paren = ('(', ')')
        else:
            paren = ('', '')
        if bozo == 1:
            bozo = ''
        else:
            bozo = str(int(bozo)) + '*'
        str1 = neg + paren[0] + str(int(-bValue/gcf)) + ' - ' + str(bozo) + 'sqrt' + str(int(newDis[1])) + paren[1]
        str2 = neg + paren[0] + str(int(-bValue/gcf)) + ' + ' + str(bozo) + 'sqrt' + str(int(newDis[1])) + paren[1]
        fraction = ''
        spaces = ''
        for i in range(len(str1)):
            fraction += '-'
        for i in range(len(str1)//2):
            spaces += ' '
        if (2*abs(aValue))/gcf > 1:
            print('root1:\n' + str1 + '\n' + fraction + '\n' + spaces + str(int((2*aValue)/gcf)) + '\n')
            print('root2:\n' + str2 + '\n' + fraction + '\n' + spaces + str(int((2*aValue)/gcf)) + '\n')
        else:
            print('root 1: ' + neg + paren[0] + str(int(-bValue/gcf)) + ' - ' + str(bozo) + 'sqrt' + str(int(newDis[1])) + paren[1] + '\n')
            print('root 2: ' + neg + paren[0] + str(int(-bValue/gcf)) + ' + ' + str(bozo)+ 'sqrt' + str(int(newDis[1])) + paren[1] + '\n')
    calculations += 10
    print(str(calculations) + ' calculations')
aValue = int(input('what is your a value '))
bValue = int(input('what is your b value '))
cValue = int(input('what is your c value '))
var = input('what is your variable ')   
quadratics(aValue, bValue, cValue, var)
