import streamlit as st

# Set the page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":wave:", layout="wide")

# Title and Intro Section
st.title("Welcome to My Portfolio!")
st.subheader("Hi, I'm Ayush Kumar F!")
st.write("I'm a Python Developer passionate about automation, data science, and software engineering.")

# About Section
st.header("About Me")
st.write("""
- **Role**: VNF Automation Engineer
- **Experience**: Automating VNF upgrades, creating CI/CD pipelines, and reducing manual effort.
- **Hobbies**: Coding, learning new tech, and fitness.
""")

# Projects Section
st.header("Projects")
st.write("""
1. **VNF Automation Tool**: Reduced upgrade time by 80%.
2. **Fleet Management Software**: Streamlined vehicle tracking for a logistics company.
3. **IP Address Increment Calculator**: Simplified subnet calculations for network engineers.
""")

# Contact Section
st.header("Contact")
st.write("Feel free to reach out:")
st.write("[Email Me](mailto:your_email@example.com)")
st.write("[GitHub](https://github.com/your_username)")
st.write("[LinkedIn](https://linkedin.com/in/your_username)")

# Footer
st.write("---")
st.write("Powered by Streamlit")
