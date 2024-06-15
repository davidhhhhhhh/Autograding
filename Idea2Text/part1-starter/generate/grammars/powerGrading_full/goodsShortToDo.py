from ideaToText import Decision

class GoodsShortToDo(Decision):
    def registerChoices(self):
        self.addChoice('prose',{
            'To {GoodsPositiveVerb} {GoodsNoun}':4,
            'For {GoodsForVerb} {GoodsNoun}':2
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('prose')