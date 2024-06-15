from ideaToText import Decision

class EconNegativeVerb(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'escape':2,
            'run from their':1,
            'change their': 2
        })

    def render(self):
    	return self.getChoice(self.getName())