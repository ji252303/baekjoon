a = input().upper()

t_word = list(set(a))

ct_list = []

for i in t_word:
    ct = a.count(i)
    ct_list.append(ct)

if ct_list.count(max(ct_list)) > 1:
    print("?")
else:
    max_index = ct_list.index(max(ct_list))
    print(t_word[max_index])
