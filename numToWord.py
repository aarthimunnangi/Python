import os
import sys


inputNum = int(input("Enter number: "))
def numToWord(inputNum):
        units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        Word = ""
        if (inputNum == 0):
            Word == "Zero"
        if inputNum >= 10000000:
            Word = numToWord(inputNum // 10000000) + " crore"
            inputNum %= 10000000
        if inputNum >= 100000:
            Word += Word + " " + numToWord(inputNum // 100000) + " lakh"
            inputNum %= 100000
        if inputNum > 1000:
            Word = Word + " " + numToWord(inputNum // 1000) + " " + " thousand"
            inputNum %= 1000
        if inputNum >= 100:
            Word = Word + " " + units[(inputNum // 100) - 1] + " " + " hundred"
            inputNum %= 100
        if inputNum >= 20:
            Word = Word + " " + tens[(inputNum // 10) - 2] + " "
            inputNum %= 10
        if inputNum > 0:
            Word = Word + " " + units[inputNum - 1]
        return Word


if __name__ == "__main__":
    finalWord = numToWord(inputNum)
    print(finalWord)




