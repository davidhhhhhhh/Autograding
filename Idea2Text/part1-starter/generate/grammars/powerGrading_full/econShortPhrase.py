from ideaToText import Decision

class EconShortPhrase(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'Economic opportunities':4,
            'economic potentials':1,
            'economic opportunities':2,
        })

    def render(self):
    	return self.getChoice(self.getName())