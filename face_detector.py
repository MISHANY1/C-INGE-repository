import cv2
import glob
import face_recognition


def make_vid_face_det(full_video_name, video_fps, video_width, video_height):
    input_video = cv2.VideoCapture(full_video_name)

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    output_video = cv2.VideoWriter('output.avi', fourcc, video_fps, (video_width, video_height))

    face_locs = []

    while True:
        ret, frame = input_video.read()
        if not ret:
            break
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locs = face_recognition.face_locations(rgb_frame)
        for top, right, bottom, left in face_locs:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        output_video.write(frame)

    output_video.release()
    input_video.release()
    cv2.destroyAllWindows()
