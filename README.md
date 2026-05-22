# Student Performance Predictor Documentation

Welcome to the documentation for the Student Performance Predictor. This application is an end-to-end machine learning web app designed to predict a student's final academic performance based on their demographic background, study habits, and social life.

---

## 1. Overview
The project is divided into three main components:
1. **Frontend (User Interface):** A modern, responsive web interface where users input student data.
2. **Backend (Server & API):** A Python-based server that handles incoming data and serves web pages.
3. **Machine Learning (AI Model):** A pre-trained classification algorithm that evaluates the data to predict performance outcomes.

---

## 2. Technical Stack
* **Frontend:** HTML5, Vanilla CSS3 (Custom Professional SaaS Theme), Jinja2 Templating.
* **Backend:** Python 3, Flask Web Framework.
* **Machine Learning:** Scikit-Learn, NumPy, Pickle (for model serialization).

---

## 3. Machine Learning Algorithm

### How it Works
The AI model is a classification algorithm. This means it takes a variety of inputs (features) and categorizes the student into one of three predefined performance classes:
* **0 (Poor Performance)**
* **1 (Average Performance)**
* **2 (Excellent Performance)**

### Data Preprocessing
Before the model can make a prediction, the raw data entered by the user must be mathematically standardized. 
* We use a **Scaler** (`scaler_student_performance.pkl`), which normalizes the input data so that large numbers (like absences) don't unfairly overpower small numbers (like gender encoding).

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

---

## 4. Backend (The Server)

The backend is powered by **Flask**, a lightweight Python web framework. It acts as the bridge between the user's browser and the Machine Learning model.

### API Routes
The `app.py` file defines two main routes (URLs):

1. `GET /` (Home Route)
   * **Function:** Serves the main web page.
   * **Action:** When a user visits the site, Flask renders the `index.html` file, displaying the data entry form.

2. `POST /predict` (Prediction Route)
   * **Function:** Processes the form submission.
   * **Action:** 
     1. Extracts all 12 data fields from the HTML form.
     2. Converts the data into a NumPy array.
     3. Transforms the data using the pre-loaded Scaler.
     4. Feeds the scaled data into the Machine Learning Model to get a prediction.
     5. Translates the numerical prediction (0, 1, or 2) into human-readable text ("Poor", "Average", "Excellent").
     6. Renders `result.html` and passes the text string to the frontend for display.

---

## 5. Frontend (The User Interface)

The frontend is built to be modern, professional, and accessible.

### `index.html`
* Contains the input form. It uses HTML5 validation (`min`, `max`, `required`) to ensure the user provides clean data before it even reaches the server.
* Styled with a clean grid layout for easy readability.

### `result.html`
* The dynamic results page. It uses **Jinja2 templating** (e.g., `{{ prediction }}`) to inject the server's prediction directly into the HTML. 
* It uses conditional logic to display a specific icon (⚠️, 📊, 🏆) based on the result.

### `style.css`
* Implements a "SaaS" (Software as a Service) design language.
* Utilizes CSS Variables (`:root`) for easy color management.
* Features soft shadows, a clean off-white background, and a vibrant Royal Blue accent color for an engaging user experience.

---

## 6. Setup and Installation

To run this application locally:

1. **Install Dependencies:**
   Ensure Python is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Server:**
   Execute the Flask application:
   ```bash
   python app.py
   ```

3. **Access the App:**
   Open a web browser and navigate to `http://127.0.0.1:5000/`.
