from ideaToText import Decision

class Incorrect(Decision):
    def registerChoices(self):
        self.addChoice('falsePhrase',{
            '{Goods}':1,
            '{Exploration}':1,
            '{GeneralLife}': 1,
            '{Taxation}': 1,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('falsePhrase')