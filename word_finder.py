import re

#wordfind
count=0

pattern= re.compile("Software",re.I|re.M)
with open ('input.txt', 'rt') as hand:
    for line in hand:
        line =line.rstrip()
        wordfinder= re.findall(pattern,line)
        print(len(wordfinder))
        print(count)