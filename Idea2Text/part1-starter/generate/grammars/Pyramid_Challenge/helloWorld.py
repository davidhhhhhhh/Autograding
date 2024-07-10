from ideaToText import Decision

class HelloWorld(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;

public class DrawRectangle extends GraphicsProgram {{
    public void run() {{
        // Set canvas size
        {SetCanvasHelloWorld}
        // Create a rectangle with the specified position 
        {InitialPositionHelloWorld}
        // Specify size of the rectangle 
        {DrawBlockHelloWorld}
        // Add color, optional 
        {AddColorHelloWorld}

        // Add the rectangle to the canvas
        add(rect);
    }}

    public static void main(String[] args) {{
        // Start the GraphicsProgram
        new DrawRectangle().start(args);
    }}
}}''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand it
        return self.getChoice('codeStructure')