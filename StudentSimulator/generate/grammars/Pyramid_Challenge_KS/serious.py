from StudentSimulator.ideaToText import Decision


class Serious(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            'common_structure': 1
        })

    def render(self):
        choice_mapping = {
            'common_structure': '''import acm.graphics.*;
import java.awt.Color;
import java.util.Random;
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
        
        // Initiate new random
        Random random = new Random();

        // Initialize brick size
        {BrickSize}

        // Horizontal Loop
        {HorizontalLoop}
        
        // Draw the inner canvas boundary
        GRect innerCanvasBoundary = new GRect((OUTER_CANVAS_WIDTH - INNER_CANVAS_WIDTH) / 2,
                                               (OUTER_CANVAS_HEIGHT - INNER_CANVAS_HEIGHT) / 2,
                                               INNER_CANVAS_WIDTH, INNER_CANVAS_HEIGHT);
        innerCanvasBoundary.setColor(Color.BLACK);
        canvas.add(innerCanvasBoundary);

        // Save the canvas as an image
        saveCanvasAsImage(canvas, args[0]);
    }}
    private static void saveCanvasAsImage(GCanvas canvas, String imageDir) {{
                    BufferedImage image = new BufferedImage(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
                    Graphics g = image.getGraphics();
                    g.setColor(Color.WHITE);
                    g.fillRect(0, 0, OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

                    // Draw the current canvas content to the buffered image
                    canvas.paint(g);

                    // Generate a unique filename using a timestamp
                    String timestamp = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
                    String filename = "image_" + timestamp + ".png";

                    try {{
                        // Write the buffered image to a file
                        File outputfile = new File(imageDir, filename);
                        ImageIO.write(image, "png", outputfile);
                        System.out.println("Image saved as " + outputfile.getPath());
                    }} catch (Exception e) {{
                        e.printStackTrace();
                    }}
                }}            
            }}''',
        }
        choice = self.getChoice('codeStructure')
        output = choice_mapping[choice]
        return output
