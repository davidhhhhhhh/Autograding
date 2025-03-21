from StudentSimulator.ideaToText import Decision


class AddColorHelloWorld(Decision):
    def registerChoices(self):
        self.addChoice('rectangleColor', {
            '//no color': 60,
            'rect.setFilled(false); rect.setColor(Color.RED);': 1,
            'rect.setFilled(true); rect.setColor(Color.BLUE);': 1,
            'rect.setFilled(false); rect.setColor(Color.GREEN);': 1,
            'rect.setFilled(true); rect.setColor(Color.YELLOW);': 1,
            'rect.setFilled(false); rect.setColor(Color.ORANGE);': 1,
            'rect.setFilled(true); rect.setColor(Color.MAGENTA);': 1,
        })

    def render(self):
        return self.getChoice('rectangleColor')