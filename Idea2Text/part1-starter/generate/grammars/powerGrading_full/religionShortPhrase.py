from ideaToText import Decision

class ReligionShortPhrase(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'Religious freedom':4,
            "Freedom of religion":2,
            'freedom of practicing religion':1,
            'religious liberty':1,
            'religious freedom':2,
            'freedom':1
        })

    def render(self):
    	return self.getChoice(self.getName())