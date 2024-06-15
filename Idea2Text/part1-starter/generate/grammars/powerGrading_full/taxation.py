from ideaToText import Decision

class Taxation(Decision):
    def registerChoices(self):
        self.addChoice('answerStyle',{
            '{TaxShort}':4,
            '{TaxFull}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('answerStyle')