

import cv2
import numpy as np

from keras.models import load_model
img_row,img_height,img_depth=32,32,3
classifier=load_model('/content/Cifar10_model.h5')
color=True
scale=8

def draw_test(name,res,input_im,scale,img_row,img_height):
  BLACK=[0,0,0]
  res=int(res)
  if res==0:
    pred='airplane'
  if res==1:
    pred='automobile'
  if res==2:
    pred='bird'
  if res==3:
    pred='cat'
  if res==4:
    pred='deer'
  if res==5:
    pred='dog'
  if res==6:
    pred='frog'
  if res==7:
    pred='hourse'
  if res==8:
    pred='ship'
  if res==9:
    pred="truck"

  expanded_img=cv2.copyMakeBorder(input_im,0,0,0,imageL.shape[0]*2,cv2.BORDER_CONSTANT,value=BLACK)
  if color==False:
    expanded_img=cv2.cvtColor(expanded_img,cv2.COLOR_BAYER_GRAY2BGR)
  cv2.putText(expanded_img,str(pred),(300,30),cv2.FONT_HERSHEY_COMPLEX,SMALL,3,(0,255,0),2)
  cv2.imshow(name,expanded_img)

for i in range(0,10):
  rand=np.random.randint(0,len(x_test))
  input_im=x_test[rand]
  imageL=cv2.resize(input_im,None,fx=scale,fy=scale,interpolation=cv2.INTER_CUBIC)
  input_im=input_im.reshape(1,img_row,img_height,img_depth)


  #prediction
  res=str(classifier.predict_classes(input_im,1,verbose=0[0]))


  draw_test=('Prediction',res,imageL,scale,img_row,img_height)
  cv2.waitKey(0)



cv2.destroyAllWindows()
