import math


# All of the function in the calculators
def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        return print('choose another num')
    else:
        return num1 / num2


def exp(num1, num2):
    return num1 ** num2


def sqrt(x):
    return math.sqrt(x)


def fac(x):
    return math.factorial(x)


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def div_avg(num1, num2):
    if num2 == 0:
        return ('choose another num')
    else:
        return num1 // num2


def log(num1, num2):
    return math.log(num2, num1)


def cir_circum(rad):
    return math.pi * 2 * rad


##used for the loop when exiting
user_input = True

##the loop and how to break it by typing exit
while user_input:
    intput = input("Köra?")
    if intput.lower() == "nej":
        user_input = False
    else:

        ##opperation selection
        print('choose operation')
        print('1. add')
        print('2. sub')
        print('3. mult')
        print('4. div')
        print('5. div avg')
        print('6. exp')
        print('7. sqrt')
        print('8. factorial')
        print('9. sin')
        print('10. cos')
        print('11. tan')
        print('12. logarthims')
        print('13. circle circumfrence')
        print('stop')

        ##the input that chooses the operation
        choose = input('operation (1/2/3/4/5/6/7/8/9/10/11/12/13/stop):')

        ##the opperations selection
        if choose == '1':
            num1 = float(input('choose num1'))
            num2 = float(input('choose num2'))
            sum = add(num1, num2)
            print(sum)
        elif choose == '2':
            num1 = float(input('choose num1'))
            num2 = float(input('choose num2'))
            dif = sub(num1, num2)
            print(dif)
        elif choose == '3':
            num1 = float(input('choose num1'))
            num2 = float(input('choose num2'))
            result = mult(num1, num2)
            print(result)
        elif choose == '4':
            num1 = float(input('choose num1'))
            num2 = float(input('choose num2'))
            result_div = div(num1, num2)
            print(result_div)
        elif choose == '6':
            num1 = float(input('choose num1'))
            num2 = float(input('choose num2'))
            result_exp = exp(num1, num2)
            print(result_exp)
        elif choose == '7':
            x = float(input('choose num'))
            result_sqrt = sqrt(x)
            print(result_sqrt)
        elif choose == '8':
            x = int(input('choose num'))
            result_fac = fac(x)
            print(result_fac)
        elif choose == '9':
            x = float(input('choose num'))
            result_sin = sin(x)
            print(result_sin)
        elif choose == '10':
            x = float(input('choose num'))
            result_cos = cos(x)
            print(result_cos)
        elif choose == '11':
            x = float(input('choose num'))
            result_tan = tan(x)
            print(result_tan)
        elif choose == '5':
            num1 = float(input('choose num1'))
            num2 = float(input('choose num2'))
            result_div_avg = div_avg(num1, num2)
            print(result_div_avg)
        elif choose == '12':
            num1 = float(input('choose num1'))
            num2 = float(input('choose num2'))
            result_log = log(num1, num2)
            print(result_log)
        elif choose == '13':
            rad = float(input('what is the radius'))
            result_rad = cir_circum(rad)
            print(result_rad)
        elif choose == 'stop':
            break
        else:
            print('choose number from 1-13')
