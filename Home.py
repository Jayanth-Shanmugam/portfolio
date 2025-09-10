import streamlit as st

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
    st.page_link("Home.py", label = "jayanth.mks@gmail.com", icon=":material/mail:", disabled=True)

with st.container():

    col1, col2, col3 = st.columns([3, 0.5, 2])

    # Introduction paragraph
    with col1:
        st.header("Jayanth Shanmugam")
        st.subheader(":material/waving_hand: Hello!") 
        intro = """
        I'm currently pursuing my **MS in Computer Science and Engineering**, specializing in AI/ML at the :blue[University at Buffalo - SUNY] 
        (Go Bulls!). My interests lie in **data engineering** and **machine learning**. Previously, I worked as a **Data Engineer** 
        at Adani Wilmar Ltd., where I was responsible for setting up efficient ways to move data to our data lake on **Google Cloud** and automate 
        existing **machine learning** workloads. I also interned at the same company during which I led **generative AI** projects, one of which 
        ranked **top 10** among 30,000 teams at the **Google GenAI Hackathon** APAC edition.
        """
        st.write(intro)

    # A picture of me
    with col3:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.image("images/welcome-page-image.jpg")

st.divider()

# Skills section
st.subheader("My Skills")
st.html("html/skills.html")

st.divider()

# Timeline section
st.subheader("Timeline")
st.html("html/timeline.html")
