import os
import cv2
path = "Images"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in [ '.jpg']: 
        file_name = path+"/"+file
        print(file_name)
        images.append(file_name)
        
print(len(images))
count = len(images)

frame=cv2.imread(images[0])
height,width,Channels=frame.shape
size=(width,height)
print(size)
output=cv2.VideoWriter("project.avi",cv2.Vcv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count-1):
    frame=cv2.imread(images[i])
    output.write(frame)
    print("done")

