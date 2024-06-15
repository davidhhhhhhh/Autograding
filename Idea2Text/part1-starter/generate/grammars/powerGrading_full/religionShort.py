from ideaToText import Decision

class ReligionShort(Decision):
    def registerChoices(self):
        self.addChoice('ReligionShortGrammar',{
            '{ReligionShortToDo}':4,
            '{ReligionShortPhrase}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('ReligionShortGrammar')