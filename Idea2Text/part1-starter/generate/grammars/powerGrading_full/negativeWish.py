from ideaToText import Decision

class NegativeWish(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'did not want':1,
            "were escaping":1,
            'dislike':1,
            'hate':1,
            'do not like':1,
        })

    def render(self):
    	return self.getChoice(self.getName())