import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;

public class DrawStructure330{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Determine the structure and initialize parameters
        int START_X = 50;;
int START_Y = 50;;
int NUM_ROWS = 6;
int BRICK_WIDTH = 30;
int BRICK_HEIGHT = 10;
int BRICK_SEP = 0;
int ROW_SEP = 0;
int HORIZONTAL_OFFSET = 20;
boolean isUpsideDown = false;
String input = "1, 2, 3, 4, 5, 6";
        
        // Draw the irregular shape
        GRect rect = new GRect(START_X, START_Y, BRICK_WIDTH, BRICK_HEIGHT);
               GRect rect1 = new GRect(START_X - 100, START_Y + 150, BRICK_WIDTH + 10, BRICK_HEIGHT + 50);
               canvas.add(rect); canvas.add(rect1);
        
        // Draw the inner canvas boundary
        GRect innerCanvasBoundary = new GRect((OUTER_CANVAS_WIDTH - INNER_CANVAS_WIDTH) / 2,
                                               (OUTER_CANVAS_HEIGHT - INNER_CANVAS_HEIGHT) / 2,
                                               INNER_CANVAS_WIDTH, INNER_CANVAS_HEIGHT);
        innerCanvasBoundary.setColor(Color.BLACK);
        canvas.add(innerCanvasBoundary);

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
                    String filename = "offTrack_" + timestamp + ".png";

                    try {
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }            
            }