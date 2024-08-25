from ideaToText import Decision


class BrickSize(Decision):
    def registerChoices(self):
        self.addChoice('correctness', {
            '{CorrectSize}': 20,
            '{FalseSize}': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('correctness')


class CorrectSize(Decision):
    def registerChoices(self):
        self.addChoice('size_params', {
            '''int brick_width = 30;
               int brick_height = 10;
               int BRICK_WIDTH = brick_width;
               int BRICK_HEIGHT = brick_height;''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('size_params')


class FalseSize(Decision):
    def registerChoices(self):
        self.addChoice('size_params', {
            '''int brick_width = 30;
               int brick_height = 30;
               int BRICK_WIDTH = brick_width;
               int BRICK_HEIGHT = brick_height;''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('size_params')