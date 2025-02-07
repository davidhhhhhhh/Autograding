from StudentSimulator.ideaToText import Decision


class RowOffset(Decision):
    def registerChoices(self):
        self.addChoice('offsetCorrectness', {
            'RightOffset': 5,

            'FalseOffset': 2
        })

    def render(self):
        choice_mapping = {'RightOffset': ''' // Correct Offset
                int rowWidth = nBricks * BRICK_WIDTH;
                double rowX = (canvas.getWidth() - rowWidth) / 2.0;
               ''',

                          'FalseOffset': '''{IncorrectOffset}
               '''}

        choice = self.getChoice('offsetCorrectness')
        output = choice_mapping[choice]
        return output


class IncorrectOffset(Decision):
    def registerChoices(self):
        self.addChoice('FalseOffsetTypes', {
            'NoOffset': 10,

            'RamOffsetRightDir': 8,

            'FullOffsetRightDir': 3,

            'RamOffsetFalseDir': 1,
        })

    def render(self):
        choice_mapping = {'NoOffset': ''' // No offset 
                double rowX = start_X;
               ''',

                          'RamOffsetRightDir': ''' // Constant value of offset, correct direction
                //
                double rowX = start_X + i * random.nextInt(30);
               ''',
                          'FullOffsetRightDir': ''' // Constant value of offset, incorrect direction
                //
                double rowX = start_X + i * brick_width;
                ''',
                          'RamOffsetFalseDir': ''' // Constant value of offset, incorrect direction
                //
                double rowX = start_X - i * random.nextInt(30);
                '''}

        choice = self.getChoice('FalseOffsetTypes')
        output = choice_mapping[choice]
        return output

