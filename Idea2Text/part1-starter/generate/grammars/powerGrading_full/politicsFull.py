from ideaToText import Decision

class PoliticsFull(Decision):
    def registerChoices(self):
        self.addChoice('FullGrammar',{
            '{Subject} {PositiveWish} {PoliticsPosNoun}':4,
            '{Subject} {NegativeWish} {PoliticsNoun}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('FullGrammar')