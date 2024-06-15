from ideaToText import Decision

class EconFull(Decision):
    def registerChoices(self):
        self.addChoice('FullGrammar',{
            '{Subject} {PositiveWish} {EconPosNoun}':4,
            '{Subject} {NegativeWish} {EconNegNoun}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('FullGrammar')