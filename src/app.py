import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from src.github_profile import generate_github_profile

st.title(":heavy_check_mark: Github Profile Readme Generator")

# personal info
kwargs = {}
st.header(":white_circle: Personal info")
with st.expander("Personal info"):
    col1,col2,col3,col4,col5 = st.columns(5)
    kwargs["name"] = col1.text_input("Name")
    kwargs["email"] = col2.text_input("Email")
    kwargs["homepage"] = col3.text_input("Homepage")    
    kwargs["phone"] = col4.text_input("Phone")  
    kwargs["location"] = col5.text_input("Location")

# social media
st.header(":red_circle: Social Media")
with st.expander("Social Media"):
    st.markdown("Enter your social media usernames(not links): ")
    col1,col2 = st.columns(2)
    kwargs["twitter"] = col1.text_input("Twitter")
    kwargs["linkedin"] = col2.text_input("Linkedin")
    kwargs["facebook"] = col1.text_input("Facebook")
    kwargs["instagram"] = col2.text_input("Instagram")
    kwargs["youtube"] = col1.text_input("Youtube")

# extensions
st.header(":large_green_circle: Extensions")
with st.expander("Extensions"):
    if st.checkbox("github stats"):
        kwargs["github_stats"] = st.text_input("Github Username")   

# select theme
st.header(":large_blue_circle: Select Theme")
themes = Path("src/themes").iterdir()
themes = [theme.stem for theme in themes]
theme = st.selectbox("Select Theme", themes)
st.markdown(f"Selected Theme: **{theme}**")

# Generate Readme
st.header(":large_yellow_circle: Readme")
st.text("copy the code below and paste it in your github profile readme.md section")
Readme = generate_github_profile(theme, **kwargs)
st.code(Readme)
