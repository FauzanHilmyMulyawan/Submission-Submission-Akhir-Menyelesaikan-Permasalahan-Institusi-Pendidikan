# -*- coding: utf-8 -*-
"""Streamlit

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nDTEqkkvlRe1cnWDvaNPdDqhJUy_YNFI
"""

import pickle
import streamlit as st

student_model = pickle.load(open('student_model.pkl', 'rb'))

st.title('Prediksi performa student')

Marital_status = st.text_input('Input Marital Status')
Application_mode = st.text_input('Input Application Mode')
Application_order = st.text_input('Input Application Order')
Course = st.text_input('Input Course')
Daytime_evening_attendance = st.text_input('Input Daytime/Evening Attendance')
Previous_qualification = st.text_input('Input Previous Qualification')
Previous_qualification_grade = st.text_input('Input Previous Qualification Grade')
Nacionality = st.text_input('Input Nationality')
Mothers_qualification = st.text_input('Input Mother\'s Qualification')
Fathers_qualification = st.text_input('Input Father\'s Qualification')
Mothers_occupation = st.text_input('Input Mother\'s Occupation')
Fathers_occupation = st.text_input('Input Father\'s Occupation')
Admission_grade = st.text_input('Input Admission Grade')
Displaced = st.text_input('Input Displaced')
Educational_special_needs = st.text_input('Input Educational Special Needs')
Debtor = st.text_input('Input Debtor')
Tuition_fees_up_to_date = st.text_input('Input Tuition Fees Up To Date')
Gender = st.text_input('Input Gender')
Scholarship_holder = st.text_input('Input Scholarship Holder')
Age_at_enrollment = st.text_input('Input Age at Enrollment')
International = st.text_input('Input International Status')
Curricular_units_1st_sem_credited = st.text_input('Input Curricular Units 1st Semester Credited')
Curricular_units_1st_sem_enrolled = st.text_input('Input Curricular Units 1st Semester Enrolled')
Curricular_units_1st_sem_evaluations = st.text_input('Input Curricular Units 1st Semester Evaluations')
Curricular_units_1st_sem_approved = st.text_input('Input Curricular Units 1st Semester Approved')
Curricular_units_1st_sem_grade = st.text_input('Input Curricular Units 1st Semester Grade')
Curricular_units_1st_sem_without_evaluations = st.text_input('Input Curricular Units 1st Semester Without Evaluations')
Curricular_units_2nd_sem_credited = st.text_input('Input Curricular Units 2nd Semester Credited')
Curricular_units_2nd_sem_enrolled = st.text_input('Input Curricular Units 2nd Semester Enrolled')
Curricular_units_2nd_sem_evaluations = st.text_input('Input Curricular Units 2nd Semester Evaluations')
Curricular_units_2nd_sem_approved = st.text_input('Input Curricular Units 2nd Semester Approved')
Curricular_units_2nd_sem_grade = st.text_input('Input Curricular Units 2nd Semester Grade')
Curricular_units_2nd_sem_without_evaluations = st.text_input('Input Curricular Units 2nd Semester Without Evaluations')
Unemployment_rate = st.text_input('Input Unemployment Rate')
Inflation_rate = st.text_input('Input Inflation Rate')
GDP = st.text_input('Input GDP')

student_pred = ''

if st.button('Test Prediksi Student'):
  student_pred=student_model.predict([[Marital_status, Application_mode, Application_order, Course, Daytime_evening_attendance, Previous_qualification, Previous_qualification_grade, Nacionality, Mothers_qualification, Fathers_qualification, Mothers_occupation, Fathers_occupation, Admission_grade, Displaced, Educational_special_needs, Debtor, Tuition_fees_up_to_date, Gender, Scholarship_holder, Age_at_enrollment, International, Curricular_units_1st_sem_credited, Curricular_units_1st_sem_enrolled, Curricular_units_1st_sem_evaluations, Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade, Curricular_units_1st_sem_without_evaluations, Curricular_units_2nd_sem_credited, Curricular_units_2nd_sem_enrolled, Curricular_units_2nd_sem_evaluations, Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade, Curricular_units_2nd_sem_without_evaluations, Unemployment_rate, Inflation_rate, GDP]])

  if(student_pred[0] == 0):
    student_pred = 'Dropout'
  if(student_pred[0] == 1):
    student_pred = 'Graduate'
  else:
    student_pred = 'Enrolled'

  st.success(student_pred)
