# Agentic Team Chat - Corporate Strategy Meeting

An innovative AI system built with LangChain where multiple agents, each representing a different C-suite executive, collaborate and discuss corporate strategy and business direction.

## Overview

This project demonstrates a multi-agent AI system where five corporate executives with distinct expertise and perspectives engage in strategic discussions about business decisions. Each agent operates with its own personality, expertise domain, and LLM instance, enabling realistic and nuanced corporate deliberations.

### The Team

1. **Sarah Chen** - CEO (Chief Executive Officer)
   - Expertise: Strategic Planning, Market Leadership, Stakeholder Management
   - Focus: Long-term vision, shareholder value, strategic alignment

2. **Marcus Johnson** - CFO (Chief Financial Officer)
   - Expertise: Financial Planning, Risk Management, Budget Allocation
   - Focus: Financial sustainability, ROI, cost efficiency

3. **Priya Patel** - CTO (Chief Technology Officer)
   - Expertise: AI/ML Innovation, Cloud Infrastructure, System Architecture
   - Focus: Technical innovation, cutting-edge solutions, scalability

4. **James Wilson** - COO (Chief Operating Officer)
   - Expertise: Operations Management, Process Optimization, Team Productivity
   - Focus: Execution, efficiency, team capabilities

5. **Elena Rodriguez** - VP of Marketing
   - Expertise: Market Research, Customer Acquisition, Brand Positioning
   - Focus: Customer needs, market realities, go-to-market strategy

## Features

- **Multi-Agent Discussions**: Five AI agents with distinct roles, expertise, and personalities
- **Multiple Discussion Formats**:
  - Open discussions on specific topics
  - Structured debates between executives
  - Round-table discussions where all agents contribute
- **Context-Aware Responses**: Each agent provides insights from their unique perspective
- **Realistic Corporate Dynamics**: Agents challenge each other, build on ideas, and defend their positions
- **Text-to-Speech Audio**: Each agent speaks with a distinct voice (184 system voices available)
- **Meeting Transcript**: Automatically saves a transcript of the entire meeting

## Architecture

### Core Components

- **agents.py**: Defines `CorporateAgent` base class and specific executive roles
  - Each agent has customizable system prompts
  - Agents can think on topics independently or respond to colleagues
  - Integration with LangChain's ChatOpenAI

- **team_meeting.py**: Orchestrates multi-agent discussions
  - `TeamMeeting` class manages agent interactions
  - Supports various discussion formats
  - Generates formatted output with color-coding
  - Maintains meeting transcripts

- **main.py**: Entry point for running a complete strategy meeting

## Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Setup

1. **Clone the repository**:

   ```bash
   cd /Users/nabheet/code/github/agentic-team-chat
   ```

2. **Create environment file**:

   ```bash
   cp .env.example .env
   ```

3. **Add your OpenAI API key to `.env`**:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   # or if using UV:
   uv sync
   ```

## Usage

### Run a Full Strategy Meeting

```bash
# Text-only output
python main.py

# With audio (agents speak their statements)
python main.py --audio
```

This will execute a complete corporate strategy meeting including:

- CEO opening remarks
- AI innovation strategy discussion
- Budget vs. Innovation debate
- Market expansion round-table
- Talent scaling discussion
- Competitive advantage positioning
- CEO closing remarks

### Programmatic Usage

Create custom meetings by using the `TeamMeeting` class:

```python
from src.team_meeting import TeamMeeting

# Create meeting without audio
meeting = TeamMeeting()

# Or with audio enabled
meeting = TeamMeeting(enable_audio=True)

# Run specific discussion formats
meeting.open_meeting()
meeting.discuss_topic("Your topic here", primary_speaker="cto")
meeting.facilitate_debate("Topic", side1="cto", side2="cfo")
meeting.round_table_discussion("Topic")
meeting.closing_remarks()
meeting.save_transcript("my_meeting.txt")
```

### Create Custom Agents

Extend the `CorporateAgent` class to create additional roles:

```python
from src.agents import CorporateAgent

class CHRO(CorporateAgent):
    """Chief Human Resources Officer"""
    def __init__(self):
        super().__init__(
            name="Your Name",
            role="Chief Human Resources Officer",
            expertise=["Talent Acquisition", "Organizational Design", "Culture"],
            personality="Your personality description"
        )
```

## Project Structure

```
agentic-team-chat/
├── main.py                 # Entry point
├── pyproject.toml          # Project configuration
├── .env.example            # Environment variables template
├── README.md              # This file
└── src/
    ├── __init__.py
    ├── agents.py          # Agent definitions
    ├── team_meeting.py    # Meeting orchestration
    └── tts.py             # Text-to-speech engine
```

## Meeting Output

The system generates:

- **Console Output**: Color-coded speaker names and statements with real-time display
- **Transcript File**: `meeting_transcript.txt` with the complete discussion

## Example Output

```
================================================================================
        TECHVENTURE CORP - QUARTERLY STRATEGY MEETING
================================================================================

Meeting Date: Q1 Strategic Review
Location: Executive Boardroom
Agenda: AI Innovation Strategy & Market Expansion

[Chief Executive Officer (CEO)]
Thank you all for joining today's strategic review. As we navigate the evolving 
market landscape, I want to focus our discussion on three critical areas...

[Chief Technology Officer (CTO)]
I appreciate the focus on innovation. From my perspective, we need to make a 
strategic decision about our AI capabilities...
```

## Configuration

### Model Selection

Edit the model in `agents.py`:

```python
self.llm = ChatOpenAI(
    model_name="gpt-4o-mini",  # Change this
    temperature=0.7            # Adjust creativity (0-1)
)
```

### Temperature

- **Lower (0.3-0.5)**: More consistent, logical responses
- **Higher (0.7-1.0)**: More creative, varied responses

## Advanced Features

### Custom Discussion Scenarios

Create specialized meeting scenarios:

```python
class BoardMeeting(TeamMeeting):
    def run_investor_update(self):
        self.discuss_topic("Quarterly financial performance", primary_speaker="cfo")
        self.discuss_topic("Product roadmap", primary_speaker="cto")
        self.closing_remarks()
```

### Agent Memory

The system maintains conversation history for each agent. Extend this for multi-turn conversations:

```python
agent = self.agents["ceo"]
agent.conversation_history.append(message)
```

## Performance Considerations

- Each agent response requires an API call to OpenAI
- Meeting with all agents discussing 5+ topics may consume multiple API credits
- Consider using `gpt-4o-mini` for cost efficiency

## Troubleshooting

### "OPENAI_API_KEY not set"

Ensure your `.env` file exists and contains a valid API key

### Rate limiting errors

OpenAI may rate-limit concurrent requests. The system handles this automatically with retries.

### Unexpected agent responses

Adjust the system prompt in `get_system_prompt()` or temperature for different behaviors

## Future Enhancements

- [ ] Add persistence for meeting history
- [ ] Implement agent memory across meetings
- [ ] Add different company scenarios (startup, non-profit, etc.)
- [ ] Create web interface for meeting visualization
- [ ] Add voting/consensus mechanisms
- [ ] Support for more than 5 agents
- [ ] Custom agenda configuration
- [ ] Meeting recording and playback

## Dependencies

- **langchain**: Multi-agent orchestration framework
- **langchain-openai**: OpenAI integration
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation
- **colorama**: Console color output
- **pyttsx3**: Text-to-speech for agent voices (optional)

## License

MIT

## Contributing

Contributions welcome! Areas for enhancement:

- Additional agent types
- New discussion formats
- Better meeting transcripts
- Performance optimizations
- Additional LLM providers

## References

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
