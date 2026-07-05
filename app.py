# Updated app.py
import streamlit as st
from datetime import datetime

from styles import load_css
from components import sidebar, status_cards, memory_card, ai_report
from cognee_client import search_memory, remember_incident
from llm import analyze_failure

st.set_page_config(
    page_title="Cognee Factory Brain",
    page_icon="🏭",
    layout="wide"
)

load_css()
sidebar()

st.markdown("""
# 🧠 Cognee Factory Brain

### The Brain of Factory Maintenance

Persistent industrial memory that transforms maintenance manuals and historical failure logs into instant troubleshooting intelligence.
""")

status_cards()
st.markdown("<br>", unsafe_allow_html=True)

# Session defaults
for key in ("question", "context", "answer"):
    if key not in st.session_state:
        st.session_state[key] = ""

st.subheader("🛠 Report an Equipment Failure")

question = st.text_area(
    "Describe Machine Problem",
    value=st.session_state.question,
    label_visibility="collapsed",
    height=180,
    placeholder="Describe the machine issue..."
)

_, right = st.columns([5, 1])

with right:
    analyze = st.button("🧠 Analyze with Cognee Brain", use_container_width=True)

if analyze:
    if not question.strip():
        st.warning("Please describe the machine problem.")
        st.stop()

    progress = st.progress(0)
    status = st.empty()

    status.info("🔍 Searching Cognee Industrial Memory...")
    progress.progress(25)

    context = search_memory(question)

    status.info("🤖 Generating AI troubleshooting report...")
    progress.progress(70)

    answer = analyze_failure(question, context)

    progress.progress(100)
    status.success("✅ Analysis Completed")

    st.session_state.question = question
    st.session_state.context = context
    st.session_state.answer = answer

if st.session_state.answer:

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:
        memory_card(st.session_state.context)

    with c2:
        ai_report(st.session_state.answer)

    st.markdown("---")

    b1, b2, b3 = st.columns(3)

    with b1:
        if st.button("🧠 Remember Incident"):
            try:
                with st.spinner("Uploading incident to Cognee..."):
                    status_code, response_text = remember_incident(
                        st.session_state.question,
                        st.session_state.context,
                        st.session_state.answer
                    )

                if status_code == 200:
                    st.success("✅ Incident remembered successfully!")
                    st.code(response_text)
                else:
                    st.error(f"Upload failed ({status_code})")
                    st.code(response_text)

            except Exception as e:
                st.exception(e)

    with b2:
        st.download_button(
            "📄 Download Report",
            st.session_state.answer,
            file_name=f"industrial_report_{datetime.now().strftime('%Y%m%d_%H%M')}.md",
            mime="text/markdown"
        )

    with b3:
        if st.button("🔄 New Analysis"):
            st.session_state.question = ""
            st.session_state.context = ""
            st.session_state.answer = ""
            st.rerun()

st.markdown("---")

with st.expander("💡 Demo Questions"):
    st.code("""What causes low oil pressure in reciprocating air compressors?

The gearbox is overheating and making loud whining noises.

The induction motor trips immediately after startup.

The hydraulic system loses pressure after 15 minutes.
""")

st.markdown("---")
st.caption("🧠 Cognee Factory Brain • Powered by Cognee Cloud • Llama 3 • OpenRouter • Streamlit")
