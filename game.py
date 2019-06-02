from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

ball_position = [3, 3]
ball_velocity = [1, 1]
bat_pos = 4

def draw_bat():
  sense.set_pixel(0, bat_pos, 255, 0, 0)
  sense.set_pixel(0, bat_pos+1, 255, 0, 0)
  sense.set_pixel(0, bat_pos-1, 255, 0, 0)
  
def move_up(event):
  global bat_pos
  if bat_pos > 1 and event.action=='pressed':
    bat_pos -= 1
    
def move_down(event):
  global bat_pos
  if bat_pos < 6 and event.action=='pressed':
    bat_pos += 1
    
def draw_ball():
  global ball_position
  # Draws the ball pixel
  sense.set_pixel(ball_position[0], ball_position[1], 255, 255, 255)
  # Moves the ball to the next position
  ball_position[0] += ball_velocity[0]
  ball_position[1] += ball_velocity[1]
    
  if ball_position[1] == 0 or ball_position[1] == 7:
    ball_velocity[1] = -ball_velocity[1]
  if ball_position[0] == 0 or ball_position[0] == 7:
    ball_velocity[0] = -ball_velocity[0]
  if ball_position[0] == 1 and bat_pos - 1 <= ball_position[1] <= bat_pos + 1:
    ball_velocity[0] = -ball_velocity[0]
        
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down


while True:
  sense.clear(0, 0, 0)
  draw_bat()
  draw_ball()
  sleep(0.25)

