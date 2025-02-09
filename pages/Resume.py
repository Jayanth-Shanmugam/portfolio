import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

# Logo to go beside sidebar navigation button
st.logo(image="images/sidebar-logo.png", icon_image="images/menu_icon.png", size="large")

with st.sidebar:
    # Website navigation
    st.page_link("Home.py", label = "Home", icon=":material/home:")
    st.page_link("pages/Resume.py", label = "Resume", icon=":material/article:")
    st.page_link("pages/Projects.py", label = "Projects", icon=":material/tactic:")
    st.page_link("pages/Blog.py", label = "Blog", icon=":material/auto_stories:")
    st.divider()

    # Contact details
    st.subheader("Get in touch")
    st.page_link("https://www.linkedin.com/in/jayanth-shanmugam", 
                 label = "![Linkedin_Icon](https://img.icons8.com/color/48/linkedin.png) LinkedIn")
    st.page_link("https://github.com/Jayanth-Shanmugam", 
                 label = "![github_Icon](https://img.icons8.com/fluency/96/github.png) Github")
    st.page_link("Home.py", label = "jmallasa@buffalo.edu", icon=":material/mail:", disabled=True)

pdf_viewer("misc/Jayanth-Resume.pdf")