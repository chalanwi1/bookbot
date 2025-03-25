def count_words(text):
    count = 0
    for x in text.split():
        count += 1
    return count

def count_chars(text):
    result = {}
    for x in text.lower():
        if x not in result:
            result[x] = 1
        else:
            result[x] += 1
    return result

def sort_on(dic):
    return dic['num']

def dic_toList(num_dic):
    lis = []
    for x in num_dic:
        lis.append({'char': x, 'num': num_dic[x]})
    lis.sort(reverse=True, key=sort_on)
    return lis