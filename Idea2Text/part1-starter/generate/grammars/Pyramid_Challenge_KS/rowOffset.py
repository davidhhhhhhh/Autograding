from ideaToText import Decision


class RowOffset(Decision):
    def registerChoices(self):
        self.addChoice('offsetCorrectness', {
            ''' // Correct Offset
                int rowWidth = nBricks * BRICK_WIDTH;
                double rowX = (canvas.getWidth() - rowWidth) / 2.0;
               ''': 5,

            ''' // Incorrect offset
                {IncorrectOffset}
               ''': 5
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('offsetCorrectness')


class IncorrectOffset(Decision):
    def registerChoices(self):
        self.addChoice('incorrectOffsetTypes', {
            ''' // No offset 
                double rowX = start_X;
               ''': 5,

            ''' // Constant value of offset, correct direction
                double rowX = start_X + i * 15;
               ''': 4,

            ''' // Constant value of offset, incorrect direction
                double rowX = start_X - i * 15;
                ''': 3,
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('incorrectOffsetTypes')

