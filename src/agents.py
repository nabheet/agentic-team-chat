"""Base corporate agent class and specialized agent roles."""

from typing import Optional
from pydantic import BaseModel, ConfigDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage


class CorporateAgent(BaseModel):
    """Base class for a corporate team member agent."""

    name: str
    role: str
    expertise: list[str]
    personality: str
    llm: Optional[ChatOpenAI] = None
    conversation_history: list[BaseMessage] = []

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init__(
        self, name: str, role: str, expertise: list[str], personality: str, **kwargs
    ):
        super().__init__(
            name=name, role=role, expertise=expertise, personality=personality, **kwargs
        )
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        self.conversation_history = []

    def get_system_prompt(self) -> str:
        """Get the system prompt for this agent."""
        return f"""You are {self.name}, the {self.role} at TechVenture Corp.

Your expertise: {", ".join(self.expertise)}
Your personality: {self.personality}

You are participating in a corporate strategy meeting. Provide thoughtful, data-driven insights from your perspective. 
Be respectful of other team members' viewpoints while advocating for your department's priorities.
Keep responses concise (2-3 sentences) unless asked for more detail.
Use real business terminology and concepts relevant to your role."""

    def think(self, topic: str, context: str = ""):
        """Generate a response on a topic based on agent's expertise and personality."""
        if not self.llm:
            raise ValueError("LLM not initialized")
        system_prompt = self.get_system_prompt()

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Topic: {topic}\n\nContext: {context}"),
        ]

        response = self.llm.invoke(messages)
        content = response.content
        if isinstance(content, list):
            return str(content[0]) if content else ""
        return str(content)

    def respond_to_colleague(
        self, colleague_name: str, colleague_statement: str, topic: str
    ):
        """Respond to a colleague's statement during a meeting."""
        if not self.llm:
            raise ValueError("LLM not initialized")
        system_prompt = self.get_system_prompt()

        prompt = f"""Your colleague {colleague_name} just said:
"{colleague_statement}"

You're discussing: {topic}

Provide a thoughtful response that either builds on their idea, offers an alternative perspective, 
or raises important considerations from your area of expertise."""

        messages = [SystemMessage(content=system_prompt), HumanMessage(content=prompt)]

        response = self.llm.invoke(messages)
        content = response.content
        if isinstance(content, list):
            return str(content[0]) if content else ""
        return str(content)


class CEO(CorporateAgent):
    """Chief Executive Officer - focuses on overall vision and profitability."""

    def __init__(self):
        super().__init__(
            name="Sarah Chen",
            role="Chief Executive Officer (CEO)",
            expertise=[
                "Strategic Planning",
                "Market Leadership",
                "Stakeholder Management",
                "Business Growth",
            ],
            personality="Visionary, decisive, and focused on long-term value creation. Values strategic alignment and shareholder returns.",
        )


class CFO(CorporateAgent):
    """Chief Financial Officer - focuses on financial health and resource allocation."""

    def __init__(self):
        super().__init__(
            name="Marcus Johnson",
            role="Chief Financial Officer (CFO)",
            expertise=[
                "Financial Planning",
                "Risk Management",
                "Budget Allocation",
                "ROI Analysis",
            ],
            personality="Data-driven, risk-conscious, and pragmatic. Ensures financial sustainability and scrutinizes spending.",
        )


class CTO(CorporateAgent):
    """Chief Technology Officer - focuses on technical innovation and infrastructure."""

    def __init__(self):
        super().__init__(
            name="Priya Patel",
            role="Chief Technology Officer (CTO)",
            expertise=[
                "AI/ML Innovation",
                "Cloud Infrastructure",
                "System Architecture",
                "Tech Stack Selection",
            ],
            personality="Technically ambitious, forward-thinking, and passionate about cutting-edge solutions. Sometimes optimistic about timelines.",
        )


class COO(CorporateAgent):
    """Chief Operating Officer - focuses on execution and efficiency."""

    def __init__(self):
        super().__init__(
            name="James Wilson",
            role="Chief Operating Officer (COO)",
            expertise=[
                "Operations Management",
                "Process Optimization",
                "Team Productivity",
                "Supply Chain",
            ],
            personality="Detail-oriented, process-focused, and pragmatic. Concerned with execution realities and team capabilities.",
        )


class VPMarketing(CorporateAgent):
    """VP of Marketing - focuses on market positioning and customer acquisition."""

    def __init__(self):
        super().__init__(
            name="Elena Rodriguez",
            role="Vice President of Marketing",
            expertise=[
                "Market Research",
                "Customer Acquisition",
                "Brand Positioning",
                "Product Launch",
            ],
            personality="Customer-centric, creative, and data-focused. Advocates for customer needs and market realities.",
        )
