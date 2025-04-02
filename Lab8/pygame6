import pygame

pygame.init()
FPS = 120
FramePerSec = pygame.time.Clock()

# Setting window size
win_x = 500
win_y = 500

win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Paint')

# Class for drawing
class drawing(object):

    def __init__(self):
        self.color = (0, 0, 0)  # Default drawing color (black)
        self.rad = 6  # Default brush radius
        self.eraser_mode = False  # Flag for eraser mode

    # Drawing Function
    def draw(self, win, pos):
        if self.eraser_mode:
            # If eraser mode is enabled, draw in white (erase)
            pygame.draw.circle(win, (255, 255, 255), (pos[0], pos[1]), 20)  
        else:
            # Otherwise, draw with the selected color
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), self.rad)  

    # Detecting clicks
    def click(self, win, color_buttons, other_buttons):
        pos = pygame.mouse.get_pos()  # Get the current mouse position

        # If the left mouse button is pressed and within the drawing area
        if pygame.mouse.get_pressed()[0] and pos[0] < 400 and pos[1] > 25:
            self.draw(win, pos)  # Draw at the cursor position

        # If clicking in the button area
        elif pygame.mouse.get_pressed()[0]:
            for button in color_buttons:
                # Check if the click is inside a color button
                if button.x < pos[0] < button.x + button.width and button.y < pos[1] < button.y + button.height:
                    self.color = button.color2  # Change drawing color
                    self.eraser_mode = False  # Disable eraser mode

            for button in other_buttons:
                # Check if the click is inside a functional button
                if button.x < pos[0] < button.x + button.width and button.y < pos[1] < button.y + button.height:
                    if button.action == 1:
                        win.fill((255, 255, 255))  # Clear the screen
                    elif button.action == 2:
                        self.eraser_mode = True  # Enable eraser mode


# Class for buttons
class button(object):

    def __init__(self, x, y, width, height, color, color2, outline=0, action=0, text=''):
        self.x = x  # X position
        self.y = y  # Y position
        self.height = height  # Button height
        self.width = width  # Button width
        self.color = color  # Button background color
        self.outline = outline  # Outline thickness
        self.color2 = color2  # Text color
        self.action = action  # Button function identifier
        self.text = text  # Button text

    # Function to draw the button
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.outline)
        font = pygame.font.SysFont('times new roman', 30)  # Font style
        text = font.render(self.text, 1, self.color2)  # Render button text
        win.blit(text, (int(self.x + self.width / 2 - text.get_width() / 2),
                        int(self.y + self.height / 2 - text.get_height() / 2)))  # Center text


# Function to handle drawing and button updates
def draw(win):
    player1.click(win, Buttons_color, Buttons_other)  # Handle user input

    # Draw button panel
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 500), 2)  
    pygame.draw.rect(win, (255, 255, 255), (400, 0, 100, 500))  
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 500), 2)  

    # Draw buttons
    for button in Buttons_color:
        button.draw(win)

    for button in Buttons_other:
        button.draw(win)

    pygame.display.update()  # Update display


# Main game loop
def main_loop():
    run = True
    while run:
        keys = pygame.key.get_pressed()  # Get pressed keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:  # Quit condition
                run = False

        draw(win)  # Update the window

    pygame.quit()  # Quit pygame when loop ends


player1 = drawing()  # Create a drawing instance
win.fill((255, 255, 255))  # Set background to white

# Defining color buttons
redButton = button(453, 30, 40, 40, (255, 0, 0), (255, 0, 0))  # Red
blueButton = button(407, 30, 40, 40, (0, 0, 255), (0, 0, 255))  # Blue
greenButton = button(407, 76, 40, 40, (0, 255, 0), (0, 255, 0))  # Green
orangeButton = button(453, 76, 40, 40, (255, 192, 0), (255, 192, 0))  # Orange
yellowButton = button(407, 122, 40, 40, (255, 255, 0), (255, 255, 0))  # Yellow
purpleButton = button(453, 122, 40, 40, (112, 48, 160), (112, 48, 160))  # Purple
blackButton = button(407, 168, 40, 40, (0, 0, 0), (0, 0, 0))  # Black

# Defining functional buttons
clrButton = button(407, 214, 86, 40, (201, 201, 201), (0, 0, 0), 0, 1, 'Clear')  # Clear button
eraserButton = button(407, 260, 86, 40, (201, 201, 201), (0, 0, 0), 0, 2, 'Eraser')  # Eraser button

# Store buttons in lists
Buttons_color = [blueButton, redButton, greenButton, orangeButton, yellowButton, purpleButton, blackButton]
Buttons_other = [clrButton, eraserButton]

main_loop()  # Start the main loop
FramePerSec.tick(FPS)  # Set FPS limit
