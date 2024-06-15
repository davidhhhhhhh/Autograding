from ideaToText import Decision

class EconNegNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'economic hardships':4,
            "undesired economic situation":2,
            'hard economic status':1,
        })

    def render(self):
    	return self.getChoice(self.getName())