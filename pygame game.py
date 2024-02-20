# Importar todos los módulos necesarios

import pygame
import time
import random
pygame.font.init()


# Definir las variables que no cambian es decir son constantes
width, height = 1000, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Dodge")

bg = pygame.transform.scale(pygame.image.load("download.jpg"), (width, height))

player_width = 40
player_height = 60

player_vel = 5
star_width = 10
star_height = 20
star_vel = 3

font = pygame.font.SysFont("comicsans", 30)
font2 = pygame.font.SysFont("comicsans", 60)

# Definir la función para dibujar instancias
def draw(player, elapsed_time, stars):
    win.blit(bg, (0, 0))

    time_text = font.render(f"Time: {round(elapsed_time)}s", 1, "white")
    win.blit(time_text, (10, 10))

    pygame.draw.rect(win, "red", player)

    for star in stars:
        pygame.draw.rect(win, "white", star)

    pygame.display.update()

# Definir la función principal
def main():
    # Definir todas las variables necesarias para la ejecución de la función
    run = True

    player = pygame.Rect(width / 2, height - player_height,player_width, player_height)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    # Hacer que el código se repita por siempre
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        # Crear los proyectiles
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, width - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)

                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        # Ver si el usuario cierra la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # Comprobar si teclas específicas estan siendo presionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel >= 0 or keys[pygame.K_a] and player.x - player_vel >= 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player_width <= width or keys[pygame.K_d] and player.x + player_vel + player_width <= width:
            player.x += player_vel
        
        # Mover los proyectiles hacia abajo
        for star in stars[:]:
            star.y += star_vel
            if star.y > height:
                stars.remove(star)
            elif star.y + star_height >= player.y  and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        # Reproducir texto de Game Over en la ventana
        if hit:
            lost_text = font2.render(f"You lost!", 1, "white")
            win.blit(lost_text, (width / 2 - lost_text.get_width() / 2, height / 2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break         

        draw(player, elapsed_time, stars)

    pygame.quit()

# Comprobar si el codigo se ejecuta directamente y no se está importando
if __name__ == "__main__":
    main()
