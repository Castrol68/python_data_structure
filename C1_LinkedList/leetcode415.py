def addStrings( num1: str, num2: str) -> str:
    len1 = len(num1)
    len2 = len(num2)
    reverse_result = []
    tmp = 0
    while len1 > 0 or len2 > 0 or tmp != 0:
        if (len1 > 0):
            tmp += ord(num1[len1 - 1]) - ord('0')
        if (len2 > 0):
            tmp += ord(num2[len2 - 1]) - ord('0')
        reverse_result.append(str(tmp % 10))
        tmp = 1 if tmp/10>=1 else 0
        len1 -= 1
        len2 -= 1
    result = ''.join(list(reversed(reverse_result)))
    return result

if __name__ == '__main__':
    num1 = '90'
    num2 = '12'
    # res = addStrings(num1, num2)
    # print(res)
    for i in range(3):
        print(i)