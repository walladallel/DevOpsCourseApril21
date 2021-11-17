import collections

myword = input("Please Enter Your Sentence: ")

def most_frequent_char(myword):
    str_lower = myword.lower()
    print("The most frequent Char is:", collections.Counter(str_lower).most_common(1)[0])

most_frequent_char(myword)