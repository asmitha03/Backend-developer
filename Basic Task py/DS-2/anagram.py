def anagram(txt1,txt2):
    txt1 = txt1.replace("","").lower()
    txt2 = txt2.replace("","").lower()
    return sorted(txt1) == sorted(txt1)
a = input("Enter a word:")
b = input("Enter a word:")
if anagram(a,b):
    print("Its an anagram")
else:
    print("Its not an anagram")
    