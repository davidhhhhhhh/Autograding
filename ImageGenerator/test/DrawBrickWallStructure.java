import acm.graphics.*;
import acm.program.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class DrawBrickWallStructure extends GraphicsProgram {
    private static final int CANVAS_WIDTH = 600;
    private static final int CANVAS_HEIGHT = 400;
    private static final int IMAGE_WIDTH = 800;
    private static final int IMAGE_HEIGHT = 600;
    private static final int NUM_COLUMNS = 15;
    private static final int NUM_ROWS = 20;
    private static final int BRICK_WIDTH = 40;
    private static final int BRICK_HEIGHT = 20;

    public void run() {
        // Set canvas size
        setSize(CANVAS_WIDTH, CANVAS_HEIGHT);

        // Centering the canvas on the output image
        int offsetX = (IMAGE_WIDTH - CANVAS_WIDTH) / 2;
        int offsetY = (IMAGE_HEIGHT - CANVAS_HEIGHT) / 2;

        // Draw rows of bricks covering the entire screen without offset
        for (int row = 0; row < NUM_ROWS; row++) {
            for (int col = 0; col < NUM_COLUMNS; col++) {
                int x = col * BRICK_WIDTH;
                int y = row * BRICK_HEIGHT;
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                brick.setFilled(false);
                brick.setColor(Color.BLACK);
                add(brick);
            }
        }

        // Save the canvas as an image
        saveCanvasAsImage("brick_wall_structure.png", offsetX, offsetY);
    }

    private void saveCanvasAsImage(String filename, int offsetX, int offsetY) {
        BufferedImage image = new BufferedImage(IMAGE_WIDTH, IMAGE_HEIGHT, BufferedImage.TYPE_INT_RGB);
        Graphics g = image.getGraphics();
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);

        // Draw the current canvas content to the buffered image
        BufferedImage canvasImage = new BufferedImage(CANVAS_WIDTH, CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
        GCanvas canvas = getGCanvas();
        canvas.paint(canvasImage.getGraphics());

        g.drawImage(canvasImage, offsetX, offsetY, null);

        // Draw a border around the canvas area
        g.setColor(Color.BLACK);
        g.drawRect(offsetX, offsetY, CANVAS_WIDTH, CANVAS_HEIGHT);

        try {
            // Write the buffered image to a file
            ImageIO.write(image, "png", new File(filename));
            System.out.println("Image saved as " + filename);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // Start the GraphicsProgram
        new DrawBrickWallStructure().start(args);
    }
}
