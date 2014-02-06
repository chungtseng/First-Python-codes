import random
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Ball(games.Sprite):
        
    quit_label = games.Text(value = "Press Q to Quit", size = 25, color = color.white, top = 5, right = 130,
                              is_collideable = False)
    games.screen.add(quit_label)

    def update(self):
        if self.right > games.screen.width:
            self.dx = -self.dx

        if self.left < 0:
            self.game_over()
            
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy

        #pressing 'q' quits the game
        if games.keyboard.is_pressed(games.K_q):
            self.game_over()

    def bounce(self):
        self.dx = -self.dx
        

    def game_over(self):
        """ End the game. """
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 3 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)
        self.destroy()

class Paddle(games.Sprite):
    image = games.load_image("paddle.bmp")

    score = games.Text(value = 0, size = 25, color = color.white, top = 15, 
        right = games.screen.width - 10, is_collideable = False)
    games.screen.add(score)

    def __init__(self):
        super(Paddle, self).__init__(image = Paddle.image, x = games.mouse.x, bottom = games.screen.height)
        
    def update(self):
        """ Move to mouse y position. """
        self.y = games.mouse.y
        
        if self.left > 0:
            self.left = 10
                
        if self.right > games.screen.height:
            self.right = games.screen.height

        self.check_catch()

    def check_catch(self):
        for ball in self.overlapping_sprites:
            Paddle.score.value += 1
            ball_image2 = games.load_image("ball.bmp")
            ball2 = Ball(image = ball_image2,
                      x = games.screen.width/2,
                      y = games.screen.height/2,
                      dx = 1,
                      dy = 1)
            games.screen.add(ball2)
            ball.bounce()


    
def main():
    wall_image = games.load_image("background.bmp", transparent = False)
    games.screen.background = wall_image

    ball_image = games.load_image("ball.bmp")
    the_ball = Ball(image = ball_image,
                      x = games.screen.width/2,
                      y = games.screen.height/2,
                      dx = 1,
                      dy = 1)
    games.screen.add(the_ball)

    the_paddle = Paddle()
    games.screen.add(the_paddle)

    games.mouse.is_visible = False

    games.screen.mainloop()

# kick it off!
main()
