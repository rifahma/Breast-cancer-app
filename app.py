import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import plotly.express as px

# Initialize session state variables
if 'history_diagnosed' not in st.session_state:
    st.session_state.history_diagnosed = ''
if 'history_biopsies' not in st.session_state:
    st.session_state.history_biopsies = ''
if 'history_family' not in st.session_state:
    st.session_state.history_family = ''
if 'symptoms_lumps' not in st.session_state:
    st.session_state.symptoms_lumps = ''
if 'symptoms_pain' not in st.session_state:
    st.session_state.symptoms_pain = ''
if 'symptoms_discharge' not in st.session_state:
    st.session_state.symptoms_discharge = ''
if 'symptoms_size_change' not in st.session_state:
    st.session_state.symptoms_size_change = ''
if 'symptoms_skin_change' not in st.session_state:
    st.session_state.symptoms_skin_change = ''
if 'screening_mammogram' not in st.session_state:
    st.session_state.screening_mammogram = ''
if 'screening_other_tests' not in st.session_state:
    st.session_state.screening_other_tests = ''
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def set_page(page):
    st.session_state.page = page

# Train a simple model (for demonstration purposes)
np.random.seed(42)
data = pd.DataFrame({
    'history_diagnosed': np.random.randint(0, 2, 100),
    'history_biopsies': np.random.randint(0, 2, 100),
    'history_family': np.random.randint(0, 2, 100),
    'symptoms_lumps': np.random.randint(0, 2, 100),
    'symptoms_pain': np.random.randint(0, 2, 100),
    'symptoms_discharge': np.random.randint(0, 2, 100),
    'symptoms_size_change': np.random.randint(0, 2, 100),
    'symptoms_skin_change': np.random.randint(0, 2, 100),
    'screening_mammogram': np.random.randint(0, 2, 100),
    'screening_other_tests': np.random.randint(0, 2, 100),
    'diagnosis': np.random.randint(0, 2, 100)
})

# Preprocessing
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Train a simple decision tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Streamlit app layout
st.title('Breast Cancer Risk Prediction App; Your First Entry For The First Handy Healthcare')

page = st.session_state.page

def show_home():
    st.image("https://homecare-aid.com/wp-content/uploads/2024/04/women-hands-holding-pink-breast-cancer-ribbon-stan-2022-12-16-07-16-23-utc-1-1024x682.jpg", use_column_width=True)
    st.write("""
    Welcome to the Breast Cancer Risk Prediction App. This tool helps you assess your risk factors and symptoms related to breast cancer. From here you access the app with some questions to predict your probability of breast cancer.
    
    Breast cancer is one of the most common cancers affecting women worldwide. Early detection and awareness of risk factors can significantly improve outcomes. This app aims to provide an easy way to assess your risk and understand the symptoms and preventive measures associated with breast cancer.
    
    Please note, this app is not a substitute for professional medical advice. Always consult with a healthcare provider for a comprehensive diagnosis and treatment plan.
    
    Here we provide the link for you as the resources and getting help from the worldwide support!
    ### Educational Resources
    - [Breast Cancer Information](https://www.cancer.org/cancer/breast-cancer.html)
    - [Preventive Measures](https://www.breastcancer.org/research-news/prevention)
    - [Support Groups](https://www.breastcancer.org/community/support)
    """)

    if st.button("Start Assessment"):
        set_page('Assessment')

def show_assessment():
    st.header('Personal and Family Medical History')
    st.session_state.history_diagnosed = st.selectbox(
        'Have you ever been diagnosed with breast cancer or any other type of cancer before?', ['', 'No', 'Yes'], key='history_diagnosed')
    st.session_state.history_biopsies = st.selectbox(
        'Have you had any previous breast biopsies or surgeries?', ['', 'No', 'Yes'], key='history_biopsies')
    st.session_state.history_family = st.selectbox(
        'Do you have a family history of breast cancer (e.g., mother, sister, daughter)?', ['', 'No', 'Yes'], key='history_family')
    
    st.header('Symptoms and Physical Changes')
    st.session_state.symptoms_lumps = st.selectbox(
        'Have you noticed any lumps or changes in your breast tissue?', ['', 'No', 'Yes'], key='symptoms_lumps')
    st.session_state.symptoms_pain = st.selectbox(
        'Have you experienced any pain or tenderness in your breasts?', ['', 'No', 'Yes'], key='symptoms_pain')
    st.session_state.symptoms_discharge = st.selectbox(
        'Do you have any nipple discharge or changes in the appearance of your nipples?', ['', 'No', 'Yes'], key='symptoms_discharge')
    st.session_state.symptoms_size_change = st.selectbox(
        'Have you observed any changes in the size, shape, or appearance of your breasts?', ['', 'No', 'Yes'], key='symptoms_size_change')
    st.session_state.symptoms_skin_change = st.selectbox(
        'Have you noticed any skin changes on your breasts, such as dimpling or redness?', ['', 'No', 'Yes'], key='symptoms_skin_change')
    
    st.header('Screening and Preventive Measures')
    st.session_state.screening_mammogram = st.selectbox(
        'Have you had a mammogram before, and if so, when was your last one?', ['', 'No', 'Yes'], key='screening_mammogram')
    st.session_state.screening_other_tests = st.selectbox(
        'Have you undergone any other breast cancer screening tests, such as MRI or ultrasound?', ['', 'No', 'Yes'], key='screening_other_tests')

    if st.button("Submit"):
        set_page('Results')

def show_results():
    input_data = pd.DataFrame({
        'history_diagnosed': [1 if st.session_state.history_diagnosed == 'Yes' else 0],
        'history_biopsies': [1 if st.session_state.history_biopsies == 'Yes' else 0],
        'history_family': [1 if st.session_state.history_family == 'Yes' else 0],
        'symptoms_lumps': [1 if st.session_state.symptoms_lumps == 'Yes' else 0],
        'symptoms_pain': [1 if st.session_state.symptoms_pain == 'Yes' else 0],
        'symptoms_discharge': [1 if st.session_state.symptoms_discharge == 'Yes' else 0],
        'symptoms_size_change': [1 if st.session_state.symptoms_size_change == 'Yes' else 0],
        'symptoms_skin_change': [1 if st.session_state.symptoms_skin_change == 'Yes' else 0],
        'screening_mammogram': [1 if st.session_state.screening_mammogram == 'Yes' else 0],
        'screening_other_tests': [1 if st.session_state.screening_other_tests == 'Yes' else 0]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.warning("Your responses indicate a higher risk of breast cancer. Please consult with a healthcare provider for a thorough evaluation.")
    else:
        st.success("Your responses indicate a lower risk of breast cancer. Keep up with regular screenings and preventive measures.")

    st.write("### Personalized Suggestions")
    suggestions = ["Maintain a healthy diet", "Exercise regularly", "Avoid smoking", "Limit alcohol intake"]
    for suggestion in suggestions:
        st.write(f"- {suggestion}")

    input_data_visual = input_data.T.reset_index()
    input_data_visual.columns = ['Feature', 'Value']
    fig = px.bar(input_data_visual, x='Feature', y='Value', title='User Input Data')
    st.plotly_chart(fig)

    if st.button("Go Home"):
        set_page('Home')

def show_feedback():
    st.header('Feedback')
    feedback = st.text_area("Please provide your feedback here:")
    if st.button('Submit Feedback'):
        st.write('Thank you for your feedback!')
        set_page('Home')

# Navigation
if page == 'Home':
    show_home()
elif page == 'Assessment':
    show_assessment()
elif page == 'Results':
    show_results()
elif page == 'Feedback':
    show_feedback()
