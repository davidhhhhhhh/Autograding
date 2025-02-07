from StudentSimulator.ideaToText import Decision


class BrickSingleRowSpacing(Decision):
    def registerChoices(self):
        self.addChoice('singleRowXSpace', {
            'RightBrickSpace': 20,
            'OverlapBrickSpace': 1,
            'ExtraBrickSpace': 1,
        })

    def render(self):
        choice_mapping = {'RightBrickSpace': '''// Correct brick space
                double x = start_X + i * BRICK_WIDTH; ''',

                          'OverlapBrickSpace': '''// Incorrect brick space, overlap
                //
                double x = start_X + i * (1 + random.nextInt(28)); ''',

                          'ExtraBrickSpace': '''// Incorrect brick space, extra space
                //
                double x = start_X + i * (31 + random.nextInt(30)); '''}

        choice = self.getChoice('singleRowXSpace')
        output = choice_mapping[choice]
        return output


class BrickMultiRowSpacing(Decision):
    def registerChoices(self):
        self.addChoice('multiRowXSpace', {
            'RightBrickSpace': 20,
            'OverlapBrickSpace': 1,
            'ExtraBrickSpace': 1,
        })

    def render(self):
        choice_mapping = {'RightBrickSpace': '''// Correct brick space
                double x = rowX + j * BRICK_WIDTH; ''',

                          'OverlapBrickSpace': '''// Incorrect brick space, overlap
                //
                double x = rowX + j * (1 + random.nextInt(28)); ''',

                          'ExtraBrickSpace': '''// Incorrect brick space, extra space
                //
                double x = rowX + j * (31 + random.nextInt(30)); '''}

        choice = self.getChoice('multiRowXSpace')
        output = choice_mapping[choice]
        return output


class BrickYSpacing(Decision):
    def registerChoices(self):
        self.addChoice('YSpace', {
            'RightYSpace': 20,

            'OverlapYSpace': 1,

            'ExtraYSpace': 1,
        })

    def render(self):
        choice_mapping = {'RightYSpace': '''// Correct brick space in Y direction
                double rowY = start_Y - i * BRICK_HEIGHT; ''',

                          'OverlapYSpace': '''// Incorrect brick space, overlap
                //
                double rowY = start_Y - i * (1 + random.nextInt(8)); ''',

                          'ExtraYSpace': '''// Incorrect brick space, extra space
                //
                double rowY = start_Y - i * (BRICK_HEIGHT + 1 + random.nextInt(10)); '''}

        choice = self.getChoice('YSpace')
        output = choice_mapping[choice]
        return output
