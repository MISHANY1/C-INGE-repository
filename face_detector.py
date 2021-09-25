import cv2
import glob
import face_recognition


def make_vid_face_det(full_video_name):
    input_video = cv2.VideoCapture(full_video_name)
    fpc = input_video.get(cv2.cv.CV_CAP_PROP_FPS)
    width = input_video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = input_video.get(cv2.CAP_PROP_FRAME_HEIGHT)

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    output_video = cv2.VideoWriter('output.avi', fourcc, fpc, (width, height))

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


make_vid_face_det("sample_video.mp4", , , )