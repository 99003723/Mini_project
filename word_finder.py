import re


count=0
findword=input("Enter the word:\n")
pattern=re.compile(findword,re.I|re.M)
with open (r'D:\Ltts training\Mini_project\input.txt', 'rt') as hand:
    lines=hand.readlines()
    for line in lines:
        wordfinder= re.findall(pattern,line)
        
        for word in wordfinder:
            print(word)
            count+=1

print(count)
