class Write:
    def __init__(self, filename1, filename2):
        self.filename1 = filename1
        self.filename2 = filename2

    def rewrite(self, filename1, filename2):
        with open(self.filename1, 'r')as file:
            list1 = [string.replace('\n', '') for string in file.readlines()]
        with open(self.filename2, 'r')as file:
            list2 = [string.replace('\n', '') for string in file.readlines()]
        with open(self.filename2, 'a')as file:
            for element in list1:
                if element in list2:
                    continue
                else:
                    file.write(element + '\n')
        with open(self.filename1, 'a')as file:
            for element in list2:
                if element in list1:
                    continue
                else:
                    file.write(element + '\n')
        return list1, list2
