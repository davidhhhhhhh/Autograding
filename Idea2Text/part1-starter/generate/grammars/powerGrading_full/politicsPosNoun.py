from ideaToText import Decision

class PoliticsPosNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'political freedom':4,
            'political liberty':2,
        })

    def render(self):
    	return self.getChoice(self.getName())