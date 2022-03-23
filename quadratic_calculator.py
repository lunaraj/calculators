import random
import math
import sys
class fixEquation(object):
    '''
    methods to put equation into standard form
    '''
    def __init__(self, equation, var):
        self.equation = equation
        self.var = var
    def sortTerms(self):
        '''
        input: nothing
        output: tuple of lists containing terms

        '''
        terms = self.equation.split(' ')
        a = []
        b = []
        c = []
        neg = 1
        neg2 = 1
        for term in terms:
            if term == '+':
                neg = 1
            elif term == '-':
                neg = -1
            elif term == '=':
                neg2 = -1
                neg = 1
            elif '^' in term and self.var in term: #checks if term is a square
                if term[0] == self.var:
                    a.append(1*neg2*neg)
                else:
                    termCopy = term.split(self.var)
                    a.append(int(termCopy[0])*neg2*neg)
            elif self.var in term: #checks if term is a value of var
                termCopy = term.split(self.var)
                if term[0] == self.var:
                    b.append(1*neg2*neg)
                else:
                    b.append(int(termCopy[0])*neg2*neg)
            else:
                c.append(int(term)*neg2*neg)
        return (a, b, c)
    def addLikeTerms(self, abc):
        a = abc[0]
        b = abc[1]
        c = abc[2]
        aValue = 0
        bValue = 0
        cValue = 0
        for digit in a:
            aValue += digit
        for digit in b:
            bValue += digit
        if bValue >= 0:
            posb = '+'
        else:
            posb = ''
        for digit in c:
            cValue += digit
        if cValue >= 0:
            posc = '+'
        else:
            posc = ''
        print('\n\n\nstandard form: ' + str(aValue) + self.var + '^2' + posb + str(bValue) + self.var + posc + str(cValue) + '=0')
        return (aValue, bValue, cValue)
class solveQuadratic(object):
    def __init__(self):
        self.vals = []
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
        ogaValue = aValue
        ogbValue = bValue
        ogcValue = cValue
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
        calculations += 7
        multiple = math.gcd(aValue, bValue, cValue)
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
            if guesses > len(factorMult) * 100:
                print('\nfactored form: none\n')
                solveQuadratic.finddis(ogaValue, ogbValue, ogcValue)
                return True
        #uses x method to divide factors
        factor1Gcf = math.gcd(aValue, factor1)
        factor2Gcf = math.gcd(aValue, factor2)
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
        finddis(ogaValue, ogbValue, ogcValue)
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
        print('roots: ' + str(root1) + ' or ' + str(root2))
        calculations += 10
        return False
    def finddis(a, b, c):
        '''
        input: a b and c values of the quadratic.
        output: the discriminant of the quadratic.
        '''
        dis = b**2-(4*a*c)
        print('discriminant: ' + str(dis) + '\n')
def quadratics(aValue, bValue, cValue, var):
    global calculations
    isUnFactorable = solveQuadratic.factor(aValue, bValue, cValue, var)
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
            calculations += 1
        for i in range(len(str1)//2):
            spaces += ' '
            calculations += 1
        if (2*abs(aValue))/gcf > 1:
            print('root1:\n' + str1 + '\n' + fraction + '\n' + spaces + str(int((2*aValue)/gcf)) + '\n')
            print('root2:\n' + str2 + '\n' + fraction + '\n' + spaces + str(int((2*aValue)/gcf)) + '\n')
        else:
            print('root 1: ' + neg + paren[0] + str(int(-bValue/gcf)) + ' - ' + str(bozo) + 'sqrt' + str(int(newDis[1])) + paren[1] + '\n')
            print('root 2: ' + neg + paren[0] + str(int(-bValue/gcf)) + ' + ' + str(bozo)+ 'sqrt' + str(int(newDis[1])) + paren[1] + '\n')
    calculations += 10
    print(str(calculations) + ' calculations')
def finddis(a, b, c):
    '''
    input: a b and c values of the quadratic.
    output: the discriminant of the quadratic.
    '''
    dis = b**2-(4*a*c)
    print('discriminant: ' + str(dis) + '\n')
def ask():
    '''
    input: nothing
    output: nothing
    does all the inputs
    '''
    equation = input('type in equation ')
    var = input('what is your variable ')
    fix = fixEquation(equation, var)
    simplified = fix.addLikeTerms(fix.sortTerms())
    quadratics(simplified[0], simplified[1], simplified[2], var)
calculations = 0
ask()
