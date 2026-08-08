class BaseAgent:
    """The standard, secure foundation for all autonomous agents."""
    
    def __init__(self, agent_name):
        self.name = agent_name        
        self.__status = "Idle"        
        self.__action_logs = []        
    
    def get_status(self):
        """Safely inspects the agent's current state."""
        return self.__status

    def _update_status(self, new_status):
        """Internal helper method to update status and update history logs."""
        self.__status = new_status
        self.__action_logs.append(f"Status changed to: {new_status}")

    def read_logs(self, admin_authenticated=False):
        """Protects historical tracking data with a security clearance gate."""
        if admin_authenticated:
            return self.__action_logs
        return "ACCESS DENIED: Administrative credentials required."

lead_agent = BaseAgent(agent_name="Nexus-9")
print(f"Safe Status Access: {lead_agent.get_status()}")
print(f"Secure Logs (Unauthorized): {lead_agent.read_logs(admin_authenticated=False)}")
lead_agent._update_status('active')
print(f"Secure Logs (Authorized):   {lead_agent.read_logs(admin_authenticated=True)}")