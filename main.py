import streamlit as st
st.subheader("WELCOME TO OUR PAGE")
st.write("EXPLORE US")
st.selectbox("Which is favoutite language",['Tamil','English','French','German'])
st.checkbox("Tamil")
st.checkbox("English")
st.slider("Pick some range",0,100)
st.select_slider("Select Entry",["Best","Average","Worst"])
st.progress(50)
st.button("Click me")


st.sidebar.title("About")
st.sidebar.selectbox("Which language yoy like",['Hindi','Telugu','Malayalam','Kanada'])
st.sidebar.markdown("Need information")
st.sidebar.button("Click")