def prefix_function(string, sub_string):
    string = sub_string + '@' + string
    n = len(string)
    sub_len = len(sub_string)
    pi = [0 for i in range(n)]
    for i in range(1, n):
        j = pi[i - 1]
        while (j > 0) and (string[i] != string[j]):
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j
        if pi[i] == sub_len:
            return i - sub_len * 2
    return -1


if __name__ == '__main__':
    string = "abaabaaaabaabaaab"
    search_str = "aabaa"
    # string = search_str + '@' + string
    print(prefix_function(string,search_str))
