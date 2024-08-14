from mss import mss
import time
import pyautogui
import cv2 
import numpy as np
from ultralytics import YOLO
avg_fps=0
img = None
t0 = time.time()
n_frames = 1

model = YOLO('runs/detect/data/custom_data.yaml/weights/best.pt')

label_dict={1:"ct_body",2:"ct_head",3:"t_body",4:"t_head"}

sct = mss()
while True:
    img = np.array(sct.grab((0,0,1152,864)))    
    region_of_interest = img[:864, :1152 ,:3]   
    region_of_interest = np.ascontiguousarray(region_of_interest, dtype=np.uint8)
 
    
    # Run inference on the source
    results = model(region_of_interest)

    result_list=[]
    class_list=[]
    conf_list=[]

    k=0
    for result in results: 
        
        for class_name in result.boxes.cls:
            class_list.append(int(class_name))

        for id,box in enumerate(result.boxes.xyxy) : # box with xyxy format, (N, 4)
            if k==0:
                if label_dict[class_list[id]]=="t_head" or label_dict[class_list[id]]=="ct_head":
                    x1,y1,x2,y2=int(box[0]),int(box[1]),int(box[2]),int(box[3])
      
                    x_midpoint=int((x1+x2)/2)
                    y_midpoint=int((y1+y2)/2)
                    
                    pyautogui.moveTo(x_midpoint,y_midpoint)
                    pyautogui.click(x1+5,y1)
                    
                    cv2.rectangle(region_of_interest,(x1,y1),(x2,y2),(0,0,255),2)
                    cv2.putText(region_of_interest, str(avg_fps) , (20,50) , cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0), 1, cv2.LINE_AA)
                    k+=1

    #region_of_interest=cv2.cvtColor(region_of_interest,cv2.COLOR_RGB2BGR)
    cv2.imshow("Computer Vision", region_of_interest)

    # Break loop and end test
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
    elapsed_time = time.time() - t0
    avg_fps = (n_frames / elapsed_time)
    print("Average FPS: " + str(avg_fps))
    #cv2.putText(region_of_interest, str(avg_fps) , (50,50) , cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0), 3, cv2.LINE_AA)
    n_frames += 1
