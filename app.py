import streamlit as st
import time
import random
import pandas as pd

st.set_page_config(page_title="LLM Cost & Performance Analyzer", layout="wide")

st.title("🤖 LLM Cost & Performance Analyzer")
st.write("Compare GPT-4, Claude, and Gemini on speed, cost, and output length.")

models = ["GPT-4", "Claude", "Gemini"]
question = st.text_area("Enter your question:", "What is Snowflake AI Data Cloud?")

if st.button("Run Analysis"):
    results = []
    for model in models:
        start = time.time()

        # Simulated response (replace with real API call)
        response = f"{model} response to: {question}"

        duration = time.time() - start + random.uniform(0.5, 2.0)
        cost = len(response.split()) * random.uniform(0.001, 0.003)
        length = len(response.split())

        results.append({
            "Model": model,
            "Duration (s)": round(duration, 2),
            "Cost ($)": round(cost, 4),
            "Length": length,
            "Response": response
        })

    df = pd.DataFrame(results)
    st.subheader("📊 Results Table")
    st.dataframe(df)

    st.subheader("📈 Metrics Comparison")
    st.bar_chart(df.set_index("Model")[["Duration (s)", "Cost ($)", "Length"]])

    st.subheader("📝 Sample Responses")
    for r in results:
        st.markdown(f"**{r['Model']}**: {r['Response']}")
