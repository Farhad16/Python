class Text(str):
    def draw(self):
        print(self+self)


text = Text("Python")
print(text.lower())
text.draw()