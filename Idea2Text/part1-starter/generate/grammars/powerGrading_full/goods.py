from ideaToText import Decision

class Goods(Decision):
    def registerChoices(self):
        self.addChoice('answerStyle',{
            '{GoodsShort}':4,
            '{GoodsFull}':2,
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('answerStyle')