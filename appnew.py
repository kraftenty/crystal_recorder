import cv2
from manager import ConstManager, FileManager, VideoManager


def main():
    videoCapture = VideoManager.getNewVideoCapture()

    if not videoCapture.isOpened():
        print('[ERROR] Cannot access webcam.')
        return

    recordingFlag = False
    reverseFlag = False
    videoWriter = VideoManager.getVideoWriter()
    
    while True:
        ret, frame = videoCapture.read()

        if not ret:
            print('[ERROR] Cannot read frame from webcam.')
            break

        if recordingFlag:
            if reverseFlag:
                frame = cv2.flip(frame, 1)
            videoWriter.write(frame)


        if recordingFlag:
            cv2.putText(frame, 'RECORDING', (200, 200), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 0, 255), lineType=cv2.LINE_AA)
        else:
            cv2.putText(frame, 'STANDBY', (200, 200), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 0, 0), lineType=cv2.LINE_AA)

        cv2.imshow(':::  Crystal Recorder  :::', frame)

        # 키 입력받기
        key = cv2.waitKey(1)
        if key == ConstManager.SPACE_KEY:
            recordingFlag = not recordingFlag
            if not recordingFlag:
                print('[INFO] Recording stopped.')
                videoWriter.release()
                previewSavedVideo(FileManager.getOutputFileName())
                FileManager.increaseFileOrderCount()
            elif recordingFlag:
                print('[INFO] Recording started.')
                videoWriter = VideoManager.getVideoWriter()
        elif key == ConstManager.ESC_KEY:
            break
        elif key == ConstManager.R_KEY:
            reverseFlag = not reverseFlag
            frame = cv2.flip(frame, 1)  # 현재 프레임에 반전 적용

    videoCapture.release()
    cv2.destroyAllWindows()

def previewSavedVideo(videoPath):
    videoCapture = VideoManager.getSavedVideoCapture(videoPath)

    if not videoCapture.isOpened():
        return

    while True:
        ret, frame = videoCapture.read()
        if not ret:
            break

        cv2.putText(frame, 'PREVIEW', (200, 200), cv2.FONT_HERSHEY_DUPLEX, 1.5 , (0, 255, 0), lineType=cv2.LINE_AA)
        cv2.imshow(':::  Crystal Recorder  :::', frame)

        if cv2.waitKey(1) == ConstManager.ESC_KEY:
            break

    videoCapture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
