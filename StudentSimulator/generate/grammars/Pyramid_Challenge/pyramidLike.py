from StudentSimulator.ideaToText import Decision


class PyramidLike(Decision):
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
import java.util.Random;

public class DrawStructure{{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {{
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Initialize structure parameters
        {InitializeStructureParametersRoughlySymmetric}
        
        // Convert String to int array 
        String[] stringArray = input.split(",");
        int[] NUM_BRICKS = new int[stringArray.length];
        for (int i = 0; i < stringArray.length; i++) {{
            NUM_BRICKS[i] = Integer.parseInt(stringArray[i].trim());
        }}

        Random rand = new Random();

        // Draw rows of bricks with horizontal offset
        for (int row = 0; row < NUM_ROWS; row++) {{
            int initialX = START_X + row * HORIZONTAL_OFFSET;
            for (int i = 0; i < NUM_BRICKS[row]; i++) {{
                int x = initialX + i * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + row * (BRICK_HEIGHT + ROW_SEP);

                // Randomly decide if there is a hole (missing brick)
                boolean hasHole = (rand.nextInt(10) < HOLE_PROBABILITY);

                if (!hasHole) {{
                    GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                    // Determine if the brick is filled
                    {SetBrickFilled}
                    brick.setColor({BrickColorRoughlySymmetric});

                    canvas.add(brick);
                }}
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
                    String filename = "pyramid_like_" + timestamp + ".png";
    
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


class InitializeStructureParametersRoughlySymmetric(Decision):
    def registerChoices(self):
        self.addChoice('startX', {
            'int START_X = 150;': 1,
            'int START_X = 200;': 1,
            'int START_X = 750;': 1,
            'int START_X = 50;': 1  # Potentially out of canvas
        })
        self.addChoice('startY', {
            'int START_Y = 550;': 1,
            'int START_Y = 510;': 1,
            'int START_Y = 50;': 1,
            'int START_Y = 350;': 1  # Potentially out of canvas
        })
        self.addChoice('numBricksBase', {
            '3': 2,
            '4': 1,
            '5': 2,
            '6': 3,
            '7': 4,
            '8': 5
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
            '5': 1,
            '0': 10,
            '10': 1
        })
        self.addChoice('rowSeparation', {
            '5': 1,
            '0': 10,
            '10': 1
        })
        self.addChoice('horizontalOffset', {
            '20': 2,
            '-20': 1
        })
        self.addChoice('holeProbability', {
            '1': 1,
            '2': 2,
            '3': 1
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
        holeProbability = self.getChoice('holeProbability')
        isUpsideDown = self.getChoice('isUpsideDown')
        start_x = self.getChoice('startX')
        start_y = self.getChoice('startY')

        numRows = numBricksBase
        numBricks = [numRows - row if isUpsideDown == 'true' else row + 1 for row in range(numRows)]
        numBricksStr = ', '.join(map(str, numBricks))

        return '\n'.join([
            '{}'.format(start_x),
            '{}'.format(start_y),
            'int NUM_ROWS = {};'.format(numRows),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight),
            'int BRICK_SEP = {};'.format(brickSeparation),
            'int ROW_SEP = {};'.format(rowSeparation),
            'int HORIZONTAL_OFFSET = {};'.format(horizontalOffset),
            'int HOLE_PROBABILITY = {};'.format(holeProbability),
            'boolean isUpsideDown = {};'.format(isUpsideDown),
            'String input = "{}";'.format(numBricksStr)
        ])


class BrickColorRoughlySymmetric(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 2,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.RED': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
            'Color.BLACK': 60
        })

    def render(self):
        return self.getChoice('brickColor')