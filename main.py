import pygame
import math
from Components.Point import Point
from Cube3D.Cube import Cube

# Cube setup
TOTAL_CUBE_POINTS = 8
SCALE = 100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ANGLE_X = 0
ANGLE_Y = 0
ANGLE_Z = 0
ROTATE_SPEED = 0.02
IMG_SCALE = (100, 100)



"""
        7-------6     
       / |     /|
      /  |    / |
     /   4---/--5
    3----/--2   /
    |   /   |  /
    |  /    | /
    | /     |/
    0-------1
    
    4 is origin, 4-5=x, 0-4=z, 4-7=y
    
    for image -> 7-4 left, 6-7 top, 6-5 right, 5-4 bottom 
"""

def connect_points(points):
    connect(0, 1, points)
    connect(0, 3, points)
    connect(0, 4, points)
    connect(1, 2, points)
    connect(1, 5, points)
    connect(2, 6, points)
    connect(2, 3, points)
    connect(3, 7, points)
    connect(4, 5, points)
    connect(4, 7, points)
    connect(6, 5, points)
    connect(6, 7, points)


def connect(pi, pj, points):
    pygame.draw.line(screen, 'black',
                     (points[pi][0], points[pi][1]), (points[pj][0], points[pj][1]))


if __name__ == '__main__':


    # Cube class
    cube_point_list: list[Point] = []

    # cube point 1
    cube_point_list.append(Point(-1, -1, 1))
    # cube point 2
    cube_point_list.append(Point(1, -1, 1))
    # cube point 3
    cube_point_list.append(Point(1, 1, 1))
    # cube point 4
    cube_point_list.append(Point(-1, 1, 1))
    # cube point 5
    cube_point_list.append(Point(-1, -1, -1))
    # cube point 6
    cube_point_list.append(Point(1, -1, -1))
    # cube point 7
    cube_point_list.append(Point(1, 1, -1))
    # cube point 8
    cube_point_list.append(Point(-1, 1, -1))

    # create Cube
    cube_a = Cube(cube_point_list)
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    clock = pygame.time.Clock()
    running = True

    # cube faces
    face_0 = pygame.image.load('./01.png').convert_alpha()

    # Pygame draw loop
    while running:
        # fill screen with color to clean last frame
        screen.fill((255, 255, 255))
        # Render stuff

        ANGLE_X += 0.01
        ANGLE_Y += 0.01
        ANGLE_Z += 0.01
        # calculate rotation
        rotated_points = cube_a.calculate_rotation(ANGLE_X, ANGLE_Y, ANGLE_Z)
        for rotated_point in range(len(rotated_points)):
            # print(f' rotated point = {rotated_points[rotated_point][0]}')
            pygame.draw.circle(screen, 'purple', (rotated_points[rotated_point][0], rotated_points[rotated_point][1]), 4)
        connect_points(rotated_points)

        x_origin = [rotated_points[4][0], rotated_points[4][1]]
        x_end = [rotated_points[5][0], rotated_points[5][1]]
        y_origin = [rotated_points[7][0], rotated_points[7][1]]
        y_end = [rotated_points[6][0], rotated_points[6][1]]
        z_origin = [rotated_points[0][0], rotated_points[0][1]]

        x_axis = pygame.draw.line(screen, 'red', (x_origin[0], x_origin[1]), (x_end[0], x_end[1]), 3)
        y_axis = pygame.draw.line(screen, 'green', (x_origin[0], x_origin[1]), (y_origin[0], y_origin[1]), 3)
        z_axis = pygame.draw.line(screen, 'blue', (x_origin[0], x_origin[1]), (z_origin[0], z_origin[1]), 3)
        # print(f'({abs((x_end[0] - x_origin[0]))}, {abs((y_origin[1] - x_origin[1]))})')
        # face_0 = pygame.transform.scale(face_0, (abs((x_end[0] - x_origin[0])), abs((y_origin[1] - x_origin[1]))))
        face_0 = pygame.transform.scale(face_0, IMG_SCALE)
        # for image -> 7-4 left, 6-7 top, 6-5 right, 5-4 bottom
        rect_0 = pygame.Rect(abs(y_origin[0] - x_origin[0]), abs(y_end[0] - y_origin[0]), IMG_SCALE[0], IMG_SCALE[1])
        """
        https://stackoverflow.com/questions/15022630/how-to-calculate-the-angle-from-rotation-matrix
        """
        #face_0 = pygame.transform.rotate(face_0, (math.atan2(cube_a.rotation_matrix_x[2][1], cube_a.rotation_matrix_x[2][2]))*180/math.pi)
        #face_0 = pygame.transform.rotate(face_0, (math.atan2(-(cube_a.rotation_matrix_y[2][0]),
                                                           # math.sqrt(((cube_a.rotation_matrix_y[2][1])**2) + (cube_a.rotation_matrix_y[2][2]**2))
                                                          #  ))*180/math.pi)
        #face_0 = pygame.transform.rotate(face_0, (math.atan2(cube_a.rotation_matrix_z[1][0], cube_a.rotation_matrix_x[0][0])*180/math.pi))
        #screen.blit(face_0, x_origin, rect_0)
        screen.blit(face_0, ([x_origin[0], x_end[0], y_origin[0], y_end[0]]))

        # Pool for events from pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            ANGLE_Y = ANGLE_X = ANGLE_Z = 0
        if keys[pygame.K_a]:
            ANGLE_Y += ROTATE_SPEED
        if keys[pygame.K_d]:
            ANGLE_Y -= ROTATE_SPEED
        if keys[pygame.K_w]:
            ANGLE_X += ROTATE_SPEED
        if keys[pygame.K_s]:
            ANGLE_X -= ROTATE_SPEED
        if keys[pygame.K_q]:
            ANGLE_Z -= ROTATE_SPEED
        if keys[pygame.K_e]:
            ANGLE_Z += ROTATE_SPEED

        clock.tick(60)  # 60 FPS
        pygame.display.update()
    pygame.quit()
