def frequency_word(text):
    words = text.split()
    res = {}
    for word in words:
       if word in res:
           res[word] += 1
       else:
           res[word] = 1
    return res
s = input("Enter a sentence:")
count = frequency_word(s)
print(count)
