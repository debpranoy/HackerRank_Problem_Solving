"""def remove_adjacent_duplicates(s):
    result = []
    for char in s:
        if not result or char != result[-1]:
            result.append(char)
    return ''.join(result)

input_str = "ABABABAB"
output_str = remove_adjacent_duplicates(input_str)
print(len(output_str))
"""
def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions

n = int(input())
for i in range(n):
    user_str = input()
    output_str = alternatingCharacters(user_str)
    print(output_str)