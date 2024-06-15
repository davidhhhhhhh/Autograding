from ideaToText import Decision

class ExploreVerb(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'explore':2,
            "conquer":1,
        })

    def render(self):
    	return self.getChoice(self.getName())