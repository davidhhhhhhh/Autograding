from ideaToText import Decision

class LifeNegNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'their current life':4,
            "their lives":2,
            'the current life':1,
        })

    def render(self):
    	return self.getChoice(self.getName())