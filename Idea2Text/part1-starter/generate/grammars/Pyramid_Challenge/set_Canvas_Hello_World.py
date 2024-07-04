from ideaToText import Decision


class Set_Canvas_Hello_World(Decision):
    def registerChoices(self):
        self.addChoice('canvasSetting', {
            '{Off_Canvas}': 1,
            '{Right_Canvas}': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('canvasSetting')
