# Student Performance Predictor Documentation

Student Performance Predictor this application is an web app designed to predict a student's final academic performance based on their data.

## 1. Overview
The project is divided into three main components:
1. **Frontend (User Interface):** A web interface where users input student data.
2. **Backend (Server & API):** A Python-based server that handles incoming data and serves web pages.
3. **Machine Learning (AI Model):** A pre-trained classification algorithm that evaluates the data to predict performance outcomes.

## 2. Technical Stack
* **Frontend:** HTML5, CSS3.
* **Backend:** Python 3, Flask Web Framework.
* **Machine Learning:** Scikit-Learn, NumPy, Pickle.

## 3. Machine Learning Algorithm

### How it Works
The AI model is a classification algorithm. This means it takes a variety of inputs (features) and categorizes the student into one of three predefined performance classes:
* **0 (Poor Performance)**
* **1 (Average Performance)**
* **2 (Excellent Performance)**

### Data Preprocessing
Before the model can make a prediction, the raw data entered by the user must be mathematically standardized. 
* I used a **Scaler**, which normalizes the input data so that large numbers (like absences) don't unfairly overpower small numbers.

### Input Features
The algorithm requires 12 specific data points (features) to make an accurate prediction:
1. **Sex:** Gender of the student (Male = 1, Female = 0).
2. **Age:** Student's age.
3. **Mother's Education (Medu):** Graded from 0 (none) to 4 (higher education).
4. **Father's Education (Fedu):** Graded from 0 (none) to 4 (higher education).
5. **Mother's Job (Mjob):** Categorized numerically (Teacher, Health, Services, At Home, Other).
6. **Father's Job (Fjob):** Categorized numerically.
7. **Study Time:** Weekly study hours (1 to 4 scale).
8. **Free Time:** Free time after school (1 to 5 scale).
9. **Going Out:** Frequency of going out with friends (1 to 5 scale).
10. **Health:** Current health status (1 to 5 scale).
11. **Absences:** Total number of school absences.
12. **Previous Grade (G1):** The student's score in the first grading period (0 to 20 scale).

## 4. Backend (The Server)

The backend is powered by **Flask**, a lightweight Python web framework. It acts as the bridge between the user's browser and the Machine Learning model.
