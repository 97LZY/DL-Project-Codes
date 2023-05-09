# DL-Project-Codes
The codes for EN.520.638 Final Project.

The link of Cholec80 dataset: http://camma.u-strasbg.fr/datasets.

Researchers need to fill the request for obtaining the completed Cholec80 and then can download it. For the convenience, we also offer the modified dataset we use in all experiments, and we put it in Google Drive for downloading: https://drive.google.com/file/d/1PnDFJvFNYPZVojCySe5pcppTrbyCAGKA/view?usp=share_link.

## To run the experiments successfully, we need to follow these steps:

###	1. Fill the request of Cholec80 and get the completed dataset with 80 videos and all the annotations we need.
### 2. Clone this repo
`git clone https://github.com/97LZY/DL-Project-Codes.git`
### 2. Run codes in data_processing folder step by step. 
#### a. First, create the folders of all videos using data_processing_step1.py.
#### b. Then, run the ffmpeg commands listed in data_processing_step2.py munally in terminal window to deal with the videos and generate all the 250x250 pixels images at 25 fps for every video under frames-25fps-1-resize folder created just now. One example:
`ffmpeg -i ./videos/video01.mp4 -r 25 -f image2 -s 250x250 ./frames-25fps-resize/video01/video01-%d.jpg`
#### c. Third, select the first frames in every 25 frames, put all the selected frames under frames-1fps-resize folder, and rename all frames under frames-1fps-resize according to the sequences. We can run data_processing_step3.py directly. After this step, we can get the modified dataset we use in all experiments. And we also offer the frames-1fps-resize folder directly if users don’t want to go through the data processing part using Cholec80.
### 3. We recommend that using Colab and Google Drive to continue the next steps if users cannot find a workstation with a strong GPU, and here we will only introduce the steps on Colab and Google Drive.
### 4. Upload the modified dataset to Google Drive and choose any ipynb file in the codes folder and two_networks_two_tasks folder to start. 
#### The ipynb files under codes folder are modified a little according to the codes in the paper [Multi-task recurrent convolutional network with correlation loss for surgical video analysis](https://github.com/YuemingJin/MTRCNet-CL#readme) , we replace some old grammar of PyTorch and make it run successfully on the environment of Colab machines. The ipynb files under two_networks_two_tasks are the models we implement ourselves.
### 5. Remember to care about all the paths in every ipynb files and modify the paths according to your arrangement.
### 6. Run every cell step by step in every ipynb, and it will go through the whole process successfully and get the expected results.

