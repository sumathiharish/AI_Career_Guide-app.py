import streamlit as st

st.set_page_config(
page_title="AI Career Predictor",
page_icon="🤖",
layout="wide"
)

st.title("🤖 AI Career Predictor")
st.subheader("Discover Your Future Career Using AI")

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

st.success(career)

if image:
    st.image(image, width=300)
```

with st.expander("🧠 How AI Works?"):
st.write("""
Artificial Intelligence:

✔ Collects Data

✔ Finds Patterns

✔ Learns From Examples

✔ Makes Predictions
""")
