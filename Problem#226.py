'''
This problem was asked by Airbnb.

You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y']

'''



def solve(arr):

    unique_word = set()     
    new_arr = []
    k = 0
    arr = list(map(str, arr))
    for i in arr:
        new_arr.append([])
        for j in i:
            new_arr[k].append(j)
        k += 1

    for i in arr:
        for j in str(i):
            unique_word.add(j)

    _dict = {i : {j:0 for j in unique_word if i != j} for i in unique_word}

    word_list = {}

    for i in unique_word:
        word_list[i] = 0
    k = 0
    max_len = 0
    for i in new_arr:
       if max_len < len(i):
           max_len = len(i)

    for i in range(len(new_arr)):
        for j in range(max_len - len(new_arr[i])):
            new_arr[i].append(' ')

    for k in range(max_len):
        for i in range(len(new_arr)-1):
            for j in range(i+1, len(new_arr)):
                if ''.join(new_arr[i][0:k]) == ''.join(new_arr[j][0:k]) and new_arr[i][k] in _dict  and new_arr[j][k] in _dict[new_arr[i][k]] and  _dict[new_arr[i][k]][new_arr[j][k]] == 0:
                    _dict[new_arr[i][k]][new_arr[j][k]],_dict[new_arr[j][k]][new_arr[i][k]] = 1, 1
                    word_list[new_arr[i][k]] += 1

    res = []
    for i in word_list:
        res.append([word_list[i], i])
    res = sorted(res, reverse = True)

    result = []


    for i in res:
        result.append(i[1])

    return result


print(solve(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']))
            

        

