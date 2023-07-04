import cv2
from cryptography.fernet import Fernet
from tkinter import messagebox, simpledialog


def data_gather():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height
    face_detector = cv2.CascadeClassifier('Cascades/cascade.xml')
    # For each person, enter one numeric face id
    face_id = simpledialog.askinteger("ID", "Input a user ID (Number)")
    messagebox.showinfo("Data", "[INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' +
                        str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 30 face sample and stop video
             break

    face_id = str(face_id)

    with open('files/' + face_id + '.bin', 'w') as f:
        f.write('Hi')

    key = Fernet.generate_key()

    # string the key in a file
    with open("files/" + face_id + '.key', 'wb') as filekey:
        filekey.write(key)

    fernet = Fernet(key)

    # opening the original file to encrypt
    with open("files/" + face_id + ".bin", 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open("files/" + face_id + ".bin", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    cam.release()
    cv2.destroyAllWindows()
