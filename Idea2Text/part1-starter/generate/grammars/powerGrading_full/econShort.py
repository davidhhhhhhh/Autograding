from ideaToText import Decision

class EconShort(Decision):
    def registerChoices(self):
        self.addChoice('Grammar',{
            '{EconShortToDo}':4,
            '{EconShortPhrase}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('Grammar')