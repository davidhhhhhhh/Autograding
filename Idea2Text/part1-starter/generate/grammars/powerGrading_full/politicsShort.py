from ideaToText import Decision

class PoliticsShort(Decision):
    def registerChoices(self):
        self.addChoice('Grammar',{
            '{PoliticsShortToDo}':4,
            '{PoliticsShortPhrase}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('Grammar')