import cv2  # To install, enter in the console: pip install opencv-python. Also install dlib (pip install dlib).
import glob  # To install, enter in the console: pip install glob2.
import face_recognition  # To install, enter in the console: pip install face-recognition.
# You must also have pip installed.

def make_vid_face_det(full_video_name):
    # This function goes through the video frame by frame, finds faces on the frame,
    # draws a box around them and transfers the frame with the recognized faces to a new video file.

    input_video = cv2.VideoCapture(full_video_name)  # Video capture by the cv2 module.

    fpc = float(input_video.get(cv2.CAP_PROP_FPS))  # Finding video's FPS.

    width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))  # Finding the width of the video.

    height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Finding the height of the video.

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # The codec of the new video file is set.

    output_video = cv2.VideoWriter('output.avi', fourcc, fpc,
                                   (width, height))  # The parameters of the new video file are set.

    face_locs = []  # Creating a list of tuples with the coordinates of faces.

    while True:  # The main cycle of the program.

        ret, frame = input_video.read()  # Taking a frame from a video.

        if not ret:
            break  # The cycle is interrupted if there are no more frames.

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # The frame is converted to RGB (since it is standard for
        # the face_recognition module).

        face_locs = face_recognition.face_locations(
            rgb_frame)  # The coordinates of the faces are saved in the face_locs list.

        for top, right, bottom, left in face_locs: #A box is drawn around the found faces.
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        output_video.write(frame) #The processed frame is transferred to a new video file.

    output_video.release() #The program closes all the resources used by it.
    input_video.release()
    cv2.destroyAllWindows()


make_vid_face_det("sample_video.mp4") #Starting the function. As an argument - the full name of the source video file.
