import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(
    page_title="Diabetes Risk Screening Tool | أداة الفحص المبكر لمخاطر السكري",
    page_icon="🩺",
    layout="centered"
)

# Sidebar - Language Selection
st.sidebar.header("🌐 Language / اللغة")
lang = st.sidebar.radio("Select Language / اختر اللغة:", ["العربية", "English"])

# Clean CSS Injection without hardcoded forced text colors on global elements
# This lets Streamlit automatically adapt text color to Light/Dark mode while styling custom boxes cleanly.
if lang == "العربية":
    st.markdown("""
        <style>
        .main { direction: rtl; text-align: right; }
        .stButton>button {
            width: 100%;
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            font-size: 18px !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            padding: 10px !important;
            border: none !important;
        }
        .stButton>button:hover {
            background-color: #1D4ED8 !important;
            color: #FFFFFF !important;
        }
        .disclaimer-box {
            background-color: #FFF5F5;
            color: #9B2C2C !important;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 24px;
            font-size: 15px;
            line-height: 1.6;
            border-right: 6px solid #E53E3E;
        }
        .result-high {
            background-color: #FFF5F5;
            color: #9B2C2C !important;
            padding: 18px;
            border-radius: 8px;
            border-right: 6px solid #E53E3E;
        }
        .result-low {
            background-color: #F0FDF4;
            color: #166534 !important;
            padding: 18px;
            border-radius: 8px;
            border-right: 6px solid #22C55E;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .main { direction: ltr; text-align: left; }
        .stButton>button {
            width: 100%;
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            font-size: 18px !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            padding: 10px !important;
            border: none !important;
        }
        .stButton>button:hover {
            background-color: #1D4ED8 !important;
            color: #FFFFFF !important;
        }
        .disclaimer-box {
            background-color: #FFF5F5;
            color: #9B2C2C !important;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 24px;
            font-size: 15px;
            line-height: 1.6;
            border-left: 6px solid #E53E3E;
        }
        .result-high {
            background-color: #FFF5F5;
            color: #9B2C2C !important;
            padding: 18px;
            border-radius: 8px;
            border-left: 6px solid #E53E3E;
        }
        .result-low {
            background-color: #F0FDF4;
            color: #166534 !important;
            padding: 18px;
            border-radius: 8px;
            border-left: 6px solid #22C55E;
        }
        </style>
    """, unsafe_allow_html=True)

# Load Model
@st.cache_resource
def load_model():
    try:
        model = joblib.load('diabetes_model.joblib')
        return model
    except Exception as e:
        err_msg = "لم يتم العثور على ملف النموذج 'diabetes_model.joblib'." if lang == "العربية" else "Model file 'diabetes_model.joblib' not found."
        st.error(err_msg)
        return None

model = load_model()

# Header & Disclaimer
if lang == "العربية":
    st.title("🩺 أداة الفحص المبكر لمخاطر مرض السكري")
    st.write("أداة مدعومة بالذكاء الاصطناعي تقدّر مستوى خطر الإصابة بمرض السكري بناءً على المؤشرات الصحية والسلوكية.")
    st.markdown("""
    <div class="disclaimer-box">
        <strong>⚠️ تنبيه طبي هام:</strong><br>
        هذا التطبيق هو أداة فحص مبدئي وتوعوي تم تطويرها لأغراض دراسية، وهي مخصصة للبالغين (18 سنة فما فوق). 
        النتائج المخرجة <strong>لا تُعد تشخيصاً طبياً رسمياً</strong> ولا تغني عن استشارة الطبيب المختص أو إجراء التحاليل المخبرية.
    </div>
    """, unsafe_allow_html=True)
    st.header("📋 أدخل البيانات الصحية")
else:
    st.title("🩺 Diabetes Risk Screening Tool")
    st.write("An AI-powered tool that estimates diabetes risk levels based on health and lifestyle indicators.")
    st.markdown("""
    <div class="disclaimer-box">
        <strong>⚠️ Important Medical Disclaimer:</strong><br>
        This application is an educational screening tool designed for adults (18+). 
        The results <strong>do NOT constitute an official medical diagnosis</strong> and cannot replace consultation with a healthcare professional or diagnostic lab tests.
    </div>
    """, unsafe_allow_html=True)
    st.header("📋 Enter Health Details")

