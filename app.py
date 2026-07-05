import streamlit as st
from datetime import datetime

from styles import load_css
from components import (
    hero,
    sidebar,
    status_cards,
    memory_card,
    ai_report,
)

from cognee_client import search_memory, remember_incident
from llm import analyze_failure

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Cognee Factory Brain",
    page_icon="🏭",
    layout="wide"
)

load_css()

sidebar()

st.markdown(
    """
# 🧠 Cognee Factory Brain

### The Brain of Factory Maintenance

Persistent industrial memory that transforms maintenance manuals and historical failure logs into instant troubleshooting intelligence."""
)

status_cards()


st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Input Section
# -----------------------------

st.subheader("🛠 Report an Equipment Failure")

question = st.text_area(
    "",
    height=180,
    placeholder="""
Example:

The reciprocating air compressor has low oil pressure after running
for 20 minutes. Oil warning light appears and compressor becomes noisy.
"""
)

left, right = st.columns([5,1])

with right:

    analyze = st.button(
        "🧠 Analyze with Cognee Brain",
        use_container_width=True
    )

# -----------------------------
# Analysis
# -----------------------------

if analyze:

    if question.strip() == "":
        st.warning("Please describe the machine problem.")
        st.stop()

    progress = st.progress(0)

    status = st.empty()

    status.info("🔍 Searching Cognee Industrial Memory...")

    progress.progress(20)

    context = search_memory(question)

    progress.progress(45)

    status.info("📚 Retrieving historical maintenance knowledge...")

    progress.progress(65)

    status.info("🤖 Generating AI troubleshooting report...")

    answer = analyze_failure(question, context)

    progress.progress(100)

    status.success("✅ Analysis Completed")

    st.markdown("---")

    c1, c2 = st.columns([1,1])

    with c1:

        memory_card(context)

    with c2:

        ai_report(answer)

    st.markdown("---")

    b1, b2, b3 = st.columns(3)

    with b1:

        if st.button("🧠 Remember Incident"):

            if st.button("🧠 Remember Incident"):

                with st.spinner("Updating Cognee memory..."):

                    ok = remember_incident(
                        question,
                        context,
                        answer
                    )

                if ok:
                    st.success("✅ Incident remembered successfully!")
                    st.info("🧠 Cognee knowledge graph updated.")

    with b2:

        st.download_button(

            label="📄 Download Report",

            data=answer,

            file_name=f"industrial_report_{datetime.now().strftime('%Y%m%d_%H%M')}.md",

            mime="text/markdown"
        )

    with b3:

        if st.button("🔄 New Analysis"):

            st.rerun()

# -----------------------------
# Demo Questions
# -----------------------------

st.markdown("---")

with st.expander("💡 Demo Questions"):

    st.code("""
What causes low oil pressure in reciprocating air compressors?

My centrifugal pump is noisy and vibrating. What are the possible causes?

How can I troubleshoot a motor controller with welded contacts?

Bearing has dirt embedment and scoring. What should I inspect first?

The hydraulic system loses pressure after 15 minutes.

The induction motor trips immediately after startup.

The gearbox is overheating and making loud whining noises.
""")

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.caption(
"""
🧠 Cognee Factory Brain

Powered by 🧠 Cognee Cloud 🤖 Llama 3 ⚡ OpenRouter 🎨 Streamlit
"""
)