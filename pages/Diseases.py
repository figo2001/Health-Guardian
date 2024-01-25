
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("Models/diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open("Models/heart_disease_model.sav",'rb'))

parkinsons_model = pickle.load(open("Models/parkinsons_model.sav", 'rb'))

breast_cancer_model=pickle.load(open("Models/Breast_cancer_model.prediction.sav",'rb'))

depression_model=pickle.load(open("Models/Depression_prediction.sav",'rb'))

lung_cancer=pickle.load(open("Models/lung_cancer_model.sav",'rb'))

kidney_model=pickle.load(open("Models/kidney_model.sav",'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Diseases Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction',
                           'Depression or Anxiety Prediction',
                           'Lung Cancer Prediction',
                           'Chronic Kidney Disease Prediction'],
                          icons=['activity','heart','person','award','emoji-frown','lungs','file-medical'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)





# Breast Cancer Page
if (selected == "Breast Cancer Prediction"):
    
    # page title
    st.title("Breast Cancer Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        mean_radius = st.number_input('mean radius')
        
    with col2:
        mean_texture = st.number_input('mean texture')
        
    with col3:
        mean_perimeter = st.number_input('mean perimeter')
        
    with col4:
        mean_area = st.number_input('mean area')
        
    with col5:
        mean_smoothness = st.number_input('mean smoothness')
        
    with col1:
        mean_compactness = st.number_input('mean compactness')
        
    with col2:
       mean_concavity = st.number_input('mean concavity')
        
    with col3:
        mean_concave_points = st.number_input('mean concave points')
        
    with col4:
        mean_symmetry = st.number_input('mean symmetry')
        
    with col5:
        mean_fractal_dimension = st.number_input('mean fractal dimension')
        
    with col1:
        radius_error = st.number_input('radius error')
        
    with col2:
        texture_error = st.number_input('texture error')
        
    with col3:
        perimeter_error = st.number_input('perimeter error')
        
    with col4:
        area_error = st.number_input('area error')
        
    with col5:
        smoothness_error = st.number_input('smoothness error')
        
    with col1:
        compactness_error = st.number_input('compactness error')
        
    with col2:
        concavity_error = st.number_input('concavity error')
        
    with col3:
        concave_points_error = st.number_input('concave points error')
        
    with col4:
        symmetry_error = st.number_input('symmetry error')
        
    with col5:
        fractal_dimension_error = st.number_input('fractal dimension error')
        
    with col1:
        worst_radius = st.number_input('worst radius')
        
    with col2:
        worst_texture = st.number_input('worst texture')
        
    with col3:
        worst_perimeter = st.number_input('worst perimeter')
        
    with col4:
        worst_area = st.number_input('worst area')
        
    with col5:
        worst_smoothness = st.number_input('worst smoothness')
    
    with col1:
        worst_compactness = st.number_input('worst compactness')
        
    with col2:
        worst_concavity = st.number_input('worst concavity')
        
    with col3:
       worst_concave_points = st.number_input('worst concave points')
        
    with col4:
        worst_symmetry = st.number_input('worst symmetry')
        
    with col5:
        worst_fractal_dimension = st.number_input('worst fractal dimension')
        
    
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        breast_prediction = breast_cancer_model.predict([[mean_radius, mean_texture, mean_perimeter, 
                                                          mean_area, mean_smoothness, mean_compactness,
                                                          mean_concavity,mean_concave_points,
                                                          mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,
                                                          area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
                                                          symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,
                                                          worst_area,worst_smoothness,worst_compactness,
                                                          worst_concavity,worst_concave_points,worst_symmetry,
                                                          worst_fractal_dimension]])                          
        
        if (breast_prediction[0] == 1):
          breast_cancer_diagnosis = "The person has Breast Cancer disease"
        else:
          breast_cancer_diagnosis = "The person does not have Breast Cancer disease"
        
    st.success(breast_cancer_diagnosis)








# Depression Prediction Page
if (selected == "Depression or Anxiety Prediction"):
    
    # page title
    st.title("Depression or Anxiety Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        Gender = st.number_input('Gender')
        
    with col2:
        Year = st.number_input('Year')
        
    with col3:
        cgpa = st.number_input('CGPA')
        
    with col4:
        Marriage = st.number_input('Marriage')
        
    with col5:
        Anxiety = st.number_input('Anxiety')
        
    with col1:
        Panic = st.number_input('Panic')
        
    with col2:
       Treatment = st.number_input('Treatment')

    with col3:
       Major = st.number_input('Major')
    
    with col4:
       Age = st.number_input('Age')
        
    
    # code for Prediction
    Depression_test_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Depression or Anxiety Test Result"):
        Depression_prediction = depression_model.predict([[Gender, Year, cgpa, 
                                                          Marriage, Anxiety, Panic,
                                                          Treatment,Major,Age]])                          
        
        if (Depression_prediction[0] == 1):
          Depression_test_diagnosis = "The person is Dipressed."
        else:
          Depression_test_diagnosis = "The person is not Dipressed."
        
    st.success(Depression_test_diagnosis)


    #Lung Cancer Prediction Page:

if(selected == "Lung Cancer Prediction"):
    
    #page title
    st.title("Lung Cancer Prediction using Machine Learning")

# getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        GENDER = st.number_input("GENDER")
        
    with col2:
        AGE = st.number_input("AGE")
    
    with col3:
        SMOKING = st.number_input("SMOKING")
    
    with col4:
        YELLOW_FINGERS = st.number_input("YELLOW_FINGERS")
    
    with col1:
        ANXIETY = st.number_input("ANXIETY")
    
    with col2:
        PEER_PRESSURE = st.number_input("PEER_PRESSURE")
    
    with col3:
        CHRONIC_DISEASE = st.number_input("CHRONIC DISEASE")
    
    with col4:
        FATIGUE = st.number_input("FATIGUE")
    
    with col1:
        ALLERGY = st.number_input("ALLERGY")
    
    with col2:
        WHEEZING = st.number_input("WHEEZING")
    
    with col3:
        ALCOHOL_CONSUMING = st.number_input("ALCOHOL CONSUMING")
    
    with col4:
        COUGHING = st.number_input("COUGHING")
    
    with col1:
        SHORTNESS_OF_BREATH = st.number_input("SHORTNESS OF BREATH")
    
    with col2:
        SWALLOWING_DIFFICULTY = st.number_input("SWALLOWING DIFFICULTY")
    
    with col3:
        CHEST_PAIN = st.number_input("CHEST PAIN")
    


# code for Prediction
    lung_cancer_result = " "
    
    # creating a button for Prediction
    
    if st.button("Lung Cancer Test Result"):
        lung_cancer_report = lung_cancer.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, 
                                                   PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY,
                                                     WHEEZING, ALCOHOL_CONSUMING, COUGHING, 
                                                     SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, 
                                                     CHEST_PAIN]])
        
        if (lung_cancer_report[0] == 0):
          lung_cancer_result = "Hurrah! You have no Lung Cancer."
        else:
          lung_cancer_result = "Sorry! You have Lung Cancer."
        
    st.success(lung_cancer_result)




    #Chronic Kidney Disease Prediction Page:

if(selected == "Chronic Kidney Disease Prediction"):
    
    #page title
    st.title("Kidney Disease Prediction using Machine Learning")

# getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        AGE = st.number_input("age")
        
    with col2:
        BLOOD_PRESSURE = st.number_input("blood_pressure")
    
    with col3:
        SPECIFIC_GRAVITY = st.number_input("specific_gravity")
    
    with col4:
        ALBUMIN = st.number_input("albumin")
    
    with col1:
        SUGAR = st.number_input("suger")
    
    with col2:
        RED_BLOOD_CELLS = st.number_input("red_blood_cells")
    
    with col3:
        PUS_CELL= st.number_input("pus_cell")
    
    with col4:
        PUS_CELL_CLUMPS = st.number_input("pus_cell_clumps")
    
    with col1:
        BACTERIA = st.number_input("bacteria")
    
    with col2:
        BLOOD_GLUCOSE_RANDOM = st.number_input("blood_glucose_random")
    
    with col3:
        BLOOD_UREA = st.number_input("blood_urea")
    
    with col4:
        SERUM_CREATININE = st.number_input("serum_creatinine")
    
    with col1:
        SODIUM = st.number_input("sodium")
    
    with col2:
        POTASSIUM = st.number_input("potassium")
    
    with col3:
        HAEMOGLOBIN = st.number_input("haemoglobin")

    with col4:
        PACKED_CELL_VOLUME = st.number_input("packed_cell_volume")

    with col1:
        WHITE_BLOOD_CELL_COUNT = st.number_input("white_blood_cell_count")

    with col2:
        RED_BLOOD_CELL_COUNT = st.number_input("red_blood_cell_count")

    with col3:
        HYPERTENSION = st.number_input("hypertension")

    with col4:
        DIABETES_MELLITUS = st.number_input("diabetes_mellitus")

    with col1:
        CORONARY_ARTERY_DISEASE = st.number_input("coronary_artery_disease")

    with col2:
        APPETITE = st.number_input("appetite")
    
    with col3:
        PEDA_EDEMA = st.number_input("peda_edema")

    with col4:
        AANEMIA = st.number_input("aanemia")
        
    


# code for Prediction
    kidney_disease_result = " "
    
    # creating a button for Prediction
    
    if st.button("Chronic Kidney Disease Test Result"):
        kidney_disease_report = kidney_model.predict([[AGE, BLOOD_PRESSURE, SPECIFIC_GRAVITY, ALBUMIN, SUGAR, 
                                                   RED_BLOOD_CELLS, PUS_CELL, PUS_CELL_CLUMPS, 
                                                   BACTERIA, BLOOD_GLUCOSE_RANDOM, BLOOD_UREA, 
                                                   SERUM_CREATININE, SODIUM, POTASSIUM, HAEMOGLOBIN, 
                                                   PACKED_CELL_VOLUME, WHITE_BLOOD_CELL_COUNT, 
                                                   RED_BLOOD_CELL_COUNT, HYPERTENSION, 
                                                   DIABETES_MELLITUS, CORONARY_ARTERY_DISEASE, 
                                                   APPETITE, PEDA_EDEMA, AANEMIA]])
        
        if (kidney_disease_report[0] == 0):
          kidney_disease_result = "You have Chronic Kidney Disease."
        else:
          kidney_disease_result = "The person is Fine."
        
    st.success(kidney_disease_result)