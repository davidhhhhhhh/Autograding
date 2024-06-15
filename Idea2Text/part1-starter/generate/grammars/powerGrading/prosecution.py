from ideaToText import Decision

class Prosecution(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'prosecutions':4,
            "prosecution":1,
            'oppressions':2,
            'oppression':1
        })

    def render(self):
    	return self.getChoice(self.getName())