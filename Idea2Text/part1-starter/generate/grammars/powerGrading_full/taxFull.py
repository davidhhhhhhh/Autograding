from ideaToText import Decision

class TaxFull(Decision):
    def registerChoices(self):
        self.addChoice('FullGrammar',{
            '{Subject} {PositiveWish} {TaxPosNoun}':2,
            '{Subject} {NegativeWish} {TaxNoun}':4,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('FullGrammar')