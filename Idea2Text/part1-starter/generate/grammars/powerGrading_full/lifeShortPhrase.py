from ideaToText import Decision

class LifeShortPhrase(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'for a better life':5,
            "For a new life":2,
            'for life':1,
        })

    def render(self):
    	return self.getChoice(self.getName())