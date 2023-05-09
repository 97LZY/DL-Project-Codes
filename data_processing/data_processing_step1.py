import os

def create_video_folder(video_dir):
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)
        print(video_dir+' does not exist, created!')

for i in range(1,81):
    if(i<=9):
        video_number = '0'+str(i)
    else:
        video_number = str(i)
    video_dir = 'frames-25fps-resize/video{}/'.format(video_number)
    create_video_folder(video_dir)
    video_dir = 'frames-1fps-resize/video{}/'.format(video_number)
    create_video_folder(video_dir)