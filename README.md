# 🧬 OptiCore // SIMULACRUM 
> **Autonomous Multi-Agent Prompt Optimization Sandbox Terminal**

OptiCore is an advanced agent optimization sandbox designed to automate prompt engineering workflows through recursive evolutionary evaluation loops. It eliminates human manual prompt testing by setting up an environment where a Critic Agent actively evaluates, diagnoses, and programmatically mutates the system instructions of a Player Agent over sequential generations based on system log telemetry data.

---

## 🚀 Core Architecture Flow

```text
               ┌──────────────────────────────┐
               ▼                              │
    ┌────────────────────┐          ┌─────────┴──────────┐
    │ Gemini 1.5 Flash   ├─────────►│ ServerEnvironment  │
    │  (Player Agent)    │          │  (Simulation Task) │
    └────────────────────┘          └─────────┬──────────┘
                                              │
                                              ▼
    ┌────────────────────┐          ┌────────────────────┐
    │   Mutated Prompt   │◄─────────┤   Llama-3-70B      │
    │    Optimization    │          │  (Mutant Critic)   │
    └────────────────────┘          └─────────┬──────────┘
                                              │
  ▲                                           │
  └───────────────────────────────────────────┘
```

- **Player Agent (Google Gemini-1.5-Flash):** Interacts natively with the simulation sandbox using natural language commands powered by the official `google-genai` SDK.
- **Task Environment (`ServerEnvironment`):** A custom Python milestone simulator tracking precise troubleshooting milestones (inspecting log data, terminating stuck system processes, issuing a cold reboot).
- **Mutant Critic (Meta-Llama-3-70B-Instruct):** Orchestrated via the open-source `huggingface_hub` Inference API client to analyze raw history traces and rewrite mutated system instructions.

---

## 🛠️ Local Installation & Startup

1. Clone this repository into your local machine directory:
```bash
git clone https://github.com
cd OptiCore-Simulacrum
```

2. Run the package installer to deploy external libraries:
```bash
pip install -r requirements.txt
```

3. Launch the premium dark cyber-minimalism UI client dashboard:
```bash
streamlit run app.py
```

4. Input your **Google AI Studio Key** and **Hugging Face Token** into the sidebar inputs, adjust your dynamic iteration depth slider (3 to 10 generations), and hit **🚀 EXECUTE AUTONOMOUS EVOLUTION LIFECYCLE**.

---

## 📊 File Manifest & System Structure
- `app.py`: Streamlit user interface client featuring custom dark-mode CSS overrides, session state caching, and live performance line charts.
- `engine.py`: The multi-model coordinator controlling the dynamic generation loop and handling API client exception fallback streams.
- `environment.py`: The stateful simulation environment parsing textual keyword actions and calculating execution metric scores.
- `requirements.txt`: Package dependency matrix locking stable versions for `streamlit`, `pandas`, `google-genai`, and `huggingface_hub`.
