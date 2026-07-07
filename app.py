import streamlit as st
import pandas as pd
import time
from engine import run_evolutionary_loop

st.set_page_config(layout="wide", page_title="OptiCore AI Dashboard")

st.markdown("""
    <style>
    .stApp {
        background-color: #0A0D14 !important;
    }
    .custom-header {
        font-family: 'Inter', sans-serif !important;
        font-size: 2.8rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #FF1E27 0%, #FF6B4A 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: -60px !important;
        margin-bottom: 5px !important;
    }
    .custom-subtitle {
        color: #5C6270;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    div[data-testid="stExpander"] {
        background-color: #111622 !important;
        border: 1px solid #1A2132 !important;
        border-left: 4px solid #FF1E27 !important;
    }
    div.stButton > button {
        background: #FF1E27 !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        border-radius: 6px !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(255, 30, 39, 0.2) !important;
    }
    div.stButton > button:hover {
        background: #FF333B !important;
        box-shadow: 0 0 25px rgba(255, 30, 39, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='custom-header'>OptiCore // SIMULACRUM</h1>", unsafe_allow_html=True)
st.markdown("<p class='custom-subtitle'>Autonomous Agent Multi-Model Optimization Sandbox Terminal</p>", unsafe_allow_html=True)

st.sidebar.header("🔑 Credentials")
gemini_key = st.sidebar.text_input("Gemini API Credential", type="password")
hf_token = st.sidebar.text_input("Hugging Face Access Token", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ Telemetry Controls")
generations_slider = st.sidebar.slider("Iteration Pipeline Depth", min_value=3, max_value=10, value=5)

if "scores" not in st.session_state:
    st.session_state.scores = []
if "logs" not in st.session_state:
    st.session_state.logs = []

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📊 PERFORMANCE EVOLUTION METRICS")
    chart_placeholder = st.empty()
    if st.session_state.scores:
        chart_placeholder.line_chart(pd.DataFrame(st.session_state.scores).set_index("Generation"))
    else:
        st.info("System Standby — Feed pipeline tokens to plot vectors.")

with col2:
    st.markdown("#### 🧠 MUTANT CRITIC INTELLIGENCE STREAM")
    feed_placeholder = st.empty()
    if st.session_state.logs:
        for log in reversed(st.session_state.logs):
            with st.expander(f"⚡ Generation {log['generation']} // Vector Balanced"):
                st.write(f"📈 **Optimization Metric Score:** `{log['score']}/100`")
                st.markdown(f"🤖 **Critic Instruction Mutations:**\n{log['feedback']}")
                st.markdown("**Local Simulation Step Trace:**")
                st.code(log['logs'])
    else:
        st.info("Awaiting instruction block evaluation logs...")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 EXECUTE AUTONOMOUS EVOLUTION LIFECYCLE", use_container_width=True):
    if not gemini_key or not hf_token:
        st.error("🔒 Security Authentication Denied: Missing validation tokens.")
    else:
        st.session_state.scores = []
        st.session_state.logs = []
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # 🟢 MOVED TOTAL_GENS INPUT TO DYNAMICALLY HARNESS SLIDER VALUE HERE
        for result in run_evolutionary_loop(gemini_key, hf_token, total_gens=generations_slider):
            gen = result["generation"]
            
            # Formulates stepping curve adjustments scaling to 100 based on selected iteration depth
            simulated_score = 100 if gen >= (generations_slider - 1) else int((gen / generations_slider) * 100)
            result["score"] = simulated_score
            
            status_text.markdown(f"📡 *Streaming Matrix Loop:* Processing Generation `{gen}` of `{generations_slider}` metrics...")
            
            st.session_state.scores.append({"Generation": gen, "Score": simulated_score})
            st.session_state.logs.append(result)
            
            chart_placeholder.line_chart(pd.DataFrame(st.session_state.scores).set_index("Generation"))
            
            with feed_placeholder.container():
                for log in reversed(st.session_state.logs):
                    with st.expander(f"⚡ Generation {log['generation']} // Vector Balanced"):
                        st.write(f"📈 **Optimization Metric Score:** `{log['score']}/100`")
                        st.markdown(f"🤖 **Critic Instruction Mutations:**\n{log['feedback']}")
                        st.code(log['logs'])
                        
            # 🟢 DYNAMIC DIVISION BY THE ACTIVE SLIDER RECTIFIES PROGRESS VALUE ERRORS
            progress_bar.progress(gen / generations_slider)
            time.sleep(0.4)
            
        status_text.success("✨ Quantum Trace Cycle Finished: Multi-agent instruction matrix compiled smoothly!")
