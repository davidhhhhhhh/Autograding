from StudentSimulator.ideaToText import Decision

class ColumnStructure(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;

public class DrawStructure{{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {{
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Determine the structure and initialize parameters
        {InitializeStructureParametersColumn}
        
        // Convert String to int array 
        String[] stringArray = input.split(",");
        int[] NUM_BRICKS = new int[stringArray.length];
        for (int i = 0; i < stringArray.length; i++) {{
            NUM_BRICKS[i] = Integer.parseInt(stringArray[i].trim());
        }}

        // Draw columns or diagonals of bricks
        for (int col = 0; col < NUM_COLUMNS; col++) {{
            int numBricks = NUM_BRICKS[col];
            for (int i = 0; i < numBricks; i++) {{
                int x = START_X + col * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + i * (BRICK_HEIGHT + BRICK_SEP);
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {SetBrickFilled}
                brick.setColor({BrickColorColumn});

                canvas.add(brick);
            }}
        }}
        // Draw the inner canvas boundary
        GRect innerCanvasBoundary = new GRect((OUTER_CANVAS_WIDTH - INNER_CANVAS_WIDTH) / 2,
                                               (OUTER_CANVAS_HEIGHT - INNER_CANVAS_HEIGHT) / 2,
                                               INNER_CANVAS_WIDTH, INNER_CANVAS_HEIGHT);
        innerCanvasBoundary.setColor(Color.BLACK);
        canvas.add(innerCanvasBoundary);
        
        // Save the canvas as an image
        saveCanvasAsImage(canvas);
    }}
    private static void saveCanvasAsImage(GCanvas canvas) {{
                    BufferedImage image = new BufferedImage(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
                    Graphics g = image.getGraphics();
                    g.setColor(Color.WHITE);
                    g.fillRect(0, 0, OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);
    
                    // Draw the current canvas content to the buffered image
                    canvas.paint(g);
    
                    // Generate a unique filename using a timestamp
                    String timestamp = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
                    String filename = "column_structure_" + timestamp + ".png";
    
                    try {{
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    }} catch (Exception e) {{
                        e.printStackTrace();
                    }}
                }}            
            }}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class InitializeStructureParametersColumn(Decision):
    def registerChoices(self):
        self.addChoice('startX', {
            'int START_X = 100 + 50;': 1,
            'int START_X = 100 + 100;': 1,
            'int START_X = 200 + 100;': 1,
            'int START_X = 300 + 100;': 3,
            'int START_X = 100;': 2,
            'int START_X = 100 - 50;': 1  # Potentially out of canvas
        })
        self.addChoice('startY', {
            'int START_Y = 100 + 400;': 3,
            'int START_Y = 100 + 350;': 2,
            'int START_Y = 100 + 300;': 2,
            'int START_Y = 100 + 100;': 2,
            'int START_Y = 100 + 50;': 2,
            'int START_Y = 100;': 1,
            'int START_Y = 100 - 50;': 1,
            'int START_Y = 100 + 450;': 1  # Potentially out of canvas
        })
        self.addChoice('structure', {
            'column': 2,
            'diagonal': 1
        })
        self.addChoice('numColumns', {
            '3': 1,
            '4': 1,
            '5': 1,
            '6': 1,
            '7': 2,
            '8': 3
        })
        self.addChoice('numBricksPerColumn', {
            'constant': 3,
            'varying': 1
        })
        self.addChoice('brickWidth', {
            '40': 1,
            '30': 20,
            '20': 1
        })
        self.addChoice('brickHeight', {
            '10': 20,
            '30': 1,
            '40': 1
        })
        self.addChoice('brickSeparation', {
            '15': 1,
            '5': 5,
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
            '{}'.format(start_x),
            '{}'.format(start_y),
            'int NUM_COLUMNS = {};'.format(numColumns),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight),
            'int BRICK_SEP = {};'.format(brickSeparation),
            'boolean isUpsideDown = {};'.format(isUpsideDown),
            'boolean isColumn = {};'.format('true' if structure == 'column' else 'false'),
            'String input = "{}";'.format(numBricksStr)
        ])


class BrickColorColumn(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 1,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.YELLOW': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
            'Color.BLACK': 60
        })

    def render(self):
        return self.getChoice('brickColor')