from ideaToText import Decision

class ExplorFull(Decision):
    def registerChoices(self):
        self.addChoice('FullGrammar',{
            '{Subject} {ExploreWish} {ExploreNoun}':4,
            '{Subject} {ExploreForVerb} {ExploreNoun}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('FullGrammar')