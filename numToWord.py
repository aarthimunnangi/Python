import os
import sys


inputNum = int(input("Enter number: "))
def numToWord(inputNum):
        units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        finalWord = ""
        if (inputNum == 0):
            finalWord == "Zero"
        if inputNum > 1000:
            finalWord = numToWord(inputNum // 1000) + " " + "thousand"
            inputNum %= 1000
        if inputNum >= 100:
            finalWord = finalWord + units[(inputNum // 100) - 1] + " " + "hundred"
            inputNum %= 100
        if inputNum >= 20:
            finalWord = finalWord + " " + tens[(inputNum // 10) - 2] + " "
            inputNum %= 10
        if inputNum > 0:
            finalWord = finalWord + " " + units[inputNum - 1]
        return finalWord


if __name__ == "__main__":
    Word = numToWord(inputNum)
    print(Word)




