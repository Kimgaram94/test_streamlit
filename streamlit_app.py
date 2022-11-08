import streamlit as st
import joblib
import numpy as np

# 헤드라인
st.write("# 보험료 예측")
st.write("### Insurance predict")

#이미지
st.image('data:image/jpeg;base64,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', width = 150)
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