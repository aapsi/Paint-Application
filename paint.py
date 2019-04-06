#self implementing paint application
import cv2
import numpy as np

brush = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\images\\brush_r1.png',3)#paint brush icon
eraser = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\images\eraser1.png',3)#eraser icon
plus = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\images\plus.png',3)#to reduce the brush or eraser size
minus = cv2.imread('C:\\Users\Hp\PycharmProjects\opencv\images\minus.png',3)# to increase the brush or eraser size
canvas = np.ones([1000,1000,3],'uint8')*255#white colored canvas
canvas[0:30,0:1000] = (0,0,0)#space for adding icons

color = (0,0,0)#default brush color(black)
line_width = -1
radius = 5
size = 0
pressed = False
erased = False
brushed = False
#clicking in the following region mentioned will help switching  between the functions
canvas[0:20,0:20] = brush
canvas[0:20,40:60] = eraser
canvas[0:20,80:100] = (0,0,255) #red color
canvas[0:20,120:140] = (255,0,0)#blue color
canvas[0:20,160:180] = (0,255,0)#green color
canvas[0:20,200:220] = plus
canvas[0:20,240:260] = minus

# click function to define what to do when mouse is clicked
def click(event,x,y,flags,param):
    global point,pressed,color,erased,radius,brushed,size#declaring global variable

    if event == cv2.EVENT_LBUTTONDOWN:
        if y in range(0,20) and x in range(0,20):#to select brush
            brushed = np.invert(brushed)
            erased = False

        if y in range(0,20) and x in range(40,60):#to select eraser
            erased = np.invert(erased)
            brushed = False

        if y in range(0,20) and x in range(80,100):#to change color of brush to red
            color = (0,0,255)
        if y in range(0,20) and x in range(120,140):#to change color of brush to red
            color = (255,0,0)
        if y in range(0,20) and x in range(160,180):#to change color of brush to red
            color = (0,255,0)
        if y in range(0,20) and x in range(200,220):#to increase the size of brush
            size += 3
        if y in range(0,20) and x in range(240,260):#to decrese the size of brush
            if size >0:
                size -= 3
            else:
                size = size

    if y in range(70, 1001):
        #various functions for brush
        # left click on mouse
        # if mouse is clicked in a particular region where a function is present then the following fuction is set to True and
        # if mouse is left idle, then brushed is false and the fuction returns
        # if the mouse is click + drag, then brushed is set to true and the drag function works from next iteration
        # while if the mouse was not clicked, or no pressed, then drag is not functional because of the If statement in the loop
        if brushed == True:
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                cv2.circle(canvas, (x,y), radius + size, color, line_width)

            if event == cv2.EVENT_MOUSEMOVE and pressed:
                cv2.circle(canvas, (x,y), radius + size, color, line_width)

            if event == cv2.EVENT_LBUTTONUP:
                pressed = False

        if erased == True:
            color1 = (255,255,255)
            if event == cv2.EVENT_LBUTTONDOWN:
                pressed = True
                cv2.circle(canvas, (x,y), radius+size, color1, line_width)

            elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
                cv2.circle(canvas, (x, y), radius+size, color1, line_width)
            elif event == cv2.EVENT_LBUTTONUP:
                pressed = False

cv2.namedWindow('frame')
cv2.setMouseCallback('frame',click)#this will respond to mouse clicks

while(True):
    cv2.imshow("frame",canvas)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):#press q to quit the screen
        break

cv2.destroyAllWindows()
