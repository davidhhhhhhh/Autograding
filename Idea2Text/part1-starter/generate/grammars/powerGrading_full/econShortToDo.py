from ideaToText import Decision

class EconShortToDo(Decision):
    def registerChoices(self):
        self.addChoice('prose',{
            'To {EconPositiveVerb} {EconPosNoun}':4,
            'To {EconNegativeVerb} {EconNegNoun}':2
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('prose')