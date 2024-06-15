from ideaToText import Decision

class Liberty(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'liberty':1,
            "freedom":1,
        })

    def render(self):
    	return self.getChoice(self.getName())