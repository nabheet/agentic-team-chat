"""Team meeting orchestration and discussion management."""

from colorama import Fore, Style, init
from agents import CEO, CFO, CTO, COO, VPMarketing
from tts import create_voice_engine

init(autoreset=True)


class TeamMeeting:
    """Orchestrates discussions between multiple corporate agents."""

    def __init__(self, enable_audio: bool = False):
        """Initialize the team with all agents.

        Args:
            enable_audio: Whether to enable text-to-speech output
        """
        self.agents = {
            "ceo": CEO(),
            "cfo": CFO(),
            "cto": CTO(),
            "coo": COO(),
            "marketing": VPMarketing(),
        }
        self.meeting_transcript = []
        self.voice_engine = create_voice_engine(enable_audio=enable_audio)
        self.enable_audio = enable_audio

    def print_header(self, text: str, color: str = Fore.CYAN):
        """Print a formatted header."""
        print(f"\n{color}{'=' * 80}")
        print(f"{color}{text.center(80)}")
        print(f"{color}{'=' * 80}{Style.RESET_ALL}\n")

    def print_speaker(self, agent_name: str, role: str, content: str):
        """Print a speaker's statement with formatting."""
        color_map = {
            "ceo": Fore.MAGENTA,
            "cfo": Fore.YELLOW,
            "cto": Fore.CYAN,
            "coo": Fore.GREEN,
            "marketing": Fore.BLUE,
        }
        color = color_map.get(agent_name, Fore.WHITE)

        print(f"{color}[{role}]{Style.RESET_ALL}")
        print(f"{content}\n")

        # Generate audio if enabled
        if self.enable_audio and self.voice_engine:
            try:
                self.voice_engine.speak(content, agent_name)
            except Exception as e:
                print(f"{Fore.RED}[TTS Error]: {e}{Style.RESET_ALL}")

        self.meeting_transcript.append(f"[{role}]\n{content}\n")

    def open_meeting(self):
        """Start the team meeting with CEO opening remarks."""
        self.print_header("TECHVENTURE CORP - QUARTERLY STRATEGY MEETING")
        print(f"{Fore.WHITE}Meeting Date: Q1 Strategic Review")
        print("Location: Executive Boardroom")
        print("Agenda: AI Innovation Strategy & Market Expansion\n")

        ceo = self.agents["ceo"]
        opening = ceo.think(
            "Open a quarterly strategy meeting by setting the agenda for discussing AI innovation and market expansion"
        )
        self.print_speaker("ceo", ceo.role, opening)

    def discuss_topic(
        self, topic: str, primary_speaker: str = "ceo", num_responses: int = 3
    ):
        """Facilitate a discussion on a specific topic."""
        self.print_header(f"TOPIC: {topic}")

        # Primary speaker opens the topic
        agent = self.agents[primary_speaker]
        opening_statement = agent.think(topic)
        self.print_speaker(primary_speaker, agent.role, opening_statement)

        # Get responses from other agents
        other_agents = [a for a in self.agents.keys() if a != primary_speaker]
        respondents = other_agents[:num_responses]

        for respondent_key in respondents:
            respondent = self.agents[respondent_key]
            response = respondent.respond_to_colleague(
                agent.name, opening_statement, topic
            )
            self.print_speaker(respondent_key, respondent.role, response)

    def facilitate_debate(self, debate_topic: str, side1: str, side2: str):
        """Facilitate a structured debate between two executives."""
        self.print_header(f"DEBATE: {debate_topic}")

        agent1 = self.agents[side1]
        agent2 = self.agents[side2]

        # Side 1 opens
        print(f"{Fore.WHITE}[Position 1 - {agent1.role}]{Style.RESET_ALL}")
        statement1 = agent1.think(f"Argue for: {debate_topic}")
        self.print_speaker(side1, agent1.role, statement1)

        # Side 2 responds
        print(f"{Fore.WHITE}[Position 2 - {agent2.role}]{Style.RESET_ALL}")
        statement2 = agent2.respond_to_colleague(agent1.name, statement1, debate_topic)
        self.print_speaker(side2, agent2.role, statement2)

        # Side 1 counter-responds
        print(f"{Fore.WHITE}[Rebuttal - {agent1.role}]{Style.RESET_ALL}")
        rebuttal = agent1.respond_to_colleague(agent2.name, statement2, debate_topic)
        self.print_speaker(side1, agent1.role, rebuttal)

    def round_table_discussion(self, topic: str):
        """Conduct a round-table discussion where each agent contributes."""
        self.print_header(f"ROUND TABLE: {topic}")

        # Each agent contributes
        for key, agent in self.agents.items():
            thought = agent.think(topic)
            self.print_speaker(key, agent.role, thought)

    def closing_remarks(self):
        """CEO provides closing remarks."""
        self.print_header("CLOSING REMARKS")

        ceo = self.agents["ceo"]
        closing = ceo.think(
            "Provide closing remarks summarizing the key decisions and next steps from this strategy meeting"
        )
        self.print_speaker("ceo", ceo.role, closing)

    def save_transcript(self, filename: str = "meeting_transcript.txt"):
        """Save the meeting transcript to a file."""
        with open(filename, "w") as f:
            f.write("\n".join(self.meeting_transcript))
        print(f"\n{Fore.GREEN}Meeting transcript saved to {filename}{Style.RESET_ALL}")

    def run_full_meeting(self):
        """Run a complete corporate strategy meeting."""
        self.open_meeting()

        # AI Innovation Strategy
        self.discuss_topic(
            "Should we invest heavily in in-house AI/ML capabilities or partner with external AI providers?",
            primary_speaker="cto",
        )

        # Budget vs Innovation debate
        self.facilitate_debate(
            "Budget Allocation: R&D Investment vs Shareholder Returns",
            side1="cto",
            side2="cfo",
        )

        # Market Expansion
        self.round_table_discussion(
            "How should we position TechVenture in emerging markets while managing operational complexity?"
        )

        # Team Integration Topic
        self.discuss_topic(
            "What are the key talent challenges in scaling our AI team?",
            primary_speaker="coo",
        )

        # Final Strategy
        self.discuss_topic(
            "What should be our primary competitive advantage in the next 18 months?",
            primary_speaker="marketing",
        )

        self.closing_remarks()
        self.save_transcript()


def main():
    """Run the corporate strategy meeting."""
    meeting = TeamMeeting()
    meeting.run_full_meeting()


if __name__ == "__main__":
    main()
