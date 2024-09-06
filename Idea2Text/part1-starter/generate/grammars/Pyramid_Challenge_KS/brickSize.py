from ideaToText import Decision


class BrickSize(Decision):
    def registerChoices(self):
        self.addChoice('SizeCorrectness', {
            'CorrectSize': 20,
            'FalseSize': 1
        })

    def render(self):
        choice_mapping = {'CorrectSize': '''int brick_width = 30;
               int brick_height = 10;
               int BRICK_WIDTH = brick_width;
               int BRICK_HEIGHT = brick_height;''',

                          'FalseSize': '''//
               int brick_width = 30 + random.nextInt(20);
               int brick_height = 30 - random.nextInt(20);
               int BRICK_WIDTH = brick_width;
               int BRICK_HEIGHT = brick_height;'''}

        choice = self.getChoice('SizeCorrectness')
        output = choice_mapping[choice]
        return output
