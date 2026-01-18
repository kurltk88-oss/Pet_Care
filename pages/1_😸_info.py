import streamlit as st
if 'breed' in st.session_state:
    st.write(st.session_state['breed'])