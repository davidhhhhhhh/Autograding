from ideaToText import Decision

class TaxShortPhrase(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'For escaping taxes':4,
            'Because of high taxes in britain':2,
            'No taxation without representation':1,
        })

    def render(self):
    	return self.getChoice(self.getName())