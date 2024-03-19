"""#def is_palindrome(s):
s = input()
s = ascii(s)
s = ''.join(s.split()).lower()
if s == s[::-1]:
    print("YES")
else:
    print("NO")

#word = "aaabbbb"
#if is_palindrome(word):
   # print("True")
#else:
    #print("False")
n =  int(input())
for i in range(1,n+1):
    for j in range(1,11):
       print(f"{j} x {i} = {j*i}")
    break
"""
def gameOfThrones(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    counts = []

    for c in alpha:
        counts.append(s.count(c))

    counts = list(filter(lambda x: x % 2 != 0, counts))

    if len(counts) > 1:
        return 'NO'
    else:
        return 'YES'

input_string = input().lower()
result = gameOfThrones(input_string)
print(result)

