import re


count=0
lines=[]
findword=input("Enter the word:\n")
pattern=re.compile(findword,re.I|re.M)
with open (r'D:\Ltts training\Mini_project\input.txt', 'rt') as hand:
    lines=hand.read()
    '''for element in lines:
        element=lines.rstrip()
        print(element)'''

    for line in lines:
        wordfinder= re.findall(pattern,line)
        file_list=lines.split()


    create_file = open(findword+".txt",'a')
    for i in range(len(file_list)):
        wordfoud= re.match(findword, file_list[i],re.I|re.M)
        if wordfoud:
            count+=1

            create_file.write(file_list[i-1]+' '+file_list[i]+''+file_list[i+1]+"\n")
            
            create_file.write(str(count)+ ':')

    #create_file.write('word repeated:'+ str(len(pattern)) + '\n')

    



        #print(file_list)
        
        #with open(findword.txt, "a+") as file_object:
            #for word in wordfinder:
                #print(word)
                #count+=1


#print(count)
