import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) > len(num2):
    print ('False')
    sys.exit(0)
count = 0
for i in range(len(num2)):
        if num2[i] == num1[0]:
            for j in range(len(num1)):
                if num2[i+j] == num1[j]:
                    count += 1
if count == len(num1):
    print(True)
else: print(False)
# ******************************
# Make your Code
# ******************************

# print ('True') or ('False')
