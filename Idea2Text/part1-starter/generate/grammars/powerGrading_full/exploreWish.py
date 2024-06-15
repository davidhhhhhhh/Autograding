from ideaToText import Decision

class ExploreWish(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'wanted to explore':1,
            'were eager to explore':2,
            'have desires to explore':1,
            'would like to explore':1
        })

    def render(self):
    	return self.getChoice(self.getName())