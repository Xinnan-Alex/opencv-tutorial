from turtle import width
import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Works for Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # works for only Live Videos (webcam or any video capture device)
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread("resources/Photos/cat.jpg")
cv.imshow("Cat", img)

cv.imshow("Resized Image", rescaleFrame(img))

# cv.waitKey(0)

capture = cv.VideoCapture("resources/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
