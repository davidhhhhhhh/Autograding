from ideaToText import Decision

class Incorrect(Decision):
    def registerChoices(self):
        self.addChoice('falsePhrase',{
            '{Subject} {PositiveVerb} {Goods}':1,
            '{Subject} {PositiveVerb} explorations of the new world':1,
            '{Subject} {PositiveVerb} {GeneralLife}': 1,
            '{Subject} {NegativeVerb} {Politics}': 1,
            '{Subject} {NegativeVerb} taxation': 1,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('falsePhrase')