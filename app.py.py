import streamlit as st
import pandas as pd
from urllib.parse import quote

st.set_page_config(page_title="WhatsApp Bulk Sender", layout="wide")

st.title("📩 WhatsApp Bulk Message Sender (Safe Version)")
st.write("Upload a CSV file with `name` and `phone` columns.")

uploaded = st.file_uploader("Upload Contacts CSV", type=["csv"])

templates = {
    "Home Loan Eligibility": "Hi {name}, I can help check your home loan eligibility for free. Interested?",
    "Interest Rates": "Hello {name}, want the latest home loan interest rate options?",
    "General Follow-up": "Hi {name}, just checking if you need any help with your home loan?"
}

template_choice = st.selectbox("Choose Message Template", list(templates.keys()))

custom_template = st.text_area("Or Write Custom Message (optional)", "")

st.markdown("---")

if uploaded:
    df = pd.read_csv(uploaded)
    if "phone" not in df.columns:
        st.error("CSV must contain a 'phone' column.")
    else:
        df["name"] = df.get("name", df["phone"]).astype(str)
        df["phone"] = df["phone"].astype(str)

        st.success(f"Loaded {len(df)} contacts.")

        final_template = custom_template if custom_template else templates[template_choice]

        st.write("### Message Preview")
        st.info(final_template.replace("{name}", "Rahul"))

        st.write("### WhatsApp Send Links")
        for index, row in df.iterrows():
            msg = final_template.replace("{name}", row["name"])
            encoded = quote(msg)
            phone = row["phone"]
            url = f"https://wa.me/{phone}?text={encoded}"
            st.write(f"➡️ [{row['name']} ({phone})]({url})")

        st.success("Links generated! Click each to send messages.")
else:
    st.warning("Upload a CSV to begin.")