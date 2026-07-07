class ServerEnvironment:
    def __init__(self):
        self.target_actions = ["log", "process", "restart"]  # Short keywords for bulletproof matching
        self.current_step = 0
        self.history = []

    def reset(self):
        self.current_step = 0
        self.history = []

    @property
    def is_completed(self):
        return self.current_step >= len(self.target_actions)

    def get_state_summary(self):
        if self.is_completed:
            return "Server is completely healthy and running."
        if self.current_step == 0:
            return "CRITICAL ERROR: Server is completely unresponsive. Log data is unread."
        elif self.current_step == 1:
            return "LOGS CLEAN: High resource CPU usage detected from a stuck process."
        elif self.current_step == 2:
            return "PROCESS KILLED: RAM cleared, but system requires a full reboot or restart."
        return "Unknown state."

    def execute_action(self, action_string):
        if self.is_completed:
            return "Success: No further actions required."
        
        expected = self.target_actions[self.current_step]
        
        # 🟢 BULLETPROOF FLEXIBLE MATCHING: Checks if the keyword exists anywhere in the agent's text
        if expected in action_string.lower():
            self.current_step += 1
            return f"Success: Advanced to step {self.current_step}."
        else:
            return f"Failure: Action didn't match. Looking for something related to '{expected}'."

    def get_metrics(self):
        max_steps = len(self.target_actions)
        score = int((self.current_step / max_steps) * 100)
        return {"score": score}
