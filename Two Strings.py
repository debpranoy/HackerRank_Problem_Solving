num_pairs = int(input("Enter the number of pairs: "))

for _ in range(num_pairs):
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    if len(set(s1) & set(s2)) > 0:
        print('YES') 
    else:
        print('NO') 