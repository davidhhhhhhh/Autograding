from ideaToText import Decision

class Correct(Decision):
    def registerChoices(self):
        self.addChoice('correctTopics',{
            '{Subject} {PositiveVerb} political {Liberty}':1,
            '{Subject} {PositiveVerb} religious {Liberty}':1,
            '{Subject} {PositiveVerb} economic opportunity': 1,
            '{Subject} {NegativeVerb} religious {Prosecution}': 1,
            '{Subject} {NegativeVerb} political {Prosecution}': 1,
            '{Subject} {NegativeVerb} economic hardship': 1,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('correctTopics')