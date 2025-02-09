import streamlit as st

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

st.header("My Projects")

st.divider()

with st.expander(":material/description: **Research Paper Recommendation System**"):
    st.write(
    """
    Our project tackles a common challenge that many students face - the overwhelming task of finding relevant research papers that match their interests. 
    We've observed that students often struggle with manually searching through extensive academic databases, which not only consumes valuable time but can 
    also discourage them from pursuing academic collaborations. We understand how frustrating it can be when potential innovations in your field might be 
    overlooked simply because of the vast amount of information to sort through.\n
    To address this, we're developing an automated platform that will make this process much more efficient. Our solution allows students to simply input 
    their research topics or keywords, and the platform will generate a curated list of relevant research papers. Beyond just simplifying the search process, 
    our platform aims to have a broader impact on academia by making research opportunities more accessible, especially for students who don't have established 
    academic networks. We're particularly excited about how our platform can foster interdisciplinary collaboration by helping students connect with professors 
    working in related or complementary fields.
    """
    )

with st.expander(":material/cognition_2: **Genius Kitchen**"):
    st.write(
    """
    For this project, we secured a top 10 placement among 30,000 competitors in the Google GenAI Hackathon APAC Edition. This achievement reflected 
    our commitment to pushing the boundaries of artificial intelligence applications and our ability to deliver outstanding solutions under competitive conditions.
    we developed an advanced AI-powered recipe platform that transforms the cooking experience for users worldwide. By combining
    Gemini LLM with Streamlit, the platform provides tailored recipe recommendations that precisely match individual dietary restrictions and taste 
    preferences. We further enhanced user engagement by developing a sophisticated multimodal system that integrates Imagen and Text-to-Speech 
    APIs. This solution creates an immersive learning experience by automatically generating visual aids and audio instructions, making 
    complex recipes more accessible and easier to follow for users of all skill levels. Here is a link to a LinkedIn post from the organizers: \n
    [LinkedIn Post](https://www.linkedin.com/posts/hack2skill_glimpses-of-top-10-finalists-activity-7193182294214385664-zdEA?utm_source=share&utm_medium=member_desktop)
    """
    )

with st.expander(":material/newspaper: **Newsly.ai**"):
    st.write(
        """
        Newsly.ai was an internal tool that our team at Adani Wilmar developed to improve the productivity of employees in the sales department.
        Everyday, people working in sales had to manually visit news websites, search for news on topics related to packaged goods like price of sunflower oil
        rapeseed oil, etc. and make purchasing decisions. All this manual sifting of news articles was a time consuming process. Therefore, to improve the productivity
        of the employees, our team developed a web interface that automatically scours the internet for relevant news articles and displays a summarized version of the article to the user. \n
        Our team developed a comprehensive web scraping solution powered by Python and Playwright that automatically collects real-time content from more than five websites across six distinct categories. 
        The system's capabilities were significantly enhanced through the integration of Google Gemini API with custom scraping tools, enabling automated news summarization and keyword extraction that drove 
        a 35% increase in team productivity. To ensure widespread accessibility and optimal performance, the team designed and implemented a responsive web interface using Flask and Bootstrap, which was successfully 
        containerized and deployed on Google Cloud Run, providing a scalable foundation for future growth. \n
        Here is a demo of the beta version of the application: 
    """
    )

    st.video("demos/NewslyAI-Demo.mp4")