# Help explanations for Age, Education, and Income
age_help_ar = """1: (18-24 سنة), 9: (60-64 سنة), 13: (80 سنة فما فوق).
ملاحظة: تدرج السن يبدأ من 18 سنة لأن نموذج التنبؤ مبني على بيانات المسح الصحي الوطني (CDC BRFSS) المخصص للبالغين."""

age_help_en = """1: (18-24 yrs), 9: (60-64 yrs), 13: (80+ yrs).
Note: Starts at 18 because the underlying CDC BRFSS dataset evaluates adult health indicators."""

edu_help_ar = """تدرج المستوى الدراسي (1-6):
1: لم يدرس / ابتدائية غير مكتملة
2: ابتدائية / إعدادية
3: ثانوي غير مكتمل
4: خريج مدرسة ثانوية
5: دبلوم / كلية متوسطة
6: خريج جامعي (4 سنوات فأكثر)"""

edu_help_en = """Education Level scale (1-6):
1: Never attended / Kindergarten
2: Elementary (Grades 1-8)
3: Some high school (Grades 9-11)
4: High school graduate
5: Some college / Technical school
6: College graduate (4+ years)"""

inc_help_ar = """تدرج مستوى الدخل السنوي للأسرة (1-8):
1: أقل من 10,000 دولار سنوياً (منخفض جداً)
5: 25,000 - 35,000 دولار سنوياً (متوسط)
8: 75,000 دولار أو أكثر سنوياً (مرتفع جداً)"""

inc_help_en = """Annual household income scale (1-8):
1: Less than $10,000/year (Very Low)
5: $25,000 to $35,000/year (Moderate)
8: $75,000 or more/year (Very High)"""

# Form Inputs
col1, col2 = st.columns(2)

if lang == "العربية":
    with col1:
        st.subheader("المؤشرات الأساسية")
        bmi = st.number_input("مؤشر كتلة الجسم (BMI):", min_value=10.0, max_value=60.0, value=25.0, step=0.5, help="الوزن بالكجم / (الطول بالمتر)²")
        age = st.slider("الفئة العمرية (من 1 إلى 13):", min_value=1, max_value=13, value=7, help=age_help_ar)
        gen_hlth = st.select_slider("تقييمك لصحتك العامة (GenHlth):", options=[1, 2, 3, 4, 5], value=3, format_func=lambda x: {1:"1 - ممتازة", 2:"2 - جيدة جداً", 3:"3 - جيدة", 4:"4 - مقبولة", 5:"5 - ضعيفة"}[x])
        high_bp = st.radio("هل تعاني من ضغط الدم المرتفع؟ (HighBP)", options=[0, 1], format_func=lambda x: "نعم" if x == 1 else "لا")
        high_chol = st.radio("هل تعاني من ارتفاع الكوليسترول؟ (HighChol)", options=[0, 1], format_func=lambda x: "نعم" if x == 1 else "لا")
        chol_check = st.radio("هل قمت بفحص الكوليسترول خلال الـ 5 سنوات الماضية؟", options=[0, 1], format_func=lambda x: "نعم" if x == 1 else "لا", index=1)

    with col2:
        st.subheader("التاريخ الطبي والسلوكيات")
        heart_disease = st.radio("هل لديك تاريخ لأمراض القلب أو الأزمات القلبية؟", options=[0, 1], format_func=lambda x: "نعم" if x == 1 else "لا")
        stroke = st.radio("هل أصبت بسكتة دماغية من قبل؟", options=[0, 1], format_func=lambda x: "نعم" if x == 1 else "لا")
        diff_walk = st.radio("هل تواجه صعوبة جدية في المشي أو صعود الدرج؟", options=[0, 1], format_func=lambda x: "نعم" if x == 1 else "لا")
        smoker = st.radio("هل دخنت أكثر من 100 سيجارة في حياتك؟", options=[0, 1], format_func=lambda x: "نعم" if x == 1 else "لا")
        phys_activity = st.radio("هل تمارس نشاطاً بدنياً خلال الـ 30 يوماً الماضية؟", options=[0, 1], format_func=lambda x: "نعم" if x == 1 else "لا", index=1)

    with st.expander("بيانات صحية واجتماعية إضافية"):
        col3, col4 = st.columns(2)
        with col3:
            phys_hlth = st.slider("عدد أيام المرض الجسدي خلال آخر 30 يوماً:", 0, 30, 0)
            ment_hlth = st.slider("عدد أيام المتاعب النفسية خلال آخر 30 يوماً:", 0, 30, 0)
            fruits = st.radio("تناول الفاكهة يومياً؟", [0, 1], format_func=lambda x: "نعم" if x == 1 else "لا", index=1)
            veggies = st.radio("تناول الخضروات يومياً؟", [0, 1], format_func=lambda x: "نعم" if x == 1 else "لا", index=1)
        with col4:
            hvy_alcohol = st.radio("استهلاك كحولي كبير؟", [0, 1], format_func=lambda x: "نعم" if x == 1 else "لا")
            any_healthcare = st.radio("هل لديك تغطية تأمين صحي؟", [0, 1], format_func=lambda x: "نعم" if x == 1 else "لا", index=1)
            no_doc_cost = st.radio("هل امتنعت عن زيارة الطبيب بسبب التكلفة؟", [0, 1], format_func=lambda x: "نعم" if x == 1 else "لا")
            sex = st.radio("الجنس:", [0, 1], format_func=lambda x: "أنثى" if x == 0 else "ذكر")
            education = st.slider("المستوى التعليمي (1-6):", 1, 6, 4, help=edu_help_ar)
            income = st.slider("مستوى الدخل (1-8):", 1, 8, 5, help=inc_help_ar)

