import numpy as np
import cv2
import os

my_filename = 'video.avi' 
frames_per_second = 24.0
my_res = '720p'


def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

#make_720p()
#change_res(4000,2000)

def rescale_frame(frame, percent=75):
     width = int(frame.shape[1] * percent/ 100)
     height = int(frame.shape[0] * percent/ 100)
     dim = (width, height)
     return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

def get_dims(cap,res = '1080p'):
	width, height = STD_DIMENSIONS['480p']
	if res in STD_DIMENSIONS:
		width, height = STD_DIMENSIONS[res]
	change_res(cap, width, height)
	return width, height

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      	return  VIDEO_TYPE[ext]
    else: 
    	return VIDEO_TYPE['avi']


cap = cv2.VideoCapture(0)
dims = get_dims(cap, res = my_res)
video_type_cv2 = get_video_type(my_filename)

out = cv2.VideoWriter(my_filename, video_type_cv2, frames_per_second, dims) #width, height

while True:
	ret, frame = cap.read()
	
	#frame = rescale_frame(frame, percent=25)
	
	out.write(frame)
	cv2.imshow('frame', frame) #imgshow
	
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#cv2.imshow('gray', gray) #imgshow
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()






