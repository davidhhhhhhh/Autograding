from ideaToText import Decision

class Exploration(Decision):
    def registerChoices(self):
        self.addChoice('answerStyle',{
            '{ExplorShort}':4,
            '{ExplorFull}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('answerStyle')