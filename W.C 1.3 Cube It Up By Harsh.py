def cubeDigitSum(n):
    if n % 3 == 0:
        pop = 18 * int(n/3)
    elif (n-1) % 3 == 0:
        pop = 18 * int(n/3) + 1
    elif (n-2) % 3 == 0:
        pop = 18 * int(n/3) + 9
    return pop


answer = 1
for i in range(0, 3):
    n = int(input("Enter The Value Of N : "))
    answer *= cubeDigitSum(n) % 1000007
print("Final Answer = ", answer % 1000007)
#ansWhenNIs5 = 27
#ansWhenNIs500 = 2997
#ansWhenNIs5000000000 = 790004
#product = 63926333676
#finalAns = 886201