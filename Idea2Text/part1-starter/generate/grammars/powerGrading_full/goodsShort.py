from ideaToText import Decision

class GoodsShort(Decision):
    def registerChoices(self):
        self.addChoice('Grammar',{
            '{GoodsShortToDo}':4,
            '{GoodsShortPhrase}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('Grammar')