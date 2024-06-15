from ideaToText import Decision

class PoliticsShortPhrase(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'Political freedom':4,
            'political liberty':1,
            'political freedom':2,
        })

    def render(self):
    	return self.getChoice(self.getName())