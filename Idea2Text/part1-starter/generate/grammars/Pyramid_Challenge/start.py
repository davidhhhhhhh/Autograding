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
            'offset_extra': 1,
            'perfect': 1,
            'perfect_extra': 1,
            'brick_wall': 1,
        })

        # Choices have two parts, an identifier and a dictionary
        # which maps possible outcomes to their relative likelihood

    def updateRubric(self):
        pass

    def render(self):
        # Mapping choices to their corresponding expanded code
        choice_mapping = {
            'hello_world': 'HelloWorld',
            'single_row': 'SingleRow',
            'diagonal': 'Diagonal',
            'two_row': 'TwoRows',
            'rectangle': 'Rectangle',
            'parallelogram': 'Parallelogram',
            'right_triangle': 'RightTriangle',
            'column_structure': 'ColumnStructure',
            'scalene_triangle': 'ScaleneTriangle',
            'pyramid_like': 'PyramidLike',
            'offset_pyramid': 'OffsetPyramid',
            'perfect': 'Perfect',
            'brick_wall': 'BrickWall',
            'offset_extra': 'OffsetExtra',
            'perfect_extra': 'PerfectExtra'
        }

        strategy = self.getChoice('strategies')
        out_codes = self.expand(choice_mapping[strategy])
        return out_codes
