import os
import easygui

filename = easygui.fileopenbox()

if '.mkv' in filename != -1:
    print('Convertendo MKV')
    os.system('ffmpeg -i "{}" -codec copy "{}.mp4"'.format(filename, filename.replace('.mkv', '')))
    filename = filename.replace('.mkv', '.mp4')

print('Convertendo para DIVx')
os.system('ffmpeg -i "{}" -c:v mpeg4 -q:v 5 -tag:v DIVX -s 320x240 -c:a libmp3lame -q:a 5 -ac 2 -ar 44100 "{}.avi"'.format(filename, filename))