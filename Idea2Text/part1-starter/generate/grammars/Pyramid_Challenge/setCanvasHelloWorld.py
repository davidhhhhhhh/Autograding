from ideaToText import Decision

class SetCanvasHelloWorld(Decision):
    def registerChoices(self):
        self.addChoice('canvasSetting', {
            '{OffCanvas}': 1,
            '{RightCanvas}': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand it
        return self.getChoice('canvasSetting')