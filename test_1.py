import re

count=0
software=[]
lines=0

pattern=re.compile("Software",re.I|re.M)

with open(r'D:\Ltts training\Mini_project\input.txt','rt') as file_info:

    for file_line in file_info:
        lines +=1
        if pattern.search(file_line)!=None:
            software.append((lines,file_line.rstrip('\n')))

    for ans in software:
        count+=1
        with open("software.txt",'a') as file_ans:
            file_ans.writelines(str(count)+':')
            file_ans.writelines(ans[1]+'\n')
print(count)