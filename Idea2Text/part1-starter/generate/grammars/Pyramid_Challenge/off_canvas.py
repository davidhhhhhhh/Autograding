from ideaToText import Decision


class Off_Canvas(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(), {
            'setSize(600,400);': 4,
            "setSize(800,400)": 2,
            "setSize(400,400)": 1,
        })

    def render(self):
        return self.getChoice(self.getName())
