import re

xas = int(input("enter the no. for words: \n"))


class special_character():
    def __init__(self):

        self.string = open('input.txt').read()  # opening input file
        self.new_string = re.sub(r'[^a-zA-Z\n]', ' ', self.string)
        # regex for replacing all non alphabetic characters with whitespace
        self.text_file = open("sample.txt", "w")
        # creating and writing the new string in sample file
        self.n = self.text_file.write(self.new_string)
        self.text_file.close()  # closing the sample file

    def input_word(self):

        self.count = 0
        self.findword = input("Enter the word:\n")
        # input for the word to be search
        pattern = re.compile(self.findword, re.I | re.M)
        # pattern for the word making it insensitive of the case
        hand = open(r'sample.txt')
        handle = hand.read()
        self.wordfinder = re.findall(pattern, handle)
        self.file_list = handle.split()  # spliting the handle

    def creative_file(self):
        create_file = self.findword + '.txt'
        # creating the file of same name of the search word and writing
        file_gen = open(create_file, 'w+')
        for i in range(len(self.file_list)):
            wordfound = re.match(self.findword, self.file_list[i], re.I | re.M)
            if wordfound:
                self.count += 1

                sent = (self.file_list[i-1] + ' ' + self.file_list[i] + ' ' +
                        self.file_list[i+1])
                # for appending one word before and after the input search word
                file_gen.write(str(sent) + '\n')
                file_gen.write(str(self.count) + ' :')

        file_gen.write('word repeated:' + str(len(self.wordfinder)) + '\n')
for v in range(xas):
        obj = special_character()
        obj.input_word()
        obj.creative_file()
