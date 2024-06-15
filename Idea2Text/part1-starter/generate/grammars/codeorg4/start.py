
from ideaToText import Decision
from ideaToText import generatorUtils as gu

# "Start" is a special decision which is invoked by the Sampler
# to generate a single sample.
class Start(Decision):

    def registerChoices(self):
        pass

    def updateRubric(self):
        pass

    def render(self):
        # currently this grammar always returns the solution
        return '''
            For(15, 300, 15) {{
               Repeat(4) {{
                  Move(Counter)
                  TurnLeft(90)
               }}
            }}
            '''