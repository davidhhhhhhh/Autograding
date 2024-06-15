from ideaToText import Decision

class Politics(Decision):
    def registerChoices(self):
        self.addChoice('answerStyle',{
            '{PoliticsShort}':4,
            '{PoliticsFull}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('answerStyle')