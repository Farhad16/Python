class Text(str):
    def duplicate(self):
        print(self+self)


class TextAppendList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)


text = TextAppendList()
text.append("Python")
