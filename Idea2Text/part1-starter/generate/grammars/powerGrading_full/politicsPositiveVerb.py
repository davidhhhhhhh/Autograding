from ideaToText import Decision

class PoliticsPositiveVerb(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'get':2,
            "obtain":1,
            'have':2,
            'acquire':2,
            'gain':1,
            'pursue':1
        })

    def render(self):
    	return self.getChoice(self.getName())