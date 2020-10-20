import tkinter as tk
import cv2     		# Import library of python Opencv
import numpy as np

top=tk.Tk(className='Edge detection')       # give name to the tkinter window

T=tk.Text(top, height=2, width=30)
T.pack()
T.insert(tk.END, "Hii Hello This is Harsh Nain")

top.geometry("300x300")     # change the size of tkinter window

top['bg']="#856ff8"	    # color of tkinter background

def edge_detection():
	cap=cv2.VideoCapture(0)			# capture frames from a camera

	while(1):

		ret, frame = cap.read()		# reads frames from a camera

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   # Hsv is best for object detection (Hue Saturation Value)

		# define range of red color in HSV
		lower_red = np.array([30,150,50])
		upper_red = np.array([255,255,180])

		mask = cv2.inRange(hsv, lower_red, upper_red)

		# Bitwise AND mask and original image
		res = cv2.bitwise_and(frame,frame, mask=mask)
		
		cv2.imshow('Original' ,frame) 		# Display original image

		edges = cv2.Canny(frame, 100,200)
	
		cv2.imshow('Edges', edges)		# Display edges in a frame

		k = cv2.waitKey(5) & 0xFF		# wait for Space key to stop (Decimal = 32)
		if k == 32:
			break
		
B = tk.Button(top, text = "Start", bg="blue", fg="white", command=edge_detection)
B.pack()
top.mainloop()			# Close the window
cv2.destroyAllWindows()

 