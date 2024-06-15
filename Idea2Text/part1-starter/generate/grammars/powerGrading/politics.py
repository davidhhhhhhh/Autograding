from ideaToText import Decision

class Politics(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'King George':1,
            "Britain":2,
            'religion':1,
            'England':2,
            'the monarchy':1
        })

    def render(self):
    	return self.getChoice(self.getName())