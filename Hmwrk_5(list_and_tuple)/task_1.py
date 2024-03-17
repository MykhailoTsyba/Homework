text = 'Some men interpret nine memos'
text_1 = text.lower()
text_2 = text_1.replace(' ', '')
list_1 = list()
list_1.extend(text_2)
list_reverse = list(reversed(list_1))

if list_1 == list_reverse:
    print('It\'s a pallindrome')
else:
    print('It\'s not a pallindrome')
