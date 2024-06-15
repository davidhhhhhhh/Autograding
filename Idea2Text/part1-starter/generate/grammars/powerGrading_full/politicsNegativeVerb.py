from ideaToText import Decision

class PoliticsNegativeVerb(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'escape':2,
            "evade":1,
            'run from':1,
        })

    def render(self):
    	return self.getChoice(self.getName())