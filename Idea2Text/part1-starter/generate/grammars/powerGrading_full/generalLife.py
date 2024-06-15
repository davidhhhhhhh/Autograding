from ideaToText import Decision

class GeneralLife(Decision):
    def registerChoices(self):
        self.addChoice('answerStyle',{
            '{LifeShort}':4,
            '{LifeFull}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('answerStyle')