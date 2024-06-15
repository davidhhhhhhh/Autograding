from ideaToText import Decision

class ReligionNegNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'religious persecutions':4,
            "religious oppression":2,
            'persecutions by other religions':1,
        })

    def render(self):
    	return self.getChoice(self.getName())