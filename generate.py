#!/usr/bin/python


__author__ = 'Andrew Gallo'


def processEven(value):
    return value / 2


def processOdd(value):
    return (3 * value) + 1


def sequence(start):
    for n in range(5, start):
        temp = n
        Ulist = [temp]
        print temp,
        while temp > 1:
            if temp % 2 == 0:
                Ulist.append(processEven(temp))
                print Ulist[-1],
                temp = Ulist[-1]
            else:
                Ulist.append(processOdd(temp))
                print Ulist[-1],
                temp = Ulist[-1]
        print Ulist


def main():
    startval = input("Enter starting value: ")
    sequence(startval)


main()
