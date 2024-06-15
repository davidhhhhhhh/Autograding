from ideaToText import Decision

class Correct(Decision):
    def registerChoices(self):
        self.addChoice('correctTopics',{
            '{Religion}':4,
            '{Politics}':2,
            '{EconOpp}': 1,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('correctTopics')