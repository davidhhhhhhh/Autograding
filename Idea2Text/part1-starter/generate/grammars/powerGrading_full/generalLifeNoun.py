from ideaToText import Decision

class GeneralLifeNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'a new life':2,
            "a good life":1,
            'a better future':1
        })

    def render(self):
    	return self.getChoice(self.getName())