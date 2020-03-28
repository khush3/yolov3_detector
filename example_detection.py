from custom_helper import *


OUTPUT_SIZE = (1280,720)

############Classes to detect
CLASSES_TO_DETECT = ['bicycle', 'car', 'motorbike', 'truck', 'dog']


	

if __name__ == '__main__':

	CUDA = 0
	
	cfgfile = "cfg/yolov3.cfg"
	weightsfile = "yolov3.weights"


	model = Darknet(cfgfile)
	model.load_weights(weightsfile)
	model.net_info["height"] = 160
	inp_dim = int(model.net_info["height"])

	if CUDA:
		model.cuda()
	model.eval()


	
	frame = cv2.imread("test.jpg")#Give the frame here
	frame = cv2.resize(frame, OUTPUT_SIZE, interpolation = cv2.INTER_AREA)

	img, coordinates = yolo_output(frame.copy(),model, CLASSES_TO_DETECT, CUDA, inp_dim)
	
	print('Coordinates of detected objects:', coordinates)
	print('Coordinates returned in the format: [xmin, ymin, xmax, ymax]')

	cv2.imshow('yolo', img)
	cv2.imshow('original image', frame)

	cv2.waitKey(0)

	cv2.destroyAllWindows()