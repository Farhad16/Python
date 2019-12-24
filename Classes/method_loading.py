class Concat:
    def add(self, datatype, *arg):
        if datatype == 'int':
            ans = 0
        elif datatype == 'str':
            ans = ''

        for x in arg:
            ans = ans + x
        print(ans)


a = Concat()
a.add('int', 10, 5, 20)
a.add('str', "Md", " ", "Farhad", " ", "Hossain")
