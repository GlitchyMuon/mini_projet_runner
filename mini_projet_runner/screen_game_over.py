#modules nécessaires
import pgzrun
import pygame

#dimensions de la fenêtre et autre variable
WIDTH = 800
HEIGHT = 600
game_over = True



#def de la function `game_over_screen` qui affiche l'écran de fin de partie
def game_over_screen():
    screen.clear()
    screen.draw.text("Game Over !!", center=(WIDTH/2, HEIGHT/2), fontsize=70, color="red")
#autres éléments ajoutés à l'écran de fin de partie



#def function `update` qui vérifie si les conditions (if) de fin de partie sont remplies
def update():
    global game_over
    #pour vérifier les conditions de fin de partie => game_over mettre = True
    if game_over:
        game_over_screen()



#def function `draw` qui dessine les éléments à écran
def draw():
    if not game_over:
        #éléments jeu normal
        pass    

pgzrun.go()