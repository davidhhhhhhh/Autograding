from ideaToText import Decision

class GoodsForVerb(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'getting':2,
            "obtaining":1,
            'having':2,
            'acquiring':2,
            'gaining':1,
            'pursuing':1
        })

    def render(self):
    	return self.getChoice(self.getName())