from ideaToText import Decision

class ReligionPosNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'religious freedom':4,
            "freedom of religion":2,
            'freedom of practicing religion':1,
            'religious liberty':1,
        })

    def render(self):
    	return self.getChoice(self.getName())