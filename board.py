import pygame
from pygame.locals import *

# Initialize Pygame and set up the display
pygame.init()
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Checkers")

checker_pieces = []

dragging = False

#function to add the pieces to the board in their correct spaces
def add_pieces():
    for row in range(8):
        for col in range(8):
            if row < 3:
                if (row % 2 == 0 and col % 2 ==1) or (row % 2 == 1 and col % 2 ==0):
                    checker_pieces.append((row, col))
            if row >4:
                if (row % 2 == 1 and col % 2 ==0) or (row % 2 == 0 and col % 2 ==1):
                    checker_pieces.append((row, col))
            else:
                checker_pieces.append((0, 0))

# Function to draw the checkers board
def draw_board():
  for row in range(8):
      for col in range(8):
          color = (255, 0, 0) if (row + col) % 2 == 0 else (0, 0, 0) #change color = (0, 0, 0) to 255,0,0
          rect = pygame.Rect(col * 50, row * 50, 50, 50)
          pygame.draw.rect(screen, color, rect)
          add_pieces()
          # Draw a checker piece if there is one at this position
          for piece_row, piece_col in checker_pieces:
              if piece_row == row and piece_col == col:
                  # Draw a circle to represent the checker piece
                  if row < 3:
                      pygame.draw.circle(screen, (255, 0, 0), (col * 50 + 25, row * 50 + 25), 20)
                  if row >4:
                      pygame.draw.circle(screen, (169, 169, 169), (col * 50 + 25, row * 50 + 25), 20)


def move_white():
    pass
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is over a node
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (mouse_x - checker_pieces[0][1]) ** 2 + (mouse_y - checker_pieces[0][1]) ** 2 <= 20 ** 2:
                dragging = True
                drag_node = 1

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                # Update the position of the dragged node
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if drag_node == 1:
                    checker_pieces[0] = (mouse_x, mouse_y)


        # Draw the board
        draw_board()
        pygame.display.update()

pygame.quit()
