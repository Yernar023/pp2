import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)
song = ["The Walking Dead","Better Call Saul","Breaking Bad"]
resume = pygame.image.load(r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\play-button.png")
stop = pygame.image.load(r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\pause.png")
prev_m = pygame.image.load(r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\back.png")
next_m = pygame.image.load(r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\next.png")
pause= [resume,stop]
music = [r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\The Walking Dead.mp3",r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\Better Call Saul.mp3",r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\Breaking Bad.mp3"]
current = 0
s = 1
pygame.mixer.music.load(music[current])
pygame.mixer.music.play()
MUSIC_END = pygame.USEREVENT+1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit() 
        elif event.type == MUSIC_END:
            current = (current + 1) % len(music)
            pygame.mixer.music.load(music[current])
            pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.unpause()
                s = 1
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.pause()
                s = 0
            elif event.key == pygame.K_RIGHT:
                current = (current + 1) % len(music)
                pygame.mixer.music.load(music[current])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current = (current - 1) % len(music)
                pygame.mixer.music.load(music[current])
                pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(MUSIC_END)
    screen.fill("White")
    text = font.render(song[current], True, "Black")
    screen.blit(text, (90, 50))
    screen.blit(pause[s],(175,100))
    screen.blit(prev_m,(100,100))
    screen.blit(next_m,(250,100))

    pygame.display.update()