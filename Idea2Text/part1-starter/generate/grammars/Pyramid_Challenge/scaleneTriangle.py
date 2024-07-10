from ideaToText import Decision

class ScaleneTriangle(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawRightTriangleHorizontalOffsetStructure extends GraphicsProgram {{
    public void run() {{
        // Set canvas size
        {SetCanvasSizeRightTriangleHorizontalOffset}

        // Determine the structure and initialize parameters
        {InitializeStructureParametersRightTriangleHorizontalOffset}
        
        // Convert String to int array 
        String[] stringArray = input.split(",");
        int[] NUM_BRICKS = new int[stringArray.length];
        for (int i = 0; i < stringArray.length; i++) {{
            NUM_BRICKS[i] = Integer.parseInt(stringArray[i].trim());
        }}
        // Draw rows of bricks with horizontal offset
        for (int row = 0; row < NUM_ROWS; row++) {{
            int numBricks = NUM_BRICKS[row];
            int initialX = START_X + row * HORIZONTAL_OFFSET;
            for (int i = 0; i < numBricks; i++) {{
                int x = initialX + i * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + row * (BRICK_HEIGHT + ROW_SEP);
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {SetBrickFilled}

                // Add a rogue row/diagonal condition
                if ((row == ROGUE_ROW_INDEX && isRogueRow) || (i == ROGUE_DIAGONAL_INDEX && isRogueDiagonal)) {{
                    {SetRogueBrickFilled}
                    brick.setColor(Color.RED);
                }} else {{
                    brick.setColor({BrickColorRightTriangleHorizontalOffset});
                }}

                add(brick);
            }}
        }}
    }}

    public static void main(String[] args) {{
        // Start the GraphicsProgram
        new DrawRightTriangleHorizontalOffsetStructure().start(args);
    }}
}}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class SetCanvasSizeRightTriangleHorizontalOffset(Decision):
    def registerChoices(self):
        self.addChoice('canvasWidth', {
            '400': 2,
            '600': 1
        })
        self.addChoice('canvasHeight', {
            '260': 3,
            '400': 1,
            '600': 1
        })

    def render(self):
        return 'setSize({}, {});'.format(self.getChoice('canvasWidth'), self.getChoice('canvasHeight'))


class InitializeStructureParametersRightTriangleHorizontalOffset(Decision):
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
        self.addChoice('numBricksBase', {
            '3': 2,
            '4': 3,
            '5': 3,
            '6': 4,
            '7': 5
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
        self.addChoice('horizontalOffset', {
            '20': 2,
            '-20': 1
        })
        self.addChoice('isUpsideDown', {
            'true': 1,
            'false': 2
        })

    def render(self):
        numBricksBase = int(self.getChoice('numBricksBase'))
        brickWidth = self.getChoice('brickWidth')
        brickHeight = self.getChoice('brickHeight')
        brickSeparation = self.getChoice('brickSeparation')
        rowSeparation = self.getChoice('rowSeparation')
        horizontalOffset = self.getChoice('horizontalOffset')
        isUpsideDown = self.getChoice('isUpsideDown')
        start_x = self.getChoice('startX')
        start_y = self.getChoice('startY')

        numRows = numBricksBase
        numBricks = [numRows - row if isUpsideDown == 'true' else row + 1 for row in range(numRows)]
        numBricksStr = ', '.join(map(str, numBricks))

        return '\n'.join([
            '{};'.format(start_x),
            '{};'.format(start_y),
            'int NUM_ROWS = {};'.format(numRows),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight),
            'int BRICK_SEP = {};'.format(brickSeparation),
            'int ROW_SEP = {};'.format(rowSeparation),
            'int HORIZONTAL_OFFSET = {};'.format(horizontalOffset),
            'boolean isUpsideDown = {};'.format(isUpsideDown),
            'String input = "{}";'.format(numBricksStr)
        ])


class SetBrickFilled(Decision):
    def registerChoices(self):
        self.addChoice('brickFilled', {
            'brick.setFilled(false);': 5,
            'brick.setFilled(true);': 1
        })

    def render(self):
        return self.getChoice('brickFilled')


class SetRogueBrickFilled(Decision):
    def registerChoices(self):
        self.addChoice('rogueBrickFilled', {
            'brick.setFilled(false);': 3,
            'brick.setFilled(true);': 1
        })

    def render(self):
        return self.getChoice('rogueBrickFilled')


class BrickColorRightTriangleHorizontalOffset(Decision):
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