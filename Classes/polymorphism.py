class UIControl:
    def draw(self):
        pass


class TextControl(UIControl):
    def draw(self):
        print("Text Control")


class DropDownControl(UIControl):
    def draw(self):
        print("DropDownControl")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownControl()
text = TextControl()
draw([text, ddl])
