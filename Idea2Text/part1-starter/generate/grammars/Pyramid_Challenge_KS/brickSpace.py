from ideaToText import Decision


class BrickSingleRowSpacing(Decision):
    def registerChoices(self):
        self.addChoice('singleRowXSpace', {
            '''// Correct brick space
                double x = start_X + i * BRICK_WIDTH; ''': 10,
            '''// Incorrect brick space, overlap
                double x = start_X + i * 15; ''': 1,
            '''// Incorrect brick space, extra space
                double x = start_X + i * (15 + brick_width); ''': 1,
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('singleRowXSpace')


class BrickMultiRowSpacing(Decision):
    def registerChoices(self):
        self.addChoice('multiRowXSpace', {
            '''// Correct brick space
                double x = rowX + j * BRICK_WIDTH; ''': 10,

            '''// Incorrect brick space, overlap
                double x = rowX + j * 15; ''': 1,

            '''// Incorrect brick space, extra space
                double x = rowX + j * (15 + BRICK_WIDTH); ''': 1,
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('multiRowXSpace')


class BrickYSpacing(Decision):
    def registerChoices(self):
        self.addChoice('YSpace', {
            '''// Correct brick space in Y direction
                double rowY = start_Y - i * BRICK_HEIGHT; ''': 10,

            '''// Incorrect brick space, overlap
                double rowY = start_Y - i * 15; ''': 1,

            '''// Incorrect brick space, extra space
                double rowY = start_Y - i * (BRICK_HEIGHT + 15);; ''': 1,
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('YSpace')