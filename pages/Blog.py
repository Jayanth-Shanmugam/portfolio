import streamlit as st

# Have the sidebar collapsed when site is visited first
st.set_page_config(initial_sidebar_state="collapsed")

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

st.subheader("My First Blog")
st.write("*February 8, 2025*")
st.write(
    """
    Hey guys! Welcome to my world. This will be a space where I share my weekly progress and what I learned in the week from my courses. For this week, 
    here are a few of my personal milestones and all things I learned which I found interesting:
    1. I have been consistently getting stronger at the gym ever since I started going with a friend of mine. I have hit a new PR of 50 pounds on the incline dumbbell press,
    45 pounds on the shoulder press, 200 pounds on the squat, and 190 pounds on the leg curl machine. 
    2. The GPU elective I chose this semester has turned out to be extremely engaging. The professor encourages us to think out of the box which has been a really good mental exercise 
    and a test of my computer science fundamentals. I feel like I can really grow as a computer scientist if I diligently attend and take part in the classroom discussions.
    3. I started reading "1984" by George Orwell a while back, and the events that happen in the book are eerily similar to the current scenario around the world. It is really surprising that a book written 
    decades ago is still relevant in this day and age.
"""
)