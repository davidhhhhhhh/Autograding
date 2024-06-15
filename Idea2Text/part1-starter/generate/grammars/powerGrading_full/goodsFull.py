from ideaToText import Decision

class GoodsFull(Decision):
    def registerChoices(self):
        self.addChoice('FullGrammar',{
            '{Subject} {PositiveWish} {GoodsNoun}':4,
            '{Subject} {NegativeWish} the lack of {GoodsNoun}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('FullGrammar')