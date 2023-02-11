import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import pyttsx3
import face_recognition
import os
import numpy as np


path = "faceID/anh"  # biến đường dẫn tới file ảnh
image = [] # tạo list lưu ma chận của từng bức ảnh
className = [] #tạo list lưu tên sau khi đã cắt đuôi của từng bức ảnh
myList = os.listdir(path)
# print(myList)
 # Bước 1 :Load kho ảnh
for cl in myList: 
    # print(cl)
    curImg = cv2.imread(f"{path}/{cl}") # là phương thức đọc hình ảnh trả về giá trị "num array"(giá trị ma trận) của hình ảnh đó
    image.append(curImg) #thêm giá trị sau khi đọc của hình ảnh vào list "image"
    className.append(os.path.splitext(cl)[0]) # Cắt tên của file ảnh chỉ để lại tên, sau đó thêm tên vào danh sách tên "className"
    
    
# Bước 2: mã hóa kho ảnh
def Mahoa(images) :  # tạo hàm đưa list ảnh vào để mã hóa(hàm này đưa vào một tham số là list các hình ảnh sau khi đọc qua "imread")
    listMaHoa = [] #tạo một list để lưu giá trị sau khi mã hóa
    for img in images : #lặp qua danh sách ảnh(sau khi đọc qua Imread)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)# Chuyển định dạng hình ảnh từ màu BGR sang RGB(để có thể thao tác với hình ảnh)
        curMaHoa = face_recognition.face_encodings(img)[0]#mã hóa hình ảnh
        listMaHoa.append(curMaHoa) #thêm  ảnh sau khi mã hóa vào list
    return listMaHoa # giá trị trả về là list(danh sách) ảnh sau khi mã hóa

# tạo một danh sách sau khi đã mã hóa để sau này lấy nó làm tham số để so sánh khi bật cam lên
dsSauMaHoa = Mahoa(image) #gọi hàm mã hóa hình ảnh và truyền tham số là danh sách hình ảnh sau khi đã đọc ở trên
# print("ma hoa thanh con")







# Load the cascade classifier
face_cascade = cv2.CascadeClassifier('ChatGPT/haarcascade_frontalface_default.xml')

# Start capturing video from the default camera
cap = cv2.VideoCapture(0)

# Function that updates the frame and detect faces in it
def update_frame(frame, label):
    # Read the next frame from the video
    ret, frame = cap.read()
    
    # If a frame was successfully read
    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 220, 0), 2)
        
        # Convert the frame back to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the frame to a PIL image
        image = Image.fromarray(frame)
        # Convert the PIL image to a tkinter PhotoImage
        image = ImageTk.PhotoImage(image)
        # Update the label's image
        label.configure(image=image)
        # Store the PhotoImage so that it doesn't get garbage collected
        label.image = image
        # Call the function again after 1 millisecond
        label.after(1, update_frame, frame, label)

# Create the main window
root = tk.Tk()
root.title("Face Detection")
root.geometry("600x400")

# Create a label to display the video frame
frame = tk.Label(root)
frame.pack()

# Start updating the frame
root.after(0, update_frame, frame, frame)

# Start the main loop
root.mainloop()
