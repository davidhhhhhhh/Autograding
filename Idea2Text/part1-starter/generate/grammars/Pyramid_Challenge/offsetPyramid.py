from ideaToText import Decision

class OffsetPyramid(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawOffsetPyramidStructure extends GraphicsProgram {
    public void run() {
        // Set canvas size
        {Set_Canvas_Size_Pyramid}

        // Initialize structure parameters
        {Initialize_Structure_Parameters_Pyramid}

        // Optionally add centering assist lines
        {Add_Centering_Assist_Lines}

        // Draw a pyramid
        for (int i = 0; i < BRICKS_IN_BASE; i++) {
            // Calculate row variables
            int nBricks = BRICKS_IN_BASE - i;
            int rowWidth = nBricks * BRICK_WIDTH;
            double rowY = OFFSET_Y + getHeight() - (i + 1) * BRICK_HEIGHT;
            double rowX = OFFSET_X + (getWidth() - rowWidth) / 2.0;

            // Draw a single row
            for (int j = 0; j < nBricks; j++) {
                // Add a single brick
                double x = rowX + j * BRICK_WIDTH;
                GRect brick = new GRect(x, rowY, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {Set_Brick_Filled}

                brick.setColor({Brick_Color_Pyramid});
                add(brick);
            }
        }
    }

    public static void main(String[] args) {
        // Start the GraphicsProgram
        new DrawOffsetPyramidStructure().start(args);
    }
}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class Set_Canvas_Size_Pyramid(Decision):
    def registerChoices(self):
        self.addChoice('canvasWidth', {
            '600': 1
        })
        self.addChoice('canvasHeight', {
            '400': 1
        })

    def render(self):
        return 'setSize({}, {});'.format(self.getChoice('canvasWidth'), self.getChoice('canvasHeight'))


class Initialize_Structure_Parameters_Pyramid(Decision):
    def registerChoices(self):
        self.addChoice('bricksInBase', {
            '14': 5,
            '13': 4,
            '12': 3,
            '11': 2,
            '10': 1
        })
        self.addChoice('brickWidth', {
            '40': 4,
            '80': 1
        })
        self.addChoice('brickHeight', {
            '20': 4,
            '40': 1
        })
        self.addChoice('offsetX', {
            '50': 2,
            '-50': 1,
            '-100': 1,
            '100': 1
        })
        self.addChoice('offsetY', {
            '50': 1,
            '-50': 1,
            '-100': 1,
            '100': 1
        })

    def render(self):
        bricksInBase = int(self.getChoice('bricksInBase'))
        brickWidth = self.getChoice('brickWidth')
        brickHeight = self.getChoice('brickHeight')
        offsetX = self.getChoice('offsetX')
        offsetY = self.getChoice('offsetY')

        return '\n'.join([
            'int BRICKS_IN_BASE = {};'.format(bricksInBase),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight),
            'int OFFSET_X = {};'.format(offsetX),
            'int OFFSET_Y = {};'.format(offsetY)
        ])


class Add_Centering_Assist_Lines(Decision):
    def registerChoices(self):
        self.addChoice('centeringAssistLines', {
            'add(new GLine(getWidth() / 2, 0, getWidth() / 2, getHeight()));': 1,
            'add(new GLine(0, getHeight() / 2, getWidth(), getHeight() / 2));': 1,
            '// No assist lines by default': 5
        })

    def render(self):
        return self.getChoice('centeringAssistLines')


class Set_Brick_Filled(Decision):
    def registerChoices(self):
        self.addChoice('brickFilled', {
            'brick.setFilled(true);': 1,
            'brick.setFilled(false);': 5
        })

    def render(self):
        return self.getChoice('brickFilled')


class Brick_Color_Pyramid(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 1,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.YELLOW': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
            'Color.BLACK': 5
        })

    def render(self):
        return self.getChoice('brickColor')