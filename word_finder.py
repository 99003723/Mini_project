import re


string = open('input.txt').read()
new_string = re.sub(r'[^a-zA-Z\n]', ' ', string)
text_file = open("sample.txt", "w")
n = text_file.write(new_string)
text_file.close()


count = 0
findword = input("Enter the word:\n")
pattern = re.compile(findword, re.I | re.M)
hand = open(r'sample.txt')
handle = hand.read()
wordfinder = re.findall(pattern, handle)
file_list = handle.split()

create_file = findword + '.txt'
file_gen = open(create_file, 'w+')
for i in range(len(file_list)):
    wordfound = re.match(findword, file_list[i], re.I | re.M)
    if wordfound:
        count += 1

        sent = (file_list[i-1] + ' ' + file_list[i] + ' ' + file_list[i+1])
        file_gen.write(str(sent) + '\n')
        file_gen.write(str(count) + ' :')

file_gen.write('word repeated:' + str(len(wordfinder)) + '\n')  #pep8 done w/o comments
