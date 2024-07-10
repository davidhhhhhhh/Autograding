from ideaToText import Decision

class SingleRow(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawBrickRow extends GraphicsProgram {{
    public void run() {{
        // Set canvas size
        {SetCanvasSizeSingleRow}

        // Initialize starting position and other parameters
        {InitializeBrickParametersSingleRow}

        // Draw bricks
        for (int i = 0; i < NUM_BRICKS; i++) {{
            int x = i * (BRICK_WIDTH + BRICK_SEP);
            int y = START_Y - BRICK_HEIGHT / 2;
            GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

            // Add a rogue brick condition
            if (i == ROGUE_BRICK_INDEX) {{
                brick.setFilled(true);
                brick.setColor(Color.RED);
            }} else {{
                brick.setColor({BrickColorSingleRow});
            }}

            add(brick);
        }}
    }}

    public static void main(String[] args) {{
        // Start the GraphicsProgram
        new DrawBrickRow().start(args);
    }}
}}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class SetCanvasSizeSingleRow(Decision):
    def registerChoices(self):
        self.addChoice('canvasWidth', {
            '400': 2,
            '600': 1
        })
        self.addChoice('canvasHeight', {
            '260': 3,
            '200': 1,
            '300': 1
        })

    def render(self):
        return 'setSize({}, {});'.format(self.getChoice('canvasWidth'), self.getChoice('canvasHeight'))


class InitializeBrickParametersSingleRow(Decision):
    def registerChoices(self):
        self.addChoice('numBricks', {
            'int NUM_BRICKS = 3;': 2,
            'int NUM_BRICKS = 4;': 1,
            'int NUM_BRICKS = 5;': 1,
            'int NUM_BRICKS = 6;': 1
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
            'int BRICK_SEP = 5;': 1,
            'int BRICK_SEP = 0;': 3,
            'int BRICK_SEP = 10;': 1
        })
        self.addChoice('rogueBrickIndex', {
            'int ROGUE_BRICK_INDEX = -1;': 3,  # No rogue brick
            'int ROGUE_BRICK_INDEX = 1;': 1,  # Rogue brick at position 1
            'int ROGUE_BRICK_INDEX = 2;': 1  # Rogue brick at position 2
        })
        self.addChoice('startYPosition', {
            'int START_Y = getHeight() - 20;': 3,  # High probability to start at the bottom
            'int START_Y = getHeight() / 2;': 1,
            'int START_Y = 40;': 1,
            'int START_Y = -40;': 1
        })

    def render(self):
        return '\n'.join([
            self.getChoice('numBricks'),
            'int BRICK_WIDTH = {};'.format(self.getChoice('brickWidth')),
            'int BRICK_HEIGHT = {};'.format(self.getChoice('brickHeight')),
            self.getChoice('brickSeparation'),
            self.getChoice('rogueBrickIndex'),
            self.getChoice('startYPosition')
        ])


class BrickColorSingleRow(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 2,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.YELLOW': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1
        })

    def render(self):
        return self.getChoice('brickColor')