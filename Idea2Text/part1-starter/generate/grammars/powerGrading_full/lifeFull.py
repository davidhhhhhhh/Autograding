from ideaToText import Decision

class LifeFull(Decision):
    def registerChoices(self):
        self.addChoice('FullGrammar',{
            '{Subject} {PositiveWish} {GeneralLifeNoun}':4,
            '{Subject} {NegativeWish} {LifeNegNoun}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('FullGrammar')