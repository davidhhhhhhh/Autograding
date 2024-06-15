from ideaToText import Decision

class Subject(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'They':1,
            "Those colonists":1,
            'Colonists': 1,
            'Because they': 1
        })

    def render(self):
    	return self.getChoice(self.getName())