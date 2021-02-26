import re

class special_character():
    def __init__(self):

        self.string = open('input.txt').read()
        self.new_string = re.sub(r'[^a-zA-Z\n]', ' ', self.string)
        self.text_file = open("sample.txt", "w")
        self.n = self.text_file.write(self.new_string)
        self.text_file.close()

    def input_word(self):

        self.count = 0
        self.findword = input("Enter the word:\n")
        pattern = re.compile(self.findword, re.I | re.M)
        hand = open(r'sample.txt')
        handle = hand.read()
        self.wordfinder = re.findall(pattern, handle)
        self.file_list = handle.split()

    def creative_file(self):


        create_file = self.findword + '.txt'
        file_gen = open(create_file, 'w+')
        for i in range(len(self.file_list)):
            wordfound = re.match(self.findword, self.file_list[i], re.I | re.M)
            if wordfound:
                self.count += 1

                sent = (self.file_list[i-1] + ' ' + self.file_list[i] + ' ' + self.file_list[i+1])
                file_gen.write(str(sent) + '\n')
                file_gen.write(str(self.count) + ' :')

        file_gen.write('word repeated:' + str(len(self.wordfinder)) + '\n')  #pep8 done w/o comments


obj=special_character()
obj.input_word()
obj.creative_file()
