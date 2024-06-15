from ideaToText import Decision

class GoodsShortPhrase(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'for gold':5,
            "for timber":1,
            'for natural resources':2,
            'for food':2,
            'for noble titles':1
        })

    def render(self):
    	return self.getChoice(self.getName())