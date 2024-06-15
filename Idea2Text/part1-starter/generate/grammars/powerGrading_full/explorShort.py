from ideaToText import Decision

class ExplorShort(Decision):
    def registerChoices(self):
        self.addChoice('Grammar',{
            'To {ExploreVerb} {ExploreNoun}':4,
            '{ExploreShortPhrase}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('Grammar')