from ideaToText import Decision

class BrickWall(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawBrickWallStructure extends GraphicsProgram {{
    public void run() {{
        // Set canvas size
        {SetCanvasSizeBrickWall}

        // Initialize structure parameters
        {InitializeStructureParametersBrickWall}

        // Draw rows of bricks covering the entire screen without offset
        for (int row = 0; row < NUM_ROWS; row++) {{
            for (int col = 0; col < NUM_COLUMNS; col++) {{
                int x = col * BRICK_WIDTH;
                int y = row * BRICK_HEIGHT;
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {SetBrickFilled}

                brick.setColor({BrickColorBrickWall});
                add(brick);
            }}
        }}
    }}

    public static void main(String[] args) {{
        // Start the GraphicsProgram
        new DrawBrickWallStructure().start(args);
    }}
}}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class SetCanvasSizeBrickWall(Decision):
    def registerChoices(self):
        self.addChoice('canvasWidth', {
            '600': 1
        })
        self.addChoice('canvasHeight', {
            '400': 1
        })

    def render(self):
        return 'setSize({}, {});'.format(self.getChoice('canvasWidth'), self.getChoice('canvasHeight'))


class InitializeStructureParametersBrickWall(Decision):
    def registerChoices(self):
        self.addChoice('brickWidth', {
            '40': 3,
            '60': 1,
            '80': 1
        })
        self.addChoice('brickHeight', {
            '20': 3,
            '10': 1,
            '40': 1
        })

    def render(self):
        brickWidth = int(self.getChoice('brickWidth'))
        brickHeight = int(self.getChoice('brickHeight'))

        canvasWidth = 600
        canvasHeight = 400

        numColumns = canvasWidth // brickWidth
        numRows = canvasHeight // brickHeight

        return '\n'.join([
            'int NUM_COLUMNS = {};'.format(numColumns),
            'int NUM_ROWS = {};'.format(numRows),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight),
            'int BRICK_SEP = 0;',
            'int ROW_SEP = 0;'
        ])

class BrickColorBrickWall(Decision):
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