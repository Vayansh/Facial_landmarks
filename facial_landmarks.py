import mediapipe as mp
import cv2 as cv
import numpy as np

def get_facial_landmarks(real_time = True,static_image_mode = False,
                         max_faces = 5,min_detection_confidence = 0.5,min_tracking_confidence = 0.5,
                         refine_landmarks = True,landmarks_connections = True,landmarks_color = (0,255,0),
                         landmarks_circle_radius = 1,landmarks_thickness = 1,
                         face_contours = True,save_to_dir = None,video = False):
    
    # If refine landmarks is True only then you can have Irises landmarks     
    # Face contours include eyebrows lining and face linings 
    
    
    facemesh = mp.solutions.face_mesh
    face = facemesh.FaceMesh(static_image_mode = static_image_mode,refine_landmarks = refine_landmarks,
                            max_num_faces = max_faces,min_detection_confidence = min_detection_confidence,
                            min_tracking_confidence = min_tracking_confidence)
    draw = mp.solutions.drawing_utils
    drawing_style = mp.solutions.drawing_styles
    # drawing_spec = draw.DrawingSpec(thickness = landmarks_thickness, circle_radius = landmarks_circle_radius,color = landmarks_color)
    
    if real_time:                                               # for real- time face detection
            cam = cv.VideoCapture(0)
            i = 1
            while True:
                success, frame = cam.read()
                
                if not success:
                    break
                
                frame = cv.flip(frame,1)
                img = np.zeros_like(frame,dtype=np.float32)
                
                rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
                outputs = face.process(rgb)        
                
                if outputs.multi_face_landmarks:
                    for output in outputs.multi_face_landmarks:
                            # detection on camera image
                            if landmarks_connections:
                                draw.draw_landmarks(frame,output,facemesh.FACEMESH_TESSELATION,
                                                    landmark_drawing_spec = draw.DrawingSpec(color = landmarks_color,thickness = landmarks_thickness, circle_radius = landmarks_circle_radius),
                                                    connection_drawing_spec = drawing_style.get_default_face_mesh_tesselation_style())
                            else:
                                draw.draw_landmarks(frame,output)
                            
                            if face_contours:    
                                draw.draw_landmarks(frame,output,facemesh.FACEMESH_CONTOURS,landmark_drawing_spec = None,
                                                    connection_drawing_spec = drawing_style.get_default_face_mesh_contours_style())
                            if refine_landmarks:    
                                draw.draw_landmarks(frame,output,facemesh.FACEMESH_IRISES,landmark_drawing_spec = None,
                                                connection_drawing_spec=drawing_style.get_default_face_mesh_iris_connections_style())
                            
                            
                            # detection on black background
                            if landmarks_connections:
                                draw.draw_landmarks(img,output,facemesh.FACEMESH_TESSELATION,
                                                    landmark_drawing_spec = draw.DrawingSpec(thickness = landmarks_thickness, circle_radius = landmarks_circle_radius,color = landmarks_color),
                                                    connection_drawing_spec = drawing_style.get_default_face_mesh_tesselation_style())
                            else:
                                draw.draw_landmarks(img,output)
                            
                            if face_contours:    
                                draw.draw_landmarks(img,output,facemesh.FACEMESH_CONTOURS,landmark_drawing_spec = None,
                                                    connection_drawing_spec = drawing_style.get_default_face_mesh_contours_style())
                            if refine_landmarks:
                                draw.draw_landmarks(img,output,facemesh.FACEMESH_IRISES,landmark_drawing_spec = None,
                                                connection_drawing_spec=drawing_style.get_default_face_mesh_iris_connections_style())
                            
            
                # showing landmarks images 
                cv.imshow('landmarks',img)
                cv.imshow('Camera',frame)
                key = cv.waitKey(1)
                
                if key%256 == 27 or key%256 == 13:                     # Enter and Esc key to exit or to end real time detection
                    break                
                elif key%256 == 32 and save_to_dir is not None: 
                    cv.imwrite(save_to_dir.strip()+f'/face_{i}.png',frame)
                    cv.imwrite(save_to_dir.strip()+f'/landmarks_{i}.png',img)
                    i += 1 
                    
            
            cam.release()
            cv.destroyAllWindows()
            
    
 
                        