import os
import datetime
import cv2

class ConstManager():
    ESC_KEY = 27
    SPACE_KEY = 32
    R_KEY = 114
    FPS = 24


class FileManager():
    fileOrderCount = 1
    dateTimeStr = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    @classmethod
    def getOutputDir(cls):
        if not os.path.exists(cls.dateTimeStr):
            os.makedirs(cls.dateTimeStr)
        return cls.dateTimeStr
    
    @classmethod
    def increaseFileOrderCount(cls):
        cls.fileOrderCount += 1

    @classmethod
    def getOutputFileName(cls):
        return os.path.join(cls.getOutputDir(), f'video_{cls.fileOrderCount}.avi')
    

class VideoManager():
    @classmethod
    def getNewVideoCapture(cls):
        return cv2.VideoCapture(0)
    
    @classmethod
    def getSavedVideoCapture(cls, videoPath):
        return cv2.VideoCapture(videoPath)

    @classmethod
    def getVideoWriter(cls):
        frame_width = int(cls.getNewVideoCapture().get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cls.getNewVideoCapture().get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = ConstManager.FPS
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        return cv2.VideoWriter(FileManager.getOutputFileName(), fourcc, fps, (frame_width, frame_height))