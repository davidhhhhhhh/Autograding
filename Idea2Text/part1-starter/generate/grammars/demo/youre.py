from ideaToText import Decision


class Youre(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(), {
            'you are': 1,
            "you're": 1,
        })

    def render(self):
        y = self.getChoice(self.getName())
        a = "1,2,3"
        return f'String input = "{a}";'
