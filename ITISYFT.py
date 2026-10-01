import sys
from time import sleep
import pygame

pygame.mixer.init()
pygame.mixer.music.load("She & Him - I Thought I Saw Your Face Today (Official Lyric Video).mp3")
pygame.mixer.music.play()

def print_lyrics():
    # Danh sách (dòng chữ, thời gian delay giữa các ký tự, thời gian nghỉ sau khi xong dòng)
    lines = [
        ("I thought I saw your face today", 0.08, 0.8),
        ("But I just turned my head away", 0.08, 0.8),
        ("Your face against the trees", 0.07, 1.2),
        ("But I just see the memories as they come", 0.1, 1.3),
        ("As they come", 0.2, 1.1),
        ("And I couldn't help but fall in love again", 0.09, 2.2),
        ("No, I couldn't help but fall in love again", 0.09, 2.9),
        ("I saw it glitter as I grew", 0.1, 0.7),
        ("And loved it why I never knew", 0.1, 0.5),
        ("I thought this place was heaven sent", 0.06, 0.7),
        ("But now it's just a monument", 0.09, 0.2),
        ("In my mind", 0.2, 0.7),
        ("In my mind", 0.1, 2.0),
        ("And I couldn't help but fall in love again", 0.09, 2.2),
        ("No, I couldn't help but fall in love again", 0.09, 2.9),
    ]

    sleep(0.5)

    for line, char_delay, line_delay in lines:
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        print() # Xuống dòng
        sleep(line_delay)

try:
    print_lyrics()
    # Giữ chương trình chạy nếu nhạc chưa phát xong
    while pygame.mixer.music.get_busy():
        sleep(0.5)
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    sys.exit()