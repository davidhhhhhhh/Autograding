from ideaToText import Decision

class ExploreForVerb(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'wish exploring':1,
            'were looking forward to explore':2,
            'were desiring to explore':1,
        })

    def render(self):
    	return self.getChoice(self.getName())