from ideaToText import Decision

class TaxPosNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'no taxation':4,
            "lower taxes":2,
            'freedom from taxation':1,
            'exemptions from taxes':1,
        })

    def render(self):
    	return self.getChoice(self.getName())