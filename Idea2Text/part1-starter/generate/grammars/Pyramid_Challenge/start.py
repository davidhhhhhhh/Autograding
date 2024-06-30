from ideaToText import Decision

# "Start" is a special decision which is invoked by the Sampler
# to generate a single sample.
class Start(Decision):

    def registerChoices(self):
        # This sentence creator for Q13 in power grading dataset.
        # It starts with two choices:
        # One choice is correct, including political, religious, or economic reason. The other
        # choice is incorrect, like taxation, exploration, or physical goods.
        self.addChoice('strategies', {
            'hello_world':1,
            'single_row':1,
            'diagonal': 1,
            'two_row': 1,
            'rectangle': 1,
            'parallelogram': 1,
            'right_triangle': 1,
            'column_structure': 1,
            'scalene_triangle': 1,
            'pyramid_like': 1,
            'offset_pyramid': 1,
            'perfect': 1,
            'brick_wall': 1,
        })

        # Choices have two parts, an identifier and a dictionary
        # which maps possible outcomes to their relative likelihood

    def updateRubric(self):
        pass

    def render(self):
        # Mapping choices to their corresponding expanded code
        choice_mapping = {
            'hello_world': 'Hello_world',
            'single_row': 'Single_row',
            'diagonal': 'Diagonal',
            'two_row': 'Two_row',
            'rectangle': 'Rectangle',
            'parallelogram': 'Parallelogram',
            'right_triangle': 'Right_triangle',
            'column_structure': 'Column_structure',
            'scalene_triangle': 'Scalene_triangle',
            'pyramid_like': 'Pyramid_like',
            'offset_pyramid': 'Offset_pyramid',
            'perfect': 'Perfect',
            'brick_wall': 'Brick_wall'
        }

        strategy = self.getChoice('strategies')
        out_codes = self.expand(choice_mapping[strategy])
        return out_codes
