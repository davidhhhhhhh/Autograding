from ideaToText import Decision

class PositiveWish(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'wanted to have':1,
            "are looking for":2,
            'want':1,
            'were seeking':2,
            'were pursuing':1,
            'would like to have':1
        })

    def render(self):
    	return self.getChoice(self.getName())