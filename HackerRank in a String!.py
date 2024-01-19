main_str = "hackerrank"
n = int(input())
for i in range(n):
    user_str = input()
    for char in main_str:
        if char in user_str:
            user_str = user_str[user_str.index(char) + 1:]
        else:
            print("No")
            break
    else:
        print("YES")
"""m_str = "hackerrank"
n = int(input())

for i in range(n):
    u_str = input()

    iter_u_str = iter(u_str)
    if all(char in iter_u_str for char in m_str):
        print("YES")
    else:
        print("NO")"""



