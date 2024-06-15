from ideaToText import Decision

class LifeShort(Decision):
    def registerChoices(self):
        self.addChoice('Grammar',{
            'To {LifeVerb} {GeneralLifeNoun}':4,
            '{LifeShortPhrase}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('Grammar')