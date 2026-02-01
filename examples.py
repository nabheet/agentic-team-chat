#!/usr/bin/env python3
"""
Example scenarios showing different meeting configurations and use cases.

This file demonstrates how to:
1. Run a standard corporate meeting
2. Create custom meeting scenarios
3. Use specialized teams (startup, consulting, healthcare)
"""

import os
import sys
import argparse
from pathlib import Path

# Must set path before imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from dotenv import load_dotenv
from colorama import Fore, Style
from team_meeting import TeamMeeting

load_dotenv()


# Global variable to store enable_audio flag
enable_audio = False


def scenario_1_standard_meeting():
    """Scenario 1: Standard quarterly strategy meeting (default)."""
    print(
        f"\n{Fore.CYAN}SCENARIO 1: Standard Quarterly Strategy Meeting{Style.RESET_ALL}\n"
    )
    meeting = TeamMeeting(enable_audio=enable_audio)
    meeting.run_full_meeting()


def scenario_2_innovation_focused():
    """Scenario 2: Focus on AI/ML innovation and digital transformation."""
    print(
        f"\n{Fore.CYAN}SCENARIO 2: Innovation & Digital Transformation Summit{Style.RESET_ALL}\n"
    )
    meeting = TeamMeeting(enable_audio=enable_audio)

    meeting.open_meeting()
    meeting.print_header("INNOVATION FOCUS")

    # Round table on innovation priorities
    meeting.round_table_discussion(
        "What should be our innovation priorities for the next 12 months? "
        "AI/ML, blockchain, IoT, or something else?"
    )

    # Debate: Build vs. Buy vs. Partner
    meeting.facilitate_debate(
        "Should we build AI capabilities in-house, acquire a specialized AI company, or partner with AI providers?",
        side1="cto",
        side2="cfo",
    )

    # Resource allocation discussion
    meeting.discuss_topic(
        "How much should we allocate from our budget to innovation initiatives versus core operations?",
        primary_speaker="ceo",
    )

    meeting.closing_remarks()
    meeting.save_transcript("innovation_meeting.txt")


def scenario_3_market_expansion():
    """Scenario 3: Market expansion and go-to-market strategy."""
    print(
        f"\n{Fore.CYAN}SCENARIO 3: Market Expansion & Go-to-Market Strategy{Style.RESET_ALL}\n"
    )
    meeting = TeamMeeting(enable_audio=enable_audio)

    meeting.open_meeting()
    meeting.print_header("MARKET EXPANSION")

    # CEO sets context
    meeting.discuss_topic(
        "We're considering expansion into Asian markets. What are the key considerations?",
        primary_speaker="ceo",
    )

    # Debate: Organic growth vs. acquisitions
    meeting.facilitate_debate(
        "Should we expand through organic growth (new offices) or acquisitions (buying local companies)?",
        side1="marketing",
        side2="cfo",
    )

    # Round table on execution
    meeting.round_table_discussion(
        "What are the biggest operational challenges in executing a multi-market strategy?"
    )

    meeting.closing_remarks()
    meeting.save_transcript("expansion_meeting.txt")


def scenario_4_cost_optimization():
    """Scenario 4: Cost optimization and operational efficiency."""
    print(
        f"\n{Fore.CYAN}SCENARIO 4: Cost Optimization & Operational Efficiency{Style.RESET_ALL}\n"
    )
    meeting = TeamMeeting(enable_audio=enable_audio)

    meeting.open_meeting()
    meeting.print_header("COST OPTIMIZATION")

    # CFO leads cost discussion
    meeting.discuss_topic(
        "We need to reduce operational costs by 15% without impacting revenue. How?",
        primary_speaker="cfo",
    )

    # Debate: Cost cutting vs. Investment
    meeting.facilitate_debate(
        "Should we prioritize cost reduction or strategic investments in technology and talent?",
        side1="cfo",
        side2="cto",
    )

    # Operational perspective
    meeting.discuss_topic(
        "What are the operational levers we can pull to achieve efficiency gains?",
        primary_speaker="coo",
    )

    meeting.closing_remarks()
    meeting.save_transcript("cost_optimization_meeting.txt")


