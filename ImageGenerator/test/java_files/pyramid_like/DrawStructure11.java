import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;
import java.util.Random;

public class DrawStructure11{
    private static final int CANVAS_WIDTH = 600;
    private static final int CANVAS_HEIGHT = 400;
    private static final int IMAGE_WIDTH = 800;
    private static final int IMAGE_HEIGHT = 600;

    public static void main(String[] args) {
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(CANVAS_WIDTH, CANVAS_HEIGHT);

        // Initialize structure parameters
        int START_X = 50;
int START_Y = 100;
int NUM_ROWS = 3;
int BRICK_WIDTH = 40;
int BRICK_HEIGHT = 30;
int BRICK_SEP = 10;
int ROW_SEP = 5;
int HORIZONTAL_OFFSET = 20;
int HOLE_PROBABILITY = 3;
boolean isUpsideDown = false;
String input = "1, 2, 3";
        
        // Convert String to int array 
        String[] stringArray = input.split(",");
        int[] NUM_BRICKS = new int[stringArray.length];
        for (int i = 0; i < stringArray.length; i++) {
            NUM_BRICKS[i] = Integer.parseInt(stringArray[i].trim());
        }

        Random rand = new Random();

        // Draw rows of bricks with horizontal offset
        for (int row = 0; row < NUM_ROWS; row++) {
            int initialX = START_X + row * HORIZONTAL_OFFSET;
            for (int i = 0; i < NUM_BRICKS[row]; i++) {
                int x = initialX + i * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + row * (BRICK_HEIGHT + ROW_SEP);

                // Randomly decide if there is a hole (missing brick)
                boolean hasHole = (rand.nextInt(10) < HOLE_PROBABILITY);

                if (!hasHole) {
                    GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                    // Determine if the brick is filled
                    brick.setFilled(false);
                    brick.setColor(Color.BLUE);

                    canvas.add(brick);
                }
            }
        }
        // Save the canvas as an image
        saveCanvasAsImage(canvas);
    }
    private static void saveCanvasAsImage(GCanvas canvas) {
        BufferedImage image = new BufferedImage(IMAGE_WIDTH, IMAGE_HEIGHT, BufferedImage.TYPE_INT_RGB);
        Graphics g = image.getGraphics();
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);

        // Draw the current canvas content to the buffered image
        BufferedImage canvasImage = new BufferedImage(CANVAS_WIDTH, CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
        Graphics canvasGraphics = canvasImage.getGraphics();
        canvasGraphics.setColor(Color.WHITE);
        canvasGraphics.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
        canvas.paint(canvasGraphics);

        // Center the canvas on the image
        int offsetX = (IMAGE_WIDTH - CANVAS_WIDTH) / 2;
        int offsetY = (IMAGE_HEIGHT - CANVAS_HEIGHT) / 2;
        g.drawImage(canvasImage, offsetX, offsetY, null);

        // Draw a border around the canvas area
        g.setColor(Color.BLACK);
        g.drawRect(offsetX, offsetY, CANVAS_WIDTH, CANVAS_HEIGHT);

        // Generate a unique filename using a timestamp
        String timestamp = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
        String filename = "pyramidLike_" + timestamp + ".png";

        try {
            // Write the buffered image to a file
            ImageIO.write(image, "png", new File(filename));
            System.out.println("Image saved as " + filename);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }            
}