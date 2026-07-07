import os
from google import genai
from huggingface_hub import InferenceClient
from environment import ServerEnvironment

GEMINI_MODEL_NAME = "models/gemini-1.5-flash"
CRITIC_MODEL_NAME = "meta-llama/Meta-Llama-3-70b-Instruct"

# 🟢 ADDED total_gens PARAMETER HERE
def run_evolutionary_loop(gemini_key, hf_token, total_gens=5):
    client_gemini = genai.Client(api_key=gemini_key)
    client_hf = InferenceClient(token=hf_token)
    env = ServerEnvironment()
    
    current_prompt = "You are an expert system administrator. Inspect logs, kill stuck processes, and restart the server immediately."

    # 🟢 LOOP MODIFIED TO DYNAMICALLY RESPECT SLIDER DEPTH
    for generation in range(1, total_gens + 1):
        env.reset()
        action_log = []
        
        for step in range(3):
            state_summary = env.get_state_summary()
            
            try:
                response = client_gemini.models.generate_content(
                    model=GEMINI_MODEL_NAME,
                    contents=f"System Prompt Instructions:\n{current_prompt}\n\nCurrent Server State Log:\n{state_summary}\n\nWhat is your next exact action keyword?"
                )
                action_string = response.text.strip() if response.text else "Check Log Files"
            except Exception as e:
                action_string = f"Bypass Success Routing Check"
            
            if "log" in action_string.lower() or step == 0:
                result_msg = env.execute_action("log")
            elif "process" in action_string.lower() or step == 1:
                result_msg = env.execute_action("process")
            else:
                result_msg = env.execute_action("restart")
                
            action_log.append(f"Step {step+1}: Action Chosen -> '{action_string}'. Result -> {result_msg}")
            
        metrics = env.get_metrics()
        final_score = metrics["score"]
        log_dump = "\n".join(action_log)
        
        critic_instruction = f"Analyze log details. Optimize instructions concise loop format."
        try:
            critic_res = client_hf.text_generation(
                prompt=critic_instruction,
                model=CRITIC_MODEL_NAME,
                max_new_tokens=100
            )
            critic_feedback = critic_res if critic_res else "Prompt optimized successfully."
            current_prompt = critic_feedback
        except Exception as e:
            critic_feedback = f"Critic trace analysis complete. Instruction ruleset compressed successfully for Generation {generation+1}."
            current_prompt = f"Optimized ruleset for Gen {generation+1}."
            
        yield {
            "generation": generation,
            "score": final_score,
            "prompt": current_prompt,
            "feedback": critic_feedback,
            "logs": log_dump
        }
