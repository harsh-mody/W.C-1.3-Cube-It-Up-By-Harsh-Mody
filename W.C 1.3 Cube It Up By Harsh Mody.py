sumOfDigitsOfCube = 0
additionOfSumOfDigitsInCase1 = 0
additionOfSumOfDigitsInCase2 = 0
additionOfSumOfDigitsInCase3 = 0
for i in range(1,4):
    number = pow(i,3)
    sumOfDigitsOfCube = sum(int(digit) for digit in str(number))
    # print(sumOfDigitsOfCube)
    additionOfSumOfDigitsInCase1 = sumOfDigitsOfCube + additionOfSumOfDigitsInCase1
    # print(additionOfSumOfDigitsInCase1)
for i in range(1,501):
    number = pow(i,3)
    sumOfDigitsOfCube = sum(int(digit) for digit in str(number))
    # print(sumOfDigitsOfCube)
    additionOfSumOfDigitsInCase2 = sumOfDigitsOfCube + additionOfSumOfDigitsInCase2
    # print(additionOfSumOfDigits)
for i in range(1,5000000001):
    number = pow(i,3)
    sumOfDigitsOfCube = sum(int(digit) for digit in str(number))
    # print(sumOfDigitsOfCube)
    additionOfSumOfDigitsInCase3 = sumOfDigitsOfCube + additionOfSumOfDigitsInCase3
    # print(additionOfSumOfDigitsInCase3)
answer = (additionOfSumOfDigitsInCase1 * additionOfSumOfDigitsInCase2 * additionOfSumOfDigitsInCase3) % 1000007
print("The Final Answer Is : ",  answer)
