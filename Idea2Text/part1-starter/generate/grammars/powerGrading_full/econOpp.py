from ideaToText import Decision

class EconOpp(Decision):
    def registerChoices(self):
        self.addChoice('answerStyle',{
            '{EconShort}':4,
            '{EconFull}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('answerStyle')