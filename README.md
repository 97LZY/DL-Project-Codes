# DL-Project-Codes
The codes for EN.520.638 Final Project.

The link of Cholec80 dataset: http://camma.u-strasbg.fr/datasets.

Researchers need to fill the request for obtaining the completed Cholec80 and then can download it. For the convenience, we also offer the modified dataset we use in all experiments, and we put it in Google Drive for downloading: https://drive.google.com/file/d/1PnDFJvFNYPZVojCySe5pcppTrbyCAGKA/view?usp=share_link.

## To run the experiments successfully, we need to follow these steps:

###	1. Fill the request of Cholec80 and get the completed dataset with 80 videos and all the annotations we need.
### 2. Clone this repo
`git clone https://github.com/97LZY/DL-Project-Codes.git`
### 3. Run codes in data_processing folder step by step. 
#### a. First, create the folders of all videos using data_processing_step1.py.
#### b. Then, run the ffmpeg commands listed in data_processing_step2.py munally in terminal window to deal with the videos and generate all the 250x250 pixels images at 25 fps for every video under frames-25fps-1-resize folder created just now. One example:
`ffmpeg -i ./videos/video01.mp4 -r 25 -f image2 -s 250x250 ./frames-25fps-resize/video01/video01-%d.jpg`
#### c. Third, select the first frames in every 25 frames, put all the selected frames under frames-1fps-resize folder, and rename all frames under frames-1fps-resize according to the sequences. We can run data_processing_step3.py directly. After this step, we can get the modified dataset we use in all experiments. And we also offer the frames-1fps-resize folder directly if users don’t want to go through the data processing part using Cholec80.
### 4. We recommend that using Colab and Google Drive to continue the next steps if users cannot find a workstation with a strong GPU, and here we will only introduce the steps on Colab and Google Drive.
### 5. Upload the modified dataset to Google Drive and choose any ipynb file in the codes folder and two_networks_two_tasks folder to start. 
#### The ipynb files under codes folder are modified a little according to the codes in the paper [Multi-task recurrent convolutional network with correlation loss for surgical video analysis](https://github.com/YuemingJin/MTRCNet-CL#readme) , we replace some old grammar of PyTorch and make it run successfully on the environment of Colab machines. The ipynb files under two_networks_two_tasks are the models we implement ourselves.
### 6. Remember to care about all the paths in every ipynb files and modify the paths according to your arrangement.
### 7. Run every cell step by step in every ipynb, and it will go through the whole process successfully and get the expected results.

## Other Skills and Details:

### 1. We run data processing part on our personal computers, and then upload the obtained dataset which can be used directly to Google Drive. And then, all the experiments are run on Google Drive using Colab. We choose a Nvidia A100 GPU for computing all the experiments and try to occupy the full memory for faster speed. And the largest batch size is about 300.
### 2.The codes offered in [Multi-task recurrent convolutional network with correlation loss for surgical video analysis](https://github.com/YuemingJin/MTRCNet-CL#readme) were finished many years ago, and some grammars have not been useful and need to be replaced with newer edition of PyTorch.
### 3. Users need to care about all the paths in every file while running codes.
### 4. We find that the read speed and write speed of Google Drive are very large bottleneck in the whole process so that it is too slow to update the changes of every frame stored in Google Drive in time. And while we need to read the images according to the paths during training and testing, it will also be very slow because of the read speed of Google Drive. Therefore, we decide to generate the useful dataset in local personal machine and then upload the dataset to Google Drive, which can have a faster speed. Besides, while training and testing, we decide to copy the dataset zip file from Google Drive to the Colab machine. Though it may cost a little time while copying, it can avoid reading images from Google Drive so that it will speed up the whole process to a considerable degree.
### 5. We need to notice that the tool labels and phase labels are both starting from 0 in a 0-based system, but the name index of frames obtained after running ffmpeg commands is from 1. Therefore, we need to guarantee the images and their corresponding labels can keep in a line while data processing.
### 6. We ever tried using the python library of ffmpeg to avoid running commands in terminal window munually. However, we noticed that it would cost much more time using this method rather than running ffmpeg commands directly. For better efficiency, we decide to run ffmpeg commands manually. 
<br/>
Authors: Ziyang Liu (zliu142@jhu.edu) and Zijian Wu (zwu52@jhu.edu)
