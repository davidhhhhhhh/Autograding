from ideaToText import Decision


class ColumnStructure(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawColumnStructure extends GraphicsProgram {
    public void run() {
        // Set canvas size
        {Set_Canvas_Size_Column}

        // Determine the structure and initialize parameters
        {Initialize_Structure_Parameters_Column}

        // Draw columns or diagonals of bricks
        for (int col = 0; col < NUM_COLUMNS; col++) {
            int numBricks = NUM_BRICKS[col];
            for (int i = 0; i < numBricks; i++) {
                int x = START_X + col * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + i * (BRICK_HEIGHT + BRICK_SEP);
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {Set_Brick_Filled}

                // Add a rogue column/diagonal condition
                if ((col == ROGUE_COLUMN_INDEX && isRogueColumn) || (i == ROGUE_DIAGONAL_INDEX && isRogueDiagonal)) {
                    {Set_Rogue_Brick_Filled}
                    brick.setColor(Color.RED);
                } else {
                    brick.setColor({Brick_Color_Column});
                }

                add(brick);
            }
        }
    }

    public static void main(String[] args) {
        // Start the GraphicsProgram
        new DrawColumnStructure().start(args);
    }
}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class Set_Canvas_Size_Column(Decision):
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


class Initialize_Structure_Parameters_Column(Decision):
    def registerChoices(self):
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
        self.addChoice('structure', {
            'column': 2,
            'diagonal': 1
        })
        self.addChoice('numColumns', {
            '3': 2,
            '4': 1,
            '5': 1,
            '6': 1,
            '7': 1,
            '8': 1
        })
        self.addChoice('numBricksPerColumn', {
            'constant': 2,
            'varying': 1
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
            '0': 3,
            '10': 1
        })
        self.addChoice('isUpsideDown', {
            'true': 1,
            'false': 2
        })

    def render(self):
        structure = self.getChoice('structure')
        numColumns = int(self.getChoice('numColumns'))
        numBricksPerColumn = self.getChoice('numBricksPerColumn')
        brickWidth = self.getChoice('brickWidth')
        brickHeight = self.getChoice('brickHeight')
        brickSeparation = self.getChoice('brickSeparation')
        isUpsideDown = self.getChoice('isUpsideDown')
        start_x = self.getChoice('startX')
        start_y = self.getChoice('startY')

        if numBricksPerColumn == 'constant':
            numBricks = [numColumns] * numColumns
        else:
            numBricks = [numColumns - col if isUpsideDown == 'false' else col + 1 for col in range(numColumns)]

        numBricksStr = ', '.join(map(str, numBricks))

        return '\n'.join([
            'int START_X = {}'.format(start_x),
            'int START_Y = {}'.format(start_y),
            'int NUM_COLUMNS = {};'.format(numColumns),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight),
            'int BRICK_SEP = {};'.format(brickSeparation),
            'boolean isUpsideDown = {};'.format(isUpsideDown),
            'boolean isColumn = {};'.format('true' if structure == 'column' else 'false'),
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
            'brick.setFilled(false);': 3,
            'brick.setFilled(true);': 1
        })

    def render(self):
        return self.getChoice('rogueBrickFilled')


class Brick_Color_Column(Decision):
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