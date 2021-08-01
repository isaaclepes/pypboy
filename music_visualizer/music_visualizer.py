# Credit to https://github.com/prtx/Music-Visualizer-in-Python/blob/master/music_visualizer.py
from numpy import fft
import pygame, sys, time

def __init__():

    # graphic interface dimensions
    width, height = 420, 360
    center = [width / 2, height / 2]
    pygame.mixer.init()

    # read amplitude and frequency of music file with defined frame skips

    frame_rate = 48000

    file_name = "./001.mp3"
    sound_file = pygame.mixer.Sound(file_name)
    amplitude = pygame.sndarray.array(sound_file)

    frame_skip = 500
    amplitude = amplitude[:, 0] + amplitude[:, 1]
    amplitude = amplitude[::frame_skip]
    frequency = list(abs(fft.fft(amplitude)))

    # scale the amplitude to 1/4th of the frame height and translate it to height/2(central line)
    max_amplitude = max(amplitude)
    for i in range(len(amplitude)):
        amplitude[i] = float(amplitude[i]) / max_amplitude * height / 4 + height / 2
    amplitude = [int(height / 2)] * width + list(amplitude)

    # initiate graphic interface and play audio piece
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    now = time.time()

    running = True
    while running:
        # visualizer animation starts here
        for i in range(len(amplitude[width:])):

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill([0, 0, 0])

            # the amplitude graph is being translated from both left and right creating a mirror effect
            prev_x, prev_y = 0, amplitude[i]
            num = 1
            for x, y in enumerate(amplitude[i + 1:i + 1 + width][::num]):
                pygame.draw.line(screen, [0, 255, 0], [prev_x * num, prev_y], [x * num, y], 1)
                # pygame.draw.line(screen, [0, 255, 0], [(prev_x * 5 - width / 2) * -1 + width / 2, prev_y],
                #                  [(x * 5 - width / 2) * -1 + width / 2, y], 1)
                prev_x, prev_y = x, y

            # time delay to control frame refresh rate
            while time.time() < now + 1.0000000000 / frame_rate * frame_skip:
                time.sleep(.00000000001)
            now = time.time()

            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    __init__()