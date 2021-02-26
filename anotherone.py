import re


count=0
findword=input("Enter the word:\n")
pattern=re.compile(findword,re.I|re.M)

string = open('input.txt','r')
newline=string.read()
new_string = re.sub(r'[^a-zA-Z0-9\n\.]', ' ', newline)
improve=open('improv.txt', 'w').write(new_string)













''' lines=improve.readlines()
    for line in lines:
        wordfinder= re.findall(pattern,line)

        for word in wordfinder:
            print(word)
            count+=1
print(count)'''





