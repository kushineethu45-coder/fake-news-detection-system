import streamlit as st

st.set_page_config(page_title="Fake News Detection System")

st.title("📰 Fake News Detection System")
st.write("Check whether news is REAL or FAKE.")

news = st.text_area("Enter your news:")

fake_words = [
    "miracle cure",
    "secret plan",
    "100% guaranteed",
    "fake news",
    "false information",
    "free money",
    "win lottery",
    "shocking"
]
if st.button("Check News"):

    if not news.strip():
        st.warning("Please enter news.")

    else:
        text = news.lower()

        matched_words = [
            word for word in fake_words if word in text
        ]

        percentage = min(len(matched_words) * 20, 100)
        real_percentage = 100 - percentage

        if matched_words:
            st.error("🔴 PREDICTION: FAKE NEWS")
            st.write("Matched keywords:", ", ".join(matched_words))
        else:
            st.success("🟢 PREDICTION: REAL NEWS")

        st.write("🔴 Fake News Percentage:", percentage, "%")
        st.progress(percentage / 100)

        st.write("🟢 Real News Percentage:", real_percentage, "%")
        st.progress(real_percentage / 100)