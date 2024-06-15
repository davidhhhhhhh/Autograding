from ideaToText import Decision

class PoliticsShortToDo(Decision):
    def registerChoices(self):
        self.addChoice('prose',{
            'To {PoliticsPositiveVerb} {PoliticsPosNoun}':4,
            'To {PoliticsNegativeVerb} {PoliticsNegNoun}':2
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('prose')