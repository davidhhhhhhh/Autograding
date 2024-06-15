from ideaToText import Decision

class TaxVerb(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'avoid':2,
            "evade":1,
            'run from':1,
            'escape from':1
        })

    def render(self):
    	return self.getChoice(self.getName())