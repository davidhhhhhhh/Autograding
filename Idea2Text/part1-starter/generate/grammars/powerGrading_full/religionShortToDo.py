from ideaToText import Decision

class ReligionShortToDo(Decision):
    def registerChoices(self):
        self.addChoice('ReligionShort',{
            'To {ReligionPositiveVerb} {ReligionPosNoun}':4,
            'To {ReligionNegativeVerb} {ReligionNegNoun}':2
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('ReligionShort')