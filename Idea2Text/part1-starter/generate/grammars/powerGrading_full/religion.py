from ideaToText import Decision

class Religion(Decision):
    def registerChoices(self):
        self.addChoice('answerStyle',{
            '{ReligionShort}':4,
            '{ReligionFull}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('answerStyle')