from ideaToText import Decision


class SetColorFilled(Decision):
    def registerChoices(self):
        self.addChoice('BrickStyle', {
            'NoColorNotFilled': 60,
            'ColorNotFilled': 3,
            'NoColorFilled': 2,
            'ColorFilled': 1
        })

    def render(self):
        choice_mapping = {'NoColorNotFilled': '''// Black Color, Not filled''',

                          'ColorNotFilled': ''' // Color but not filled
                          {BrickColor} ''',

                          'NoColorFilled': '''// Black Color but filled
                          brick.setFilled(true);''',

                          'ColorFilled': '''// Color and filled
                          {BrickColor}
                          brick.setFilled(true);'''}

        choice = self.getChoice('BrickStyle')
        output = choice_mapping[choice]
        return output


class BrickColor(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 1,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.RED': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
        })

    def render(self):
        color = self.getChoice('brickColor')
        return '''
        brick.setColor({});'''.format(color)
