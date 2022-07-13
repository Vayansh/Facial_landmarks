import mediapipe as mp
import numpy as np
import cv2 as cv

facemesh = mp.solutions.face_mesh
face = facemesh.FaceMesh(static_image_mode = False,refine_landmarks = True,max_num_faces = 5,min_detection_confidence = 0.5)
draw = mp.solutions.drawing_utils
drawing_style = mp.solutions.drawing_styles

# drawing_spec = draw.DrawingSpec(thickness = 1, circle_radius = 1)
cam = cv.VideoCapture(0)

while True:
    success,frame = cam.read()
    
    if not success:
        break
    frame = cv.flip(frame,1)
    img = np.zeros_like(frame,dtype=np.float32)
    
    rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    outputs = face.process(rgb)
    
    if outputs.multi_face_landmarks:
        for output in outputs.multi_face_landmarks:
                draw.draw_landmarks(frame,output,facemesh.FACEMESH_TESSELATION,
                                    landmark_drawing_spec = draw.DrawingSpec(color = (0,255,0),thickness = 1,circle_radius = 1),
                                    connection_drawing_spec = drawing_style.get_default_face_mesh_tesselation_style())
                draw.draw_landmarks(frame,output,facemesh.FACEMESH_CONTOURS,landmark_drawing_spec = None,
                                    connection_drawing_spec = drawing_style.get_default_face_mesh_contours_style())
                draw.draw_landmarks(frame,output,facemesh.FACEMESH_IRISES,landmark_drawing_spec = None,
                                    connection_drawing_spec=drawing_style.get_default_face_mesh_iris_connections_style())
                
                draw.draw_landmarks(img,output,facemesh.FACEMESH_TESSELATION,
                                    landmark_drawing_spec = draw.DrawingSpec(color = (0,255,0),thickness = 1,circle_radius = 1),
                                    connection_drawing_spec = drawing_style.get_default_face_mesh_tesselation_style())
                draw.draw_landmarks(img,output,facemesh.FACEMESH_CONTOURS,landmark_drawing_spec = None,
                                    connection_drawing_spec = drawing_style.get_default_face_mesh_contours_style())
                draw.draw_landmarks(img,output,facemesh.FACEMESH_IRISES,landmark_drawing_spec = None,
                                    connection_drawing_spec=drawing_style.get_default_face_mesh_iris_connections_style())
                
                

    cv.imshow('landmarks',img)
    cv.imshow('frame',frame)
    key = cv.waitKey(1)
    
    if key%256 == 27:
        break
    
cam.release()
cv.destroyAllWindows()    