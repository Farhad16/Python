sentence = "This is the common question in interview"

char_list = {}
for char in sentence:
    if char in char_list:
        char_list[char] += 1
    else:
        char_list[char] = 1

char_sorted = (sorted(char_list.items(), key=lambda kv: kv[1], reverse=True))
print(char_sorted[0])
