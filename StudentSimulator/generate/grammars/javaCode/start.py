from StudentSimulator.ideaToText import Decision

# "Start" is a special decision which is invoked by the Sampler
# to generate a single sample.
class Start(Decision):

    def registerChoices(self):
        # This sentence creator for Q13 in power grading dataset.
        # It starts with two choices:
        # One choice is correct, including political, religious, or economic reason. The other
        # choice is incorrect, like taxation, exploration, or physical goods.
        self.addChoice('correctness', {
            'correct': 5,
            'false': 1
        })

        # Choices have two parts, an identifier and a dictionary
        # which maps possible outcomes to their relative likelihood

    def updateRubric(self):
        pass

    def render(self):
        # Mapping choices to their corresponding expanded code
        choice_mapping = {
            'correct': 'Correct',
            'false': 'Incorrect'
        }

        strategy = self.getChoice('correctness')
        out_codes = self.expand(choice_mapping[strategy])
        return out_codes