def scenario_5_crisis_response():
    """Scenario 5: Crisis response and business continuity."""
    print(
        f"\n{Fore.CYAN}SCENARIO 5: Crisis Response & Business Continuity{Style.RESET_ALL}\n"
    )
    meeting = TeamMeeting(enable_audio=enable_audio)

    meeting.print_header("CRISIS RESPONSE MEETING")

    # CEO crisis statement
    print(f"\n{Fore.RED}URGENT: Crisis Response Meeting{Style.RESET_ALL}\n")
    ceo = meeting.agents["ceo"]
    crisis_statement = ceo.think(
        "Our main product has a critical security vulnerability discovered. "
        "How do we respond to protect customers and the company?"
    )
    meeting.print_speaker("ceo", ceo.role, crisis_statement)

    # Round table on immediate actions
    meeting.round_table_discussion(
        "What are the immediate actions we need to take in the first 24 hours?"
    )

    # Technical response
    meeting.discuss_topic(
        "What's the technical solution and timeline to fix this vulnerability?",
        primary_speaker="cto",
    )

    # Communication strategy
    meeting.discuss_topic(
        "How do we communicate with customers and stakeholders about this issue?",
        primary_speaker="marketing",
    )

    meeting.closing_remarks()
    meeting.save_transcript("crisis_response_meeting.txt")


def scenario_6_one_on_one_debate():
    """Scenario 6: Deep dive debate between two executives."""
    print(
        f"\n{Fore.CYAN}SCENARIO 6: CEO vs CFO - Growth vs. Profitability Debate{Style.RESET_ALL}\n"
    )
    meeting = TeamMeeting(enable_audio=enable_audio)

    meeting.print_header("EXECUTIVE DEBATE: Growth vs. Profitability")

    # Deep multi-round debate
    meeting.facilitate_debate(
        "Should we prioritize rapid growth with near-term losses or slower growth with profitability?",
        side1="ceo",
        side2="cfo",
    )

    print("\n" + "=" * 80 + "\n")

    # Second round with other perspectives
    meeting.discuss_topic(
        "What's the operational impact of each strategy on our team and systems?",
        primary_speaker="coo",
    )

    meeting.save_transcript("growth_vs_profitability_debate.txt")


def list_scenarios():
    """List all available scenarios."""
    scenarios = {
        "1": ("Standard Quarterly Meeting", scenario_1_standard_meeting),
        "2": ("Innovation & Digital Transformation", scenario_2_innovation_focused),
        "3": ("Market Expansion Strategy", scenario_3_market_expansion),
        "4": ("Cost Optimization", scenario_4_cost_optimization),
        "5": ("Crisis Response", scenario_5_crisis_response),
        "6": ("Growth vs. Profitability Debate", scenario_6_one_on_one_debate),
    }
    return scenarios


def main():
    """Main function to run example scenarios."""
    parser = argparse.ArgumentParser(
        description="Run Agentic Team Chat example scenarios."
    )
    parser.add_argument(
        "scenario",
        nargs="?",
        help="Scenario number (1-6). If not provided, you'll be prompted.",
    )
    parser.add_argument(
        "--audio",
        action="store_true",
        help="Enable text-to-speech output with agent-specific voices",
    )
    args = parser.parse_args()

    # Set global enable_audio flag
    global enable_audio
    enable_audio = args.audio

    print(f"\n{Fore.CYAN}{'=' * 80}{Style.RESET_ALL}")
    print(
        f"{Fore.CYAN}Agentic Team Chat - Example Scenarios{Style.RESET_ALL}".center(80)
    )
    print(f"{Fore.CYAN}{'=' * 80}{Style.RESET_ALL}\n")

    # Check for OpenAI key
    if not os.getenv("OPENAI_API_KEY"):
        print(f"{Fore.RED}Error: OPENAI_API_KEY not set{Style.RESET_ALL}")
        sys.exit(1)

    if enable_audio:
        print(
            f"{Fore.CYAN}Audio output enabled. Agents will speak their statements.{Style.RESET_ALL}\n"
        )

    scenarios = list_scenarios()

    print(f"{Fore.GREEN}Available Scenarios:{Style.RESET_ALL}\n")
    for key, (name, _) in scenarios.items():
        print(f"  {key}. {name}")

    print("\nUsage: python examples.py [scenario_number] [--audio]")
    print("Example: python examples.py 2 --audio\n")

    # Get scenario from command line or user input
    if args.scenario:
        choice = args.scenario
    else:
        choice = input(f"{Fore.YELLOW}Select scenario (1-6): {Style.RESET_ALL}").strip()

    if choice in scenarios:
        name, func = scenarios[choice]
        print(f"\n{Fore.GREEN}Running: {name}{Style.RESET_ALL}\n")
        func()
        print(f"\n{Fore.GREEN}Meeting completed!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Invalid scenario. Please select 1-6.{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()
