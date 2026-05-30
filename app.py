import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
page_title="AI Career Predictor",
page_icon="🤖",
layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""

<style>

.stApp {
    background-color: #0f172a;
}

.big-title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #cbd5e1;
}

label {
    color: white !important;
    font-weight: bold !important;
}

.result-card {
    background: linear-gradient(135deg,#06b6d4,#2563eb);
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 0px 25px cyan;
}

</style>

""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
'<div class="big-title">🤖 AI CAREER PREDICTOR</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">Discover Your Future Career Using AI</div>',
unsafe_allow_html=True
)

st.write("")

# ---------------- QUESTIONS ----------------

col1, col2 = st.columns(2)

with col1:
maths = st.selectbox(
"📐 Do you like Mathematics?",
["Yes", "No"]
)

```
coding = st.selectbox(
    "💻 Do you like Coding?",
    ["Yes", "No"]
)

biology = st.selectbox(
    "🧬 Do you like Biology?",
    ["Yes", "No"]
)
```

with col2:
helping = st.selectbox(
"❤️ Do you like Helping People?",
["Yes", "No"]
)

```
creative = st.selectbox(
    "🎨 Are you Creative?",
    ["Yes", "No"]
)

teaching = st.selectbox(
    "🎤 Do you enjoy Teaching?",
    ["Yes", "No"]
)
```

st.write("")

# ---------------- PREDICT BUTTON ----------------

if st.button("🚀 Predict My Future Career"):

```
st.balloons()

if maths == "Yes" and coding == "Yes":
    career = "👨‍💻 SOFTWARE DEVELOPER"
    image = "Software.jpg"

elif biology == "Yes" and helping == "Yes":
    career = "👨‍⚕️ DOCTOR"
    image = "Doctor.jpg"

elif teaching == "Yes" and helping == "Yes":
    career = "👩‍🏫 TEACHER"
    image = "teacher.jpg"

elif creative == "Yes":
    career = "🎨 GRAPHIC DESIGNER"
    image = "designer.jpg"

else:
    career = "📚 EXPLORE MULTIPLE CAREERS"
    image = None

left, center, right = st.columns([1, 2, 1])

with center:

    st.markdown(
        f"""
        <div class="result-card">
            <h1 style="color:white;">{career}</h1>
            <h2 style="color:white;">🎉 AI HAS PREDICTED YOUR FUTURE 🎉</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if image:
        try:
            st.image(image, width=250)
        except:
            st.warning(f"Image not found: {image}")
```

# ---------------- FOOTER ----------------

with st.expander("🧠 How AI Works?"):
st.write("""
✔ Collects Data

✔ Finds Patterns

✔ Learns From Examples

✔ Makes Predictions

Artificial Intelligence learns from data and uses patterns to make smart decisions.
""")
