from ideaToText import Decision


class RightTriangle(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawRightTriangleStructure extends GraphicsProgram {
    public void run() {
        // Set canvas size
        {Set_Canvas_Size_RightTriangle}

        // Determine the shape and initialize parameters
        {Initialize_Shape_Parameters_RightTriangle}

        // Draw rows of bricks
        for (int row = 0; row < NUM_ROWS; row++) {
            int numBricks = NUM_BRICKS[row];
            for (int i = 0; i < numBricks; i++) {
                int x = START_X + i * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + row * (BRICK_HEIGHT + ROW_SEP);
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {Set_Brick_Filled}

                // Add a rogue row/diagonal condition
                if ((row == ROGUE_ROW_INDEX && isRogueRow) || (i == ROGUE_DIAGONAL_INDEX && isRogueDiagonal)) {
                    {Set_Rogue_Brick_Filled}
                    brick.setColor(Color.RED);
                } else {
                    brick.setColor({Brick_Color_RightTriangle});
                }

                add(brick);
            }
        }
    }

    public static void main(String[] args) {
        // Start the GraphicsProgram
        new DrawRightTriangleStructure().start(args);
    }
}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class Set_Canvas_Size_RightTriangle(Decision):
    def registerChoices(self):
        self.addChoice('canvasWidth', {
            '400': 2,
            '600': 1
        })
        self.addChoice('canvasHeight', {
            '200 + 60': 3,
            '400': 1,
            '600': 1
        })

    def render(self):
        return 'setSize({}, {});'.format(self.getChoice('canvasWidth'), self.getChoice('canvasHeight'))


class Initialize_Shape_Parameters_RightTriangle(Decision):
    def registerChoices(self):
        self.addChoice('shape', {
            'rightTriangle': 2,
            'trapezoid': 1
        })
        self.addChoice('numBricksBase', {
            '13': 2,
            '14': 3,
            '15': 4,
            '16': 5
        })
        self.addChoice('brickWidth', {
            '40': 2,
            '30': 1,
            '20': 1
        })
        self.addChoice('brickHeight', {
            '20': 2,
            '30': 1,
            '40': 1
        })
        self.addChoice('brickSeparation', {
            '5': 1,
            '0': 5,
            '10': 1
        })
        self.addChoice('rowSeparation', {
            '5': 1,
            '0': 5,
            '10': 1
        })
        self.addChoice('isUpsideDown', {
            'true': 1,
            'false': 2
        })
        self.addChoice('startX', {
            'int START_X = 50;': 1,
            'int START_X = 100;': 1,
            'int START_X = -50;': 1  # Potentially out of canvas
        })
        self.addChoice('startY', {
            'int START_Y = 50;': 1,
            'int START_Y = 100;': 1,
            'int START_Y = -50;': 1  # Potentially out of canvas
        })

    def render(self):
        shape = self.getChoice('shape')
        numBricksBase = self.getChoice('numBricksBase')
        brickWidth = self.getChoice('brickWidth')
        brickHeight = self.getChoice('brickHeight')
        brickSeparation = self.getChoice('brickSeparation')
        rowSeparation = self.getChoice('rowSeparation')
        isUpsideDown = self.getChoice('isUpsideDown')
        start_x = self.getChoice('startX')
        start_y = self.getChoice('startY')

        if shape == 'rightTriangle':
            numRows = int(numBricksBase)
            numBricks = [numRows - row if isUpsideDown == 'false' else row + 1 for row in range(numRows)]
        else:
            numRows = min(10, int(numBricksBase))
            numBricks = [numRows - row if isUpsideDown == 'false' else int(numBricksBase) - row for row in
                         range(numRows)]

        numBricksStr = ', '.join(map(str, numBricks))

        return '\n'.join([
            'int START_X = {}'.format(start_x),
            'int START_Y = {}'.format(start_y),
            'int NUM_ROWS = {};'.format(numRows),
            'int NUM_BRICKS_BASE = {};'.format(numBricksBase),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight),
            'int BRICK_SEP = {};'.format(brickSeparation),
            'int ROW_SEP = {};'.format(rowSeparation),
            'boolean isUpsideDown = {};'.format(isUpsideDown),
            'boolean isRightTriangle = {};'.format('true' if shape == 'rightTriangle' else 'false'),
            'int[] NUM_BRICKS = {{{}}};'.format(numBricksStr)
        ])


class Set_Brick_Filled(Decision):
    def registerChoices(self):
        self.addChoice('brickFilled', {
            'brick.setFilled(false);': 5,
            'brick.setFilled(true);': 1
        })

    def render(self):
        return self.getChoice('brickFilled')


class Set_Rogue_Brick_Filled(Decision):
    def registerChoices(self):
        self.addChoice('rogueBrickFilled', {
            'brick.setFilled(false);': 5,
            'brick.setFilled(true);': 1
        })

    def render(self):
        return self.getChoice('rogueBrickFilled')


class Brick_Color_RightTriangle(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 2,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.YELLOW': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
            'Color.BLACK': 5
        })

    def render(self):
        return self.getChoice('brickColor')