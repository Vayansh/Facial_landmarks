# Facial - Landmarks 
 
An easy library to get real-time facial landmarks at normal fps(30 fps) and can be saved in your pc, all just by calling one function.
# Function 
get_facial_landmarks(real_time = True,static_image_mode = False,
                         max_faces = 5,min_detection_confidence = 0.5,min_tracking_confidence = 0.5,
                         refine_landmarks = True,landmarks_connections = True,landmarks_color = (0,255,0),
                         landmarks_circle_radius = 1,landmarks_thickness = 1,
                         face_contours = True,save_to_dir = None)

## STATIC_IMAGE_MODE
If set to false, the solution treats the input images as a video stream. It will try to detect faces in the first input images, and upon a successful detection further localizes the face landmarks. In subsequent images, once all max_num_faces faces are detected and the corresponding face landmarks are localized, it simply tracks those landmarks without invoking another detection until it loses track of any of the faces. This reduces latency and is ideal for processing video frames. If set to true, face detection runs on every input image, ideal for processing a batch of static, possibly unrelated, images. Default to false.

## MAX_NUM_FACES
Maximum number of faces to detect. Default to 5.

## REFINE_LANDMARKS
Whether to further refine the landmark coordinates around the eyes and lips, and output additional landmarks around the irises by applying the Attention Mesh Model. Default to True.

## MIN_DETECTION_CONFIDENCE
Minimum confidence value ([0.0, 1.0]) from the face detection model for the detection to be considered successful. Default to 0.5.

## MIN_TRACKING_CONFIDENCE
Minimum confidence value ([0.0, 1.0]) from the landmark-tracking model for the face landmarks to be considered tracked successfully, or otherwise face detection will be invoked automatically on the next input image. Setting it to a higher value can increase robustness of the solution, at the expense of a higher latency. Ignored if static_image_mode is true, where face detection simply runs on every image. Default to 0.5.

## LANDMARK_CONNECTIONS 
It will connect the landmarks according to Mediapipe-facemesh-tasselation. If set to False, then only landmarks will be shown. 
Default is set to True

## LANDMARK_COLOR
It will take input as tuple of BGR color code. Default is set to Green. It will set the landmarks color to desired color

## LANDMARK_CIRCLE_RADIUS
It will take integer as a input. Default is set to 1. It will set the landmarks circle radius to desired color.

## LANDMARK_THICKNESS
It will take integer as a input. Default is set to 1. It will set the landmarks thickness to desired thickness.

## Facial_contours
It will display face contours which includes eyebrows linings and face linings as according to Mediapipe-face-contours. Default is set to True. 

## SAVE_TO_DIR 
It will save the image to specified directory on clicking the spacebar. Default is set to None, hence no Image will be saved.


# How to exit the Real-Time detection 
Press Enter or Esc key to exit the Real-time detector.




# Future Work
1) Detecting Face landmarks from images in directory using mediapipe library and making it into just one function call.
2) Making and saving of real-time Facial Landmarks detection.

# Used libraries
MediaPipe 
opencv-python
Numpy