else:
    with col1:
        st.subheader("Key Indicators")
        bmi = st.number_input("Body Mass Index (BMI):", min_value=10.0, max_value=60.0, value=25.0, step=0.5, help="Weight(kg) / Height(m)²")
        age = st.slider("Age Category (1 to 13):", min_value=1, max_value=13, value=7, help=age_help_en)
        gen_hlth = st.select_slider("General Health Rating (GenHlth):", options=[1, 2, 3, 4, 5], value=3, format_func=lambda x: {1:"1 - Excellent", 2:"2 - Very Good", 3:"3 - Good", 4:"4 - Fair", 5:"5 - Poor"}[x])
        high_bp = st.radio("High Blood Pressure? (HighBP)", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        high_chol = st.radio("High Cholesterol? (HighChol)", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        chol_check = st.radio("Cholesterol Checked in Past 5 Years?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No", index=1)

    with col2:
        st.subheader("Medical History & Lifestyle")
        heart_disease = st.radio("History of Heart Disease / Attack?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        stroke = st.radio("Ever had a Stroke?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        diff_walk = st.radio("Serious Difficulty Walking / Stairs?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        smoker = st.radio("Smoked > 100 Cigarettes in Life?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        phys_activity = st.radio("Physical Activity in Past 30 Days?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No", index=1)

    with st.expander("Additional Health & Socioeconomic Factors"):
        col3, col4 = st.columns(2)
        with col3:
            phys_hlth = st.slider("Physical Illness Days (past 30 days):", 0, 30, 0)
            ment_hlth = st.slider("Mental Health Issues Days (past 30 days):", 0, 30, 0)
            fruits = st.radio("Consume Fruit Daily?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", index=1)
            veggies = st.radio("Consume Vegetables Daily?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", index=1)
        with col4:
            hvy_alcohol = st.radio("Heavy Alcohol Consumption?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
            any_healthcare = st.radio("Have Health Insurance?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", index=1)
            no_doc_cost = st.radio("Could Not See Doctor Due to Cost?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
            sex = st.radio("Sex:", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
            education = st.slider("Education Level (1-6):", 1, 6, 4, help=edu_help_en)
            income = st.slider("Income Level (1-8):", 1, 8, 5, help=inc_help_en)

# Input DataFrame
input_data = pd.DataFrame([{
    'HighBP': high_bp,
    'HighChol': high_chol,
    'CholCheck': chol_check,
    'BMI': bmi,
    'Smoker': smoker,
    'Stroke': stroke,
    'HeartDiseaseorAttack': heart_disease,
    'PhysActivity': phys_activity,
    'Fruits': fruits,
    'Veggies': veggies,
    'HvyAlcoholConsump': hvy_alcohol,
    'AnyHealthcare': any_healthcare,
    'NoDocbcCost': no_doc_cost,
    'GenHlth': gen_hlth,
    'MentHlth': ment_hlth,
    'PhysHlth': phys_hlth,
    'DiffWalk': diff_walk,
    'Sex': sex,
    'Age': age,
    'Education': education,
    'Income': income
}])

st.markdown("---")

btn_label = "🔍 فحص مستوى الخطر الآن" if lang == "العربية" else "🔍 Check Risk Level Now"

if st.button(btn_label):
    if model is not None:
        try:
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]
            
            risk_prob = probability[1] if len(probability) == 2 else np.sum(probability[1:])
            
            if lang == "العربية":
                st.subheader("📊 نتيجة الفحص:")
                if prediction > 0 or risk_prob > 0.45:
                    st.markdown(f"""
                    <div class="result-high">
                        <h3>⚠️ هناك مؤشرات لاحتمالية عالية لمخاطر السكري</h3>
                        <p>نسبة الخطر التقديرية: <strong>{risk_prob*100:.1f}%</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.warning("نوصي بزيارة طبيب الأسرة أو إجراء فحص السكر التراكمي (HbA1c) للاطمئنان.")
                else:
                    st.markdown(f"""
                    <div class="result-low">
                        <h3>✅ المؤشرات الحالية تشير إلى مستوى خطر منخفض</h3>
                        <p>نسبة الخطر التقديرية: <strong>{risk_prob*100:.1f}%</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.success("أحسنت! حافظ على نمط حياتك الصحي والنشاط البدني والفحوصات الدورية.")
            else:
                st.subheader("📊 Screening Results:")
                if prediction > 0 or risk_prob > 0.45:
                    st.markdown(f"""
                    <div class="result-high">
                        <h3>⚠️ High Diabetes Risk Indicators Detected</h3>
                        <p>Estimated Risk Level: <strong>{risk_prob*100:.1f}%</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.warning("We recommend consulting a healthcare provider or getting an HbA1c lab test.")
                else:
                    st.markdown(f"""
                    <div class="result-low">
                        <h3>✅ Low Diabetes Risk Level Detected</h3>
                        <p>Estimated Risk Level: <strong>{risk_prob*100:.1f}%</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.success("Great job! Maintain a healthy lifestyle, regular activity, and periodic checkups.")

            st.progress(float(risk_prob))
            
            # Risk Factors Summary
            st.write("---")
            if lang == "العربية":
                st.write("### 🔑 أهم العوامل الملحوظة في مدخلاتك:")
                factors = []
                if high_bp == 1: factors.append("• وجود ضغط دم مرتفع")
                if high_chol == 1: factors.append("• ارتفاع مستوى الكوليسترول")
                if bmi >= 25: factors.append(f"• ارتفاع مؤشر كتلة الجسم ({bmi})")
                if gen_hlth >= 4: factors.append("• تدني التقييم العام للصحة")
                if heart_disease == 1: factors.append("• وجود تاريخ لأمراض القلب")
                if smoker == 1: factors.append("• التدخين")
                
                if factors:
                    for f in factors: st.write(f)
                else:
                    st.write("لم تظهر عوامل خطورة رئيسية بارزة في المدخلات الأساسية.")
            else:
                st.write("### 🔑 Key Risk Factors Noted:")
                factors = []
                if high_bp == 1: factors.append("• High Blood Pressure")
                if high_chol == 1: factors.append("• High Cholesterol")
                if bmi >= 25: factors.append(f"• Elevated BMI ({bmi})")
                if gen_hlth >= 4: factors.append("• Fair / Poor General Health Rating")
                if heart_disease == 1: factors.append("• History of Heart Disease")
                if smoker == 1: factors.append("• Smoking History")
                
                if factors:
                    for f in factors: st.write(f)
                else:
                    st.write("No major high-risk factors observed in primary inputs.")
                    
        except Exception as err:
            st.error(f"Error during prediction: {err}")