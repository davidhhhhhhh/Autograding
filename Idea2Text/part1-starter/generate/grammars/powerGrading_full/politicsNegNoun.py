from ideaToText import Decision

class PoliticsNegNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'political persecutions':4,
            "political oppression":2,
            'persecutions by monarchies':1,
        })

    def render(self):
    	return self.getChoice(self.getName())