from ideaToText import Decision

class TaxNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'taxation':4,
            "taxes":2,
            'British taxes':1,
        })

    def render(self):
    	return self.getChoice(self.getName())