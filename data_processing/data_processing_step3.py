import os
import shutil
from natsort import natsorted

# Select the first frame in every 25 frames, and put all the selected frames under frames-1fps-resize folder.
for i in range(1,81):
    if(i<=9):
        video_number = '0'+str(i)
    else:
        video_number = str(i)
    frames_25fps_resize_path = 'frames-25fps-resize/video{}/'.format(video_number)
    frames = os.listdir(frames_25fps_resize_path)
    frame_number=0
    for frame_index in range(len(frames)):
        if((frame_index%25 ==0) and ((frame_index+25)<=(len(frames)-1))):
            frame_number=frame_number+1
            shutil.copy('frames-25fps-resize/video{}/video{}-{}.jpg'.format(video_number,video_number,frame_index+1), 'frames-1fps-resize/video{}/'.format(video_number))
            #print('frames-25fps-resize/video{}/video{}-{}.jpg'.format(video_number,video_number,frame_index+1))
    print("video{}".format(video_number)+" : "+str(len(frames))+" frames ----> "+str(frame_number)+" frames")

# Rename all frames under frames-1fps-resize, and make the name according to the sequences.
for i in range(1,81):
    if(i<=9):
        video_number = '0'+str(i)
    else:
        video_number = str(i)
    print("--------------------")
    print("video number: "+video_number)
    print("--------------------")
    frames_1fps_resize_path = 'frames-1fps-resize/video{}/'.format(video_number)
    frames = os.listdir(frames_1fps_resize_path)
    frames_list=natsorted(frames)
    frame_number=0
    for frame_index in range(len(frames_list)):
        frame_number=frame_number+1
        if frame_number==1:
            print('frames-1fps-resize/video{}/{}'.format(video_number,frames_list[frame_index]) + "--->" +'frames-1fps-resize/video{}/video{}-{}.jpg'.format(video_number,video_number,frame_number))
        if frame_number==2:
            print('frames-1fps-resize/video{}/{}'.format(video_number,frames_list[frame_index]) + "--->" +'frames-1fps-resize/video{}/video{}-{}.jpg'.format(video_number,video_number,frame_number))
        if frame_number==3:
            print('frames-1fps-resize/video{}/{}'.format(video_number,frames_list[frame_index]) + "--->" +'frames-1fps-resize/video{}/video{}-{}.jpg'.format(video_number,video_number,frame_number))
            print("....................")
        if frame_number==len(frames_list):
            print('frames-1fps-resize/video{}/{}'.format(video_number,frames_list[frame_index]) + "--->" +'frames-1fps-resize/video{}/video{}-{}.jpg'.format(video_number,video_number,frame_number))
        os.rename('frames-1fps-resize/video{}/{}'.format(video_number,frames_list[frame_index]),'frames-1fps-resize/video{}/video{}-{}.jpg'.format(video_number,video_number,frame_number))