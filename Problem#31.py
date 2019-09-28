'''
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

'''


# Inefficient solution
def recursive_solve(str1, str2, i, k):

    if i == 0:
        return k

    if k == 0:
        return i

    if str1[i-1] == str2[k-1]:
        return recursive_solve(str1, str2, i-1, k-1)

    return 1 + min( min(recursive_solve(str1, str2, i-1, k-1), recursive_solve(str1, str2, i-1, k)),
            recursive_solve(str1, str2, i, k-1))



# Efficient solution O(n^2)
def dynamic_solve(str1, str2):

    l1 = len(str1)
    l2 = len(str2)

    dp = [[0 for i in range(l2+1)] for j in range(l1+1)]


    for i in range(l1+1):

        for j in range(l2+1):

            if(i == 0):
                dp[i][j] = j
            elif(j == 0):
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 +  min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j]))

    return dp[l1][l2]
str1 = input()
str2 = input()
len1 = len(str1)
len2 = len(str2)
print(recursive_solve(str1, str2, len1, len2))
print(dynamic_solve(str1, str2))
