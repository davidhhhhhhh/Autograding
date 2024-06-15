from ideaToText import Decision

class ExploreNoun(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'the new world':5,
            "Americas":1,
            'new land':2,
        })

    def render(self):
    	return self.getChoice(self.getName())