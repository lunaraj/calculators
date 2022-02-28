import math
def factorByGrouping(a, b, c, d, var):
    if c < 0:
        c = -c
        d = -d
        neg = '-'
    else:
        neg = '+'
    gcf = math.gcd(a, b)
    if b < 0:
        pos = ''
    else:
        pos = '+'
    gcf2 = math.gcd(c, d)
    if gcf == 1:
        newGcf = ''
    else:
        newGcf = str(gcf)
    if a/gcf == 1:
        aGcf = ''
    else:
        aGcf = str(int(a/gcf))
    if neg == '-' and math.sqrt(gcf2).is_integer() == True:
        gcf = math.sqrt(gcf)
        if gcf == 1:
            newGcf = ''
        else:
            newGcf = str(gcf)
        gcf2 = math.sqrt(gcf2)
        gcf2 = int(gcf2)
        print('(' + newGcf + var + '-' + str(gcf2) + ')(' + newGcf + var + '+' + str(gcf2) + ')(' + aGcf + var + pos + str(int(b/gcf)) + ')')
    else:
        gcf2 = int(gcf2)
        print('(' + newGcf + var + '^2' + neg + str(gcf2) + ')(' + aGcf + var + pos + str(int(b/gcf)) + ')')
def ask():
    '''
    input: nothing
    output: nothing
    does all the inputs
    '''
    aValue = int(input('what is your a value '))
    bValue = int(input('what is your b value ')) 
    cValue = int(input('what is your c value '))
    dValue = int(input('what is your d value '))
    var = input('what is your variable ')
    factorByGrouping(aValue, bValue, cValue, dValue, var)
calculations = 0
ask()
