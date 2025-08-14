import cv2
#sys.path.append(r"C:/Users\hp\Videos\Screen Recordings")
def new_func():
    cap = cv2.VideoCapture(r"C:\Users\hp\Videos\Screen Recordings\Screen Recording 2025-07-02 200722.mp4")
    return cap

cap = new_func()

# Open --> frames

while True:
    is_True, frame = cap.read()

    cv2.imshow("screenrecording", frame)
    

    cv2.waitKey(20)
