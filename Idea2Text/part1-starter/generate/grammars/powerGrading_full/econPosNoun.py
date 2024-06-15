from ideaToText import Decision

class EconPosNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'economic opportunities':4,
            'more revenues':2,
            'jobs':1
        })

    def render(self):
    	return self.getChoice(self.getName())