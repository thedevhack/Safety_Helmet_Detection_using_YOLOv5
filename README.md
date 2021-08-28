# Safety_Helmet_Detection_using_YOLOv5

Create a Dataset of images(png/jpg) and labels(jpg) to it in YOLOv5 Format

YOLOv5 Format is shown Below

![alt text]https://user-images.githubusercontent.com/47482315/131216020-6ddb2d6f-82c7-4966-b6fa-101c582be7f3.png

The Folder Structure of Dataser Folder Should be like

Dataset
--images
----train
----validation
--labels
----train
----validation

After Placing the Images and Labels in the Dataset Folder

Edit the Config.Yaml file in our Repository

https://user-images.githubusercontent.com/47482315/131216143-13c960b5-838c-426f-b038-21d6fd45e11f.png

As in above image we can see the File contains 4 parameters to be changed 
1)Training images Path:This Should be something like "Project/Dataset/images/train"
1)Validation images Path:This Should be something like "Project/Dataset/images/validation"
3)Number of Classes:This Determines how many types of classes or objects we want to identify using YOLOv5
4)Names of Classes:This Contains names of all classes

After Doing this We need to install all the Required Modules used by YOLOv5 for its proper working using pip
The Command to be used in CLI to install all Modelues while being in our Project Directory will be: pip install -r requirements.txt

Now For Training The Model with your dataset just use this command:
python train.py --img 416 --batch 8 --epochs 100 --data config.yaml --cfg models/yolov5s.yaml --name run_name

In the above image the img value 416 Depends on the dimensions of the images you are using to train and validate and name can be anything you like and all other
parameters can also be changed.

After having a successful run of the above command we will have a new Folder named runs in which there will be a folder named same as the run_name you gave above in the command
Go in that folder and then go in Weights folder and copy the best.pt file in our main Project Directory

This File will be used to Detect the Hats(Objects)

Now using that Weights File we will run this Command
python detect.py --source "Path of the images in which you want to detect the Objects"  --weights best.pt

After Running this Command The Output images will be again in the runs Folder

The Diference Between Before Detection and After Can be seen below:
https://user-images.githubusercontent.com/47482315/131216590-bc881704-c599-4295-b60a-191fa65af33b.png
https://user-images.githubusercontent.com/47482315/131216617-065dd4d6-db68-4fec-8d7a-c0a2c2ce9c44.png

