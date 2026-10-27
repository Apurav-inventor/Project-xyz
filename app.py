
import streamlit as st
from PIL import Image
from google import genai

st.set_page_config(
    page_title="ChartLens AI",
    page_icon="📈",
    layout="centered"
)

st.title("📈 ChartLens AI")
st.write("Understand stock charts in simple language.")

st.info(
    "Educational tool only. No buy or sell recommendations."
)

uploaded_file = st.file_uploader(
    "Upload a stock chart screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Your uploaded chart",
             use_container_width=True)

    if st.button("Explain my chart"):
        try:
            client = genai.Client(
                api_key=st.secrets[AQ.Ab8RN6Kva-onSMVjuU-kx3cB7Tn9HiUQBH_lyruPunaoRHTqUg]
            )

            prompt = """
            Explain this stock chart to a beginner.
            Describe:
            1. Visible price trend
            2. Moving averages, if shown
            3. RSI, if shown
            4. Trading volume
            5. Possible support and resistance zones
            6. What these concepts mean

            Never recommend buying, selling, or holding.
            Do not invent values that are not visible.
            State when indicators are missing or unclear.
            Explain that this is educational, not financial advice.
            """

            with st.spinner("Analyzing chart..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[prompt, image]
                )

            if response.text:
                st.subheader("Chart Explanation")
                st.markdown(response.text)
            else:
                st.warning("No explanation returned.")

        except Exception:
            st.error(
                "Analysis failed. Check your API key, "
                "model availability, and usage limits."
            )
