
import streamlit as st
import joblib

# Load trained pipeline
pipe = joblib.load("model_text.pkl")

# Page configuration
st.set_page_config(
    page_title="Spam Message Detector",
    page_icon="📩",
    layout="centered"
)

# Header
st.title("📩 Spam Message Detector")
st.subheader("AI-Based SMS Classification")

st.write(
    "Enter a message below to check whether it is "
    "Spam or Not Spam."
)

st.divider()

# User input
message = st.text_area(
    "💬 Enter Your Message",
    height=180,
    placeholder="Example: Congratulations! You have won a free prize..."
)

# Prediction button
if st.button("🔍 Predict Message", use_container_width=True):

    if message.strip() == "":
        st.warning("⚠️ Please enter a message.")

    else:
        # Prediction
        prediction = pipe.predict([message])[0]

        # Probability
        probabilities = pipe.predict_proba([message])[0]
        confidence = max(probabilities) * 100

        st.divider()

        st.write("### 📊 Prediction Result")

        st.write("**Prediction:**", prediction)
        st.write("**Confidence:**", f"{confidence:.2f}%")

        # Display result
        if prediction == "spam":
            st.error("🚨 This message is SPAM")

        else:
            st.success("✅ This message is NOT SPAM")

        # Confidence progress bar
        st.progress(int(confidence))

# Footer
st.divider()

st.caption("Developed by Rajala Yerriswamy Reddy | Machine Learning")

