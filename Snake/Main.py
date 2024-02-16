import Global as g
import Input
import Snake
import Apple

g.pygame.init()
g.SCREEN.fill((255, 255, 255))


running = True
while running:
    running = Input.handle_input()
    
    Snake.draw()
    
    #debug segment positions
    #print(g.snake_body+["     Frame:"+str(Input.frame_count)])
    #testing commits from laptop

    g.pygame.display.flip()
    g.clock.tick(120)
    
g.pygame.quit()