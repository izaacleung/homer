import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="NF H.O.M.E.R 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**Mail** : Izaac.leung@nanfung.com")
    st.write("**Created by Izaac**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>NF H.O.M.E.R 🤖</h1>
    """,
    unsafe_allow_html=True,)
st.image('https://onemilliondollar.ust.hk/2018/1m_website/Icons/Nan_Fung_Logo.png', caption='NF', use_column_width=True)
st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>NF H.O.M.E.R, using ChatGPT and our own proprietary data to answer your questions based on our database 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 NF's Pages")
st.write("""
- **NF-advisor**: General Chat on data (PDF, TXT,CSV) with domain knowledge
- **NF-i-secretary**: Chat on tabular data (CSV) | for precise information such as outlook calendar
""")
st.markdown("---")







