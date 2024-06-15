from ideaToText import Decision

class ExploreShortPhrase(Decision):
    def registerChoices(self):
        self.addChoice(self.getName(),{
            'For exploration':4,
            'Exploring the new world':2,
            'To conquer the new world':1,
        })

    def render(self):
    	return self.getChoice(self.getName())