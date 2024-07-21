from ideaToText import Decision


class Offtrack(Decision):
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
        {InitializeStructureParametersOfftrack}
        
        // Draw the irregular shape
        {DrawOfftrack}
        
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
                    String filename = "offTrack_" + timestamp + ".png";

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


class InitializeStructureParametersOfftrack(Decision):
    def registerChoices(self):
        self.addChoice('startX', {
            'int START_X = 150;': 1,
            'int START_X = 200;': 1,
            'int START_X = 750;': 1,
            'int START_X = 50;': 1  # Potentially out of canvas
        })
        self.addChoice('startY', {
            'int START_Y = 50;': 1,
            'int START_Y = 400;': 1,
            'int START_Y = 500;': 1,
            'int START_Y = 550;': 1  # Potentially out of canvas
        })
        self.addChoice('numBricksBase', {
            '3': 2,
            '4': 3,
            '5': 3,
            '6': 4,
            '7': 5
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
            '0': 20,
            '10': 1
        })
        self.addChoice('rowSeparation', {
            '5': 1,
            '0': 20,
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


class DrawOfftrack(Decision):
    def registerChoices(self):
        self.addChoice('randomCode', {
            '''GRect rect = new GRect(START_X, START_Y, BRICK_WIDTH, BRICK_HEIGHT);
               GRect rect1 = new GRect(START_X + 100, START_Y + 50, BRICK_WIDTH, BRICK_HEIGHT);
               canvas.add(rect); canvas.add(rect1);''': 1,
            '''GRect rect = new GRect(START_X, START_Y, BRICK_WIDTH, BRICK_HEIGHT);
               GRect rect1 = new GRect(START_X - 100, START_Y + 150, BRICK_WIDTH + 10, BRICK_HEIGHT + 50);
               canvas.add(rect); canvas.add(rect1);''': 1,
            '''GRect rect = new GRect(START_X, START_Y, 50, BRICK_HEIGHT);
               GRect rect1 = new GRect(START_X - 300, START_Y + 150, BRICK_WIDTH + 10, 100 + 50);
               canvas.add(rect); canvas.add(rect1);''': 1,
        })

    def render(self):
        return self.getChoice('randomCode')
