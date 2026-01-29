import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.let_it_rain import rain

#Add fun popup 
rain(
     emoji="🧬",
    font_size=80,
    falling_speed=4,
    animation_length=2,)

# Set page configuration
st.set_page_config(
    page_title="Rachel van Duyn | Portfolio",
    page_icon="🧬",
)

# Title of the app
st.title("Bioinformatics MSc | Cancer Research | Teaching")


# Collect basic information
name = "Rachel van Duyn"
field = "Bioinformatics"
institution = "University of Pretoria"
linkedin = "https://www.linkedin.com/in/rachel-van-duyn-6b1248174/"

# Display basic profile information
st.header("Overview")
col1, col2 = st.columns([1,1]) 
with col1:
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
with col2:
    st.image(
        "Image.jpeg", width=400)

st.header("About Me")
st.write("I am a Master’s student in Bioinformatics, focusing on refining and optimising AI-driven approaches for cancer diagnostics in South Africa. My work sits at the intersection of genomics, machine learning, and health equity, with a particular emphasis on improving diagnostic accuracy and representation for under-served populations. Previously my work focused on identifying germline novel variants in Black South African women with breast cancer, aiming to improve our understanding of genetic risk in underrepresented populations.")
st.text(" ")
st.write("Alongside my studies, I work as an online tutor teaching Mathematics, Science, and English, with a strong emphasis on scientific communication. This role has strengthened my ability to translate complex technical concepts across disciplines, communicate clearly with diverse audiences, and support learners in building confidence and understanding.")

# Add a section for research interests
st.header("Research Interests")
st.markdown("""
- **🧬 Genomics and Bioinformatics**
- **🌍 Health Equity in Genomics**
- **📊 Data Analysis and Visualization**
- **🗣️ Scientific Communication**
""")

# Add a section for skills

st.markdown("### ⚡ Core Capabilities")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### 💻 Programming")
    st.progress(70)
    st.caption("R • Python • Bash • SQL")
with col2:
    st.markdown("#### 🧬 Bioinformatics")
    st.progress(70)
    st.caption("Variant calling • WGS • Annotation • Data visualisation")
with col3:
    st.markdown("#### 🗣️ Communication")
    st.progress(90)
    st.caption("Scientific writing • Cross-disciplinary teaching • SciComm")

# Add a section for eduction

st.markdown("### 🎓 Academic Qualifications")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### Msc in Bioinformatics")
    st.progress(5)
    st.caption("University of Pretoria • 2026 - Present")
with col2:
    st.markdown("#### Honours in Bioinformatics")
    st.progress(100)
    st.caption("University of Pretoria • 2025 - 2025, with distinction")
with col3:
    st.markdown("#### BSc in Human Physiology and Genetics")
    st.progress(100)
    st.caption("University of Pretoria • 2022 - 2024")


# Add a contact section
st.header("Contact Information")
st.markdown(f"""
**LinkedIn:** {linkedin}  
**GitHub:** https://github.com/RachelvanDuyn  
**Email:** rachelvanduyn@icloud.com
""")

st.markdown("---")
st.center = True
st.markdown("<div style='text-align: center'> © 2026 Rachel van Duyn | Built with Streamlit & Python </div>", unsafe_allow_html=True)