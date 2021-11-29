import collections

def most_frequent_char(myword):
    str_lower = myword.lower()
    print("The most frequent Char is:", collections.Counter(str_lower).most_common(1)[0])

if __name__ == '__main__':
    most_frequent_char("letsgodevops")
