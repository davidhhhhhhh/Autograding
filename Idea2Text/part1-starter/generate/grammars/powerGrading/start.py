from ideaToText import Decision

# "Start" is a special decision which is invoked by the Sampler
# to generate a single sample.
class Start(Decision):

    def registerChoices(self):
        # This sentence creator for Q13 in power grading dataset.
        # It starts with two choices:
        # One choice is correct, including political, religious, or economic reason. The other
        # choice is incorrect, like taxation, exploration, or physical goods.
        self.addChoice('correctness', {
            'correct':6,
            'incorrect':1
        })

        # Choices have two parts, an identifier and a dictionary
        # which maps possible outcomes to their relative likelihood
        self.addChoice('punct', {
            '':10,
            '.':5,
            '!':1
        })

    def updateRubric(self):
        pass

    def render(self):
        # once choices have been made, you now have to turn
        # those ideas into text
        punctuation = self.getChoice('punct')
        cor = self.getChoice('correctness')
        if cor == 'correct':
            phrase = self.expand('Correct')
        if cor == 'incorrect':
            phrase = self.expand('Incorrect')
        return phrase + punctuation
