def theLoveLetterMystery(s):
    ans = 0
    for i in range(len(s)//2):
           man = abs(ord(s[-1-i]) - ord(s[i]))
           ans += man
    return(ans+(abs(ord(s[-1-i]) - ord(s[i]))))

n = int(input())
for i in range(n):
    user_inp = input()
    Palindrome  = theLoveLetterMystery(user_inp)
    print(Palindrome)
