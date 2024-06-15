from ideaToText import Decision

class TaxShort(Decision):
    def registerChoices(self):
        self.addChoice('Grammar',{
            'To {TaxVerb} {TaxNoun}':4,
            '{TaxShortPhrase}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('Grammar')