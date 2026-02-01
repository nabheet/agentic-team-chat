"""Utilities for creating custom agents and meeting scenarios."""

from src.agents import CorporateAgent


def create_custom_agent(
    name: str, role: str, expertise: list[str], personality: str
) -> CorporateAgent:
    """
    Create a custom corporate agent.

    Args:
        name: Agent's full name
        role: Job title/role
        expertise: List of expertise areas
        personality: Description of personality and decision-making style

    Returns:
        CorporateAgent instance
    """

    class CustomAgent(CorporateAgent):
        pass

    return CustomAgent(
        name=name, role=role, expertise=expertise, personality=personality
    )


def create_tech_startup_team():
    """Create a team for a tech startup context."""
    from src.agents import CEO, CFO, CTO, COO

    return {
        "ceo": CEO(),
        "cfo": CFO(),
        "cto": CTO(),
        "coo": COO(),
    }


def create_consulting_firm_team():
    """Create agents representing a consulting firm leadership."""
    agents = {}

    # Managing Partner
    agents["managing_partner"] = create_custom_agent(
        name="Alexandra Sterling",
        role="Managing Partner",
        expertise=[
            "Client Relations",
            "Business Strategy",
            "Consulting Methodology",
            "Market Leadership",
        ],
        personality="Driven, client-focused, and results-oriented. Values firm profitability and market reputation.",
    )

    # Operations Partner
    agents["ops_partner"] = create_custom_agent(
        name="David Chen",
        role="Operations Partner",
        expertise=[
            "Resource Planning",
            "Project Management",
            "Team Development",
            "Quality Assurance",
        ],
        personality="Process-oriented, detail-focused. Concerned with delivery excellence and team capacity.",
    )

    # Innovation Partner
    agents["innovation_partner"] = create_custom_agent(
        name="Sofia Rodriguez",
        role="Innovation Partner",
        expertise=[
            "Digital Transformation",
            "Technology Integration",
            "Market Trends",
            "New Offerings",
        ],
        personality="Forward-thinking, experimental, passionate about emerging technologies and new business models.",
    )

    return agents


def create_healthcare_organization_team():
    """Create agents representing a healthcare organization leadership."""
    agents = {}

    # Chief Medical Officer
    agents["cmo"] = create_custom_agent(
        name="Dr. James Mitchell",
        role="Chief Medical Officer",
        expertise=[
            "Patient Care Quality",
            "Clinical Standards",
            "Medical Research",
            "Regulatory Compliance",
        ],
        personality="Evidence-based, patient-focused, committed to clinical excellence and safety.",
    )

    # Chief Financial Officer
    agents["cfo"] = create_custom_agent(
        name="Patricia Wong",
        role="Chief Financial Officer",
        expertise=[
            "Healthcare Finance",
            "Insurance Management",
            "Cost Control",
            "Revenue Optimization",
        ],
        personality="Financially disciplined, pragmatic about resource constraints, focused on sustainability.",
    )

    # Chief Operating Officer
    agents["coo"] = create_custom_agent(
        name="Robert Jackson",
        role="Chief Operating Officer",
        expertise=[
            "Hospital Operations",
            "Staff Management",
            "Supply Chain",
            "Process Efficiency",
        ],
        personality="Operational expert, people-focused, concerned with staff satisfaction and operational excellence.",
    )

    return agents


if __name__ == "__main__":
    print(
        "This module provides utilities for creating custom agents and meeting scenarios."
    )
    print("\nAvailable functions:")
    print("- create_custom_agent(): Create a single custom agent")
    print("- create_tech_startup_team(): Pre-configured startup team")
    print("- create_consulting_firm_team(): Pre-configured consulting firm team")
    print("- create_healthcare_organization_team(): Pre-configured healthcare team")
