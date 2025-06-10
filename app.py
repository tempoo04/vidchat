import streamlit as st
import videohelper
import raghelper

if "selected_video_url" not in st.session_state:
    st.session_state.current_video_url = None
    st.session_state.current_transcript_docs = []

st.set_page_config(page_title="VidChat: Chat with Youtube!", layout="centered")
st.image(image="./img/banner_app.jpeg")
st.title("VidChat: Chat with Youtube!")
st.divider()

tab_url, tab_search = st.tabs(["URL Import", "Search by Term"])

with tab_url:
    video_url = st.text_input(label= "Enter Youtube URL", key = "video_url")
    prompt = st.text_input(label= "Enter Yor Prompt", key = "url_prompt")
    submit_btn = st.button("Enter", key="url_submit")

    if submit_btn:
        st.video(data = video_url)
        st.divider()
        if st.session_state.current_video_url != video_url:
            with st.spinner("STEP1 1: Video transcript is being prepared..."):
                video_transcript_docs = videohelper.get_video_transcript(url=video_url)
                st.session_state.current_transcript_docs = video_transcript_docs
        st.success("Video Transcript was saved into the database")
        st.divider()
        st.session_state.current_video_url = video_url


        with st.spinner("STEP 2: Your question is being answered..."):
            AI_Response, relevant_documents = raghelper.rag_with_video_transcript(st.session_state.current_transcript_docs,prompt)
        st.info("ANSWER:")
        st.markdown(AI_Response)
        st.divider()

        for doc in relevant_documents:
            st.warning("REFERENCE:")
            st.caption(doc.page_content)
            st.markdown(f"SOURCE : {doc.metadata}")
            st.divider()


