"""Agentic Team Chat - Corporate Strategy Meeting with AI Agents."""

from .agents import CorporateAgent, CEO, CFO, CTO, COO, VPMarketing
from .team_meeting import TeamMeeting
from .tts import AgentVoice, create_voice_engine

__version__ = "0.1.0"

__all__ = [
    "CorporateAgent",
    "CEO",
    "CFO",
    "CTO",
    "COO",
    "VPMarketing",
    "TeamMeeting",
    "AgentVoice",
    "create_voice_engine",
]
