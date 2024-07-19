import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;

public class DrawStructure99{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Initialize brick parameters for first row
        int NUM_BRICKS_FIRST_ROW = 7;
int BRICK_WIDTH_FIRST_ROW = 30;
int BRICK_HEIGHT_FIRST_ROW = 20;
int BRICK_SEP_FIRST_ROW = 0;
int ROGUE_BRICK_INDEX_FIRST_ROW = -1;
int START_X_FIRST_ROW = 200;
int START_Y_FIRST_ROW = 450;

        // Draw first row of bricks
        for (int i = 0; i < NUM_BRICKS_FIRST_ROW; i++) {
            int x = START_X_FIRST_ROW + i * (BRICK_WIDTH_FIRST_ROW + BRICK_SEP_FIRST_ROW);
            int y = START_Y_FIRST_ROW;
            GRect brick = new GRect(x, y, BRICK_WIDTH_FIRST_ROW, BRICK_HEIGHT_FIRST_ROW);

            // Add a rogue brick condition for the first row
            if (i == ROGUE_BRICK_INDEX_FIRST_ROW) {
                brick.setFilled(true);
                brick.setColor(Color.RED);
            } else {
                brick.setColor(Color.BLUE);
            }

            canvas.add(brick);
        }

        // Initialize brick parameters for second row
        int NUM_BRICKS_SECOND_ROW = 7;
int BRICK_WIDTH_SECOND_ROW = 30;
int BRICK_HEIGHT_SECOND_ROW = 20;
int BRICK_SEP_SECOND_ROW = 0;
int ROGUE_BRICK_INDEX_SECOND_ROW = -1;
int START_X_SECOND_ROW = START_X_FIRST_ROW;
int START_Y_SECOND_ROW = START_Y_FIRST_ROW + BRICK_HEIGHT_FIRST_ROW;

        // Draw second row of bricks
        for (int i = 0; i < NUM_BRICKS_SECOND_ROW; i++) {
            int x = START_X_SECOND_ROW + i * (BRICK_WIDTH_SECOND_ROW + BRICK_SEP_SECOND_ROW);
            int y = START_Y_SECOND_ROW;
            GRect brick = new GRect(x, y, BRICK_WIDTH_SECOND_ROW, BRICK_HEIGHT_SECOND_ROW);

            // Add a rogue brick condition for the second row
            if (i == ROGUE_BRICK_INDEX_SECOND_ROW) {
                brick.setFilled(true);
                brick.setColor(Color.RED);
            } else {
                brick.setColor(Color.BLUE);
            }

            canvas.add(brick);
        }
        // Save the canvas as an image
        saveCanvasAsImage(canvas);
    }
    private static void saveCanvasAsImage(GCanvas canvas) {
                    BufferedImage image = new BufferedImage(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
                    Graphics g = image.getGraphics();
                    g.setColor(Color.WHITE);
                    g.fillRect(0, 0, OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);
    
                    // Draw the current canvas content to the buffered image
                    canvas.paint(g);
    
                    // Generate a unique filename using a timestamp
                    String timestamp = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
                    String filename = "two_rows_" + timestamp + ".png";
    
                    try {
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }            
            }