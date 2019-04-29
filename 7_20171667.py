def differ_one_char(s1, s2):
    if(len(s1) != len(s2)):
        return False

    diff_cnt = 0
    for i in range(len(s1)):
        if(s1[i] != s2[i]):
            diff_cnt += 1

    return diff_cnt == 1

print(differ_one_char('abc', 'afc'))
print(differ_one_char('def', 'fff'))
print(differ_one_char('abc', 'abcd'))
print(differ_one_char('cat', 'fat'))
print(differ_one_char('power', 'tower'))
