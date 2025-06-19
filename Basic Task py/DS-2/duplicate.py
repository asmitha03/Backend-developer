def duplicate(list):
    seen = set()
    res = []
    for item in list:
        if item not in seen:
            seen.add(item)
            res.append(item)
    return res
num = [2,4,5,3,3,4]
s_num = duplicate(num)
print(s_num)