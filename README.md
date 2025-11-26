# 🎯 Face Recognition Attendance System

An automated attendance system using real-time face recognition powered by OpenCV and face_recognition library.

## 📸 How It Works
- Captures real-time video from webcam
- Detects and recognizes registered faces
- Automatically marks attendance in a CSV file

## 🔧 Tech Stack
- Python
- OpenCV
- face_recognition
- NumPy
- Pandas



# Smart Attendance Using Face Recognition

## 📌 Overview

Smart Attendance is an automated attendance marking application that uses **face recognition**. Instead of uploading multiple individual photos of students, the user simply uploads **one single photo** containing all student faces. The system automatically detects all faces in the image and marks attendance for each recognized student in an **Excel (XLSX) sheet**.

This dramatically reduces manual effort, improves accuracy, and speeds up the attendance process.

---

## 🚀 Features

* **Single Photo Input**: User uploads one group photo containing all students.
* **Automatic Face Detection**: The system detects all the faces present in the image.
* **Face Recognition**: Recognizes each student based on pre-registered face data.
* **Auto Attendance Marking**: Attendance is automatically stored in an Excel sheet.

---

## 🏗️ How It Works

1. **Upload Group Photo** containing all students.
2. System **detects all faces** in the image.
3. Each face is **compared with the stored dataset**.
4. Matched students get their **attendance marked automatically**.
5. Attendance is stored in an **Excel (XLSX)** file.

   

---

## 📁 Project Folder Structure

```
face_recognition/
├── apps/
│   ├── admin.py
│   ├── auth.py
│   ├── faculty.py
│   ├── home.py
│   ├── student.py
│   └── __pycache__/
│
├── faces/
│   └── ... (stored student face images)
│
│
├── templates/
│   ├── admin/
│   │   ├── add-faculty.html
│   │   └── add-student.html
│   │
│   ├── faculty/
│   │   ├── attendence-result.html
│   │── dashboard.html
│   │── get-attendance.html
│   │── insert.html
│   │── login.html
│   |── mark-attendance.html
│   |── result.html
│   
│   
│
├── utils/
│   ├── admin.py
│   ├── attendance.py
│   ├── insert.py
│   ├── query.py
│   
│
├── sample.xlsx
├── app.py

```

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **face_recognition library** 
* **Pandas**
* **Flask**
* **HTML, CSS** 

---
