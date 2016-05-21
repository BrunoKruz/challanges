# Created by Bruno Ramos
# bruno.kruz@gmail.com
# 20/05/2016 Rio de Janeiro
import sys

dic = {'zero':0, 'one' :1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
       'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17,
       'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70,
       'eighty':80, 'ninety':90}



def __1000000__(val):
    result = 0
    split = val.split("million")
    for m in split[:-1]:
        result += __1000__(m) * 1000000
    return result + __1000__(split[-1])


def __1000__(val):
    result = 0
    split = val.split("thousand")
    for m in split[:-1]:
        result += __100__(m) * 1000
    return result + __100__(split[-1])


def __100__(val):
    result = 0
    split = val.split("hundred")
    for m in split[:-1]:
        result += __10__(m) * 100
    return result + __10__(split[-1])


def __10__(val):
    val = val.strip()

    if len(val) == 0:
        return 0

    result = 0
    for i in val.split(' '):
        result += dic[i]


    return result


with open("C:\Temp\input.txt", 'r') as test_cases:
 for test in test_cases:
    test = test.strip()
    if len(test) == 0:
        continue
    negative = False
    if "negative" in test:
        negative = True
        test = test.replace("negative ", "").strip()

    result = __1000000__(test)
    if negative:
        print(0-result)
    else:
        print(result)

test_cases.close()

