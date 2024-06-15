from ideaToText import Decision

class ReligionFull(Decision):
    def registerChoices(self):
        self.addChoice('ReligionFullGrammar',{
            '{Subject} {PositiveWish} {ReligionPosNoun}':4,
            '{Subject} {NegativeWish} {ReligionNegNoun}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('ReligionFullGrammar')