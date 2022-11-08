import streamlit as st
import joblib
import numpy as np

# 헤드라인
st.write("# 보험료 예측")
st.write("### Insurance predict")
#이미지
st.image('https://www.google.com/imgres?imgurl=https%3A%2F%2Fas2.ftcdn.net%2Fv2%2Fjpg%2F02%2F38%2F67%2F33%2F1000_F_238673309_nqIr8os4FhvqRrzwwHbvmyhs5Z3AKRRx.jpg&imgrefurl=https%3A%2F%2Fstock.adobe.com%2Fimages%2Fhealth-insurance-man-standing-cross-legged-near-the-signed-health-insurance-policy-human-life-insurance-healthcare-concept-vector-illustration-in-flat-cartoon-style%2F238673309&tbnid=h6fWsSp8StYwvM&vet=12ahUKEwisr9bF0Z37AhXBd94KHTtNBDIQMygNegUIARDvAQ..i&docid=FCJR2SLKDnxoTM&w=1000&h=1000&q=insurance%20cartoon&ved=2ahUKEwisr9bF0Z37AhXBd94KHTtNBDIQMygNegUIARDvAQ')
# 첫번째 행
r1_col1, r1_col2, r1_col3 = st.columns(3)

age = r1_col1.number_input("age", step=1, value=23)

bmi = r1_col2.number_input("bmi", value=34.40)

children = r1_col3.number_input("children", step=1, value=0)

# 두번째 행
r2_col1, r2_col2, r2_col3 = st.columns(3)

r2_col1.write("smoker")
smoker = r2_col1.checkbox("")

sex_option = ("male", "female")
sex = r2_col2.selectbox("sex", sex_option)
is_male = sex_option[0] == sex

region_option = ('southwest', 'southeast', 'northwest', 'northeast')
region = r2_col3.selectbox("region", region_option)
is_southwest = region_option[0] == region
is_southeast = region_option[1] == region
is_northwest = region_option[2] == region

# 예측 버튼
predict_button = st.button("예측")

st.write("---")

# 예측 결과
if predict_button:
    model = joblib.load('first_model.pkl')

    pred = model.predict(np.array([[age, bmi, children, smoker * 1,
        is_male * 1, is_northwest * 1, is_southeast * 1, is_southwest * 1]]))

    st.metric("예측 보험료", pred[0])