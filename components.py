import streamlit as st


def hero():

    st.markdown(
        """
        <div class="hero">

        <h1>🏭 Industrial Failure Memory Assistant</h1>

        <h4>
        AI-powered troubleshooting using <b>Cognee Persistent Memory</b> +
        <b>Llama 3</b>
        </h4>

        <p>
        Search historical industrial failures, retrieve maintenance
        knowledge, and generate professional troubleshooting reports.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


def status_cards():

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="metric-card">

            <h2>🧠</h2>

            <h3>Cognee Memory</h3>

            <h4 style="color:#22c55e;">Connected</h4>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:

        st.markdown(
            """
            <div class="metric-card">

            <h2>🤖</h2>

            <h3>Llama 3</h3>

            <h4 style="color:#22c55e;">Ready</h4>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:

        st.markdown(
            """
            <div class="metric-card">

            <h2>📚</h2>

            <h3>Knowledge Base</h3>

            <h4 style="color:#22c55e;">Indexed</h4>

            </div>
            """,
            unsafe_allow_html=True,
        )


def sidebar():

    with st.sidebar:

        st.title("🏭 Industrial AI")

        st.divider()

        st.subheader("System")

        st.success("Cognee Connected")

        st.success("OpenRouter Connected")

        st.success("Llama Ready")

        st.divider()

        st.subheader("Knowledge")

        st.write("📚 Maintenance Manual")

        st.write("🧠 Company Memory")

        st.divider()

        st.subheader("Capabilities")

        st.write("✔ Root Cause Analysis")

        st.write("✔ Troubleshooting")

        st.write("✔ Safety Guidance")

        st.write("✔ Maintenance Actions")

        st.divider()

        st.caption("Hackathon 2026")

def memory_card(context):
    st.subheader("📚 Similar Historical Incidents")
    with st.container(border=True):
        st.markdown(context)

def ai_report(answer):
    st.subheader("🤖 AI Root Cause Analysis")
    with st.container(border=True):
        st.markdown(answer)                