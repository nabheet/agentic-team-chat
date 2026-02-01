# System Summary & Getting Started

## What You've Built

A sophisticated multi-agent AI system that simulates corporate strategy meetings where 5 C-suite executives discuss business decisions. Built with LangChain and OpenAI, it demonstrates realistic corporate dynamics through AI agents with distinct personalities, expertise, and viewpoints.

## The Team Members

- **Sarah Chen (CEO)**: Visionary leader focused on long-term strategy
- **Marcus Johnson (CFO)**: Data-driven financial expert
- **Priya Patel (CTO)**: Tech innovator pushing for cutting-edge solutions  
- **James Wilson (COO)**: Operations expert focused on execution
- **Elena Rodriguez (VP Marketing)**: Customer-centric market strategist

## Quick Start (3 Steps)

```bash
# 1. Set up environment
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=your_key

# 2. Run default meeting
python main.py

# 3. Explore examples
python examples.py 2
```

## What Happens When You Run It

1. **Meeting Opens**: CEO provides vision and sets agenda
2. **Discussions Unfold**: Agents debate and discuss 5+ corporate topics
3. **Structured Debates**: CEOs and executives present opposing views
4. **Consensus Emerges**: Multiple perspectives lead to holistic decisions
5. **Closing**: CEO summarizes key decisions and next steps
6. **Output Saved**: Full transcript saved to file

## Key Features

✓ Multi-agent discussions with realistic corporate dynamics
✓ 6 different meeting scenarios (examples.py)
✓ Structured debates between executives
✓ Customizable agents and meeting formats
✓ Automatic meeting transcripts
✓ Color-coded console output
✓ Extensible architecture for your own scenarios

## Project Structure

```
agentic-team-chat/
├── main.py              # Run standard meeting
├── examples.py          # 6 example scenarios
├── utils.py             # Helper functions
├── src/
│   ├── agents.py        # Agent definitions
│   └── team_meeting.py  # Meeting orchestration
├── README.md            # Full documentation
├── QUICKSTART.md        # 5-minute setup
├── ARCHITECTURE.md      # Technical design
├── ADVANCED.md          # Advanced customization
├── .env.example         # Environment template
└── pyproject.toml       # Dependencies
```

## Common Use Cases

### 1. Default Corporate Meeting

```bash
python main.py
```

Full strategy meeting with all agents and multiple topics.

### 2. Specific Scenarios

```bash
python examples.py 1    # Quarterly meeting
python examples.py 2    # Innovation focus
python examples.py 3    # Market expansion
python examples.py 4    # Cost optimization
python examples.py 5    # Crisis response
python examples.py 6    # Growth vs profitability debate
```

### 3. Programmatic Usage

```python
from src.team_meeting import TeamMeeting

meeting = TeamMeeting()
meeting.discuss_topic("Your question here", primary_speaker="cto")
meeting.save_transcript()
```

### 4. Custom Agents & Meetings

```python
from src.agents import CorporateAgent

class CustomRole(CorporateAgent):
    def __init__(self):
        super().__init__(name="...", role="...", expertise=[...], personality="...")

# Create specialized meeting
class CustomMeeting(TeamMeeting):
    def run_custom(self):
        # Your logic
        pass
```

## Example Output

```
================================================================================
        TECHVENTURE CORP - QUARTERLY STRATEGY MEETING
================================================================================

Meeting Date: Q1 Strategic Review
Location: Executive Boardroom
Agenda: AI Innovation Strategy & Market Expansion

[Chief Executive Officer (CEO)]
Good morning everyone. We're at a critical juncture where we need to decide 
how aggressive we want to be with AI investments...

[Chief Technology Officer (CTO)]
I completely agree, Sarah. From my perspective, we're falling behind competitors
who are already deploying advanced AI...

[Chief Financial Officer (CFO)]
While I appreciate the innovation push, we need to ensure strong returns on our 
investments. The current market uncertainty demands fiscal discipline...
```

## Customization Examples

### Add New Agent

```python
class VP_Sales(CorporateAgent):
    def __init__(self):
        super().__init__(
            name="David Brooks",
            role="VP of Sales",
            expertise=["Sales Strategy", "Customer Relationships", "Revenue Growth"],
            personality="Driven, customer-focused, always pushing targets."
        )
```

### Create Custom Meeting

```python
class BoardOfDirectorsMeeting(TeamMeeting):
    def run_board_meeting(self):
        self.open_meeting()
        self.discuss_topic("Q1 financial results", primary_speaker="cfo")
        self.facilitate_debate("Growth strategy", side1="ceo", side2="cfo")
        self.closing_remarks()
        self.save_transcript("board_meeting.txt")
```

### Get Agent Opinion

```python
from src.agents import CTO

cto = CTO()
opinion = cto.think("What's our biggest technology challenge in the next 12 months?")
print(opinion)
```

## Configuration & Optimization

### Model Selection

- **gpt-4o-mini** (default): Fast, cost-effective, good quality
- **gpt-4o**: Higher quality, slower, more expensive
- **gpt-3.5-turbo**: Fastest, cheapest, lower quality

### Temperature Control

- **0.3**: Logical, consistent, predictable
- **0.7**: Balanced (default)
- **1.0**: Creative, varied, diverse

Edit in `src/agents.py`:

```python
self.llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
```

## Cost Estimates

Each meeting approximately:

- **gpt-4o-mini**: $0.10-0.20
- **gpt-4o**: $0.50-1.00
- **gpt-3.5-turbo**: $0.01-0.05

Set usage limits in OpenAI dashboard.

## Files Reference

| File | Purpose |
|------|---------|
| main.py | Entry point for standard meeting |
| examples.py | 6 different meeting scenarios |
| utils.py | Helper functions for customization |
| src/agents.py | Agent definitions (CEO, CFO, CTO, COO, Marketing) |
| src/team_meeting.py | Meeting orchestration and formats |
| README.md | Complete documentation |
| QUICKSTART.md | 5-minute setup guide |
| ARCHITECTURE.md | Technical system design |
| ADVANCED.md | Advanced customization guide |

## Troubleshooting

**Problem**: "OPENAI_API_KEY not set"
**Solution**:

1. Check `.env` file exists and has your key
2. Restart terminal after editing `.env`
3. Run: `python -c "import os; print(os.getenv('OPENAI_API_KEY'))"`

**Problem**: Slow responses
**Solution**: Use gpt-4o-mini, reduce topics, lower temperature

**Problem**: Import errors
**Solution**: Run `pip install -e .` or `uv sync`

**Problem**: API rate limits
**Solution**: LangChain handles this automatically. Check OpenAI usage dashboard.

## Next Steps

1. **Try Different Scenarios**: Run `python examples.py` with different numbers
2. **Create Custom Agents**: Extend `CorporateAgent` for your needs
3. **Build Custom Meetings**: Extend `TeamMeeting` for specific use cases
4. **Integrate with Apps**: Use as backend for web apps, dashboards, etc.
5. **Experiment with Topics**: Modify meeting topics and see different responses

## Performance Tips

- Use `gpt-4o-mini` for regular meetings
- Create focused meetings (fewer topics) for faster execution
- Run parallel meetings with ThreadPoolExecutor for batch processing
- Cache agent responses if running similar meetings

## Advanced Features

- **Custom Agent Personalities**: Create agents with specific viewpoints
- **Debate Formats**: Structure multi-round debates between executives
- **Specialized Teams**: Pre-configured teams for different org types
- **Meeting Transcripts**: Automatic saving and analysis
- **Extensible Architecture**: Easy to add new features

## API Usage

Each agent response = 1 API call

- Single thought: 1 call
- Response to colleague: 1 call
- Full meeting (10 calls): ~30-60 seconds

Monitor usage in OpenAI dashboard.

## Documentation

- **README.md**: Full feature documentation
- **QUICKSTART.md**: Quick setup and first meeting
- **ARCHITECTURE.md**: Technical system design
- **ADVANCED.md**: Advanced customization examples

## Support & Issues

1. Check documentation files first
2. Review examples.py for implementation patterns
3. Check agent system prompts for behavior issues
4. Verify OpenAI API key and credits

## Key Concepts

**Agents**: AI entities with names, roles, expertise, and personalities
**LLM**: Language model (gpt-4o-mini) that generates responses
**Prompts**: System prompts give context; user prompts ask questions
**Meeting**: Orchestration class managing agent interactions
**Transcript**: Record of all discussion saved to file

## What Makes This System Unique

1. **Role-specific expertise**: Each agent has distinct areas of focus
2. **Realistic dynamics**: Agents challenge each other realistically
3. **Multiple formats**: Discussion, debate, round-table options
4. **Fully extensible**: Easy to add new agents and scenarios
5. **Production-ready**: Error handling, transcripts, configuration

## Future Possibilities

- Integrate with real business data
- Connect to actual databases
- Build web interface for visualization
- Add voting/consensus mechanisms
- Create agent memory across meetings
- Support more than 5 agents
- Add custom company scenarios

---

**Ready to start?** Run `python main.py` with your OpenAI API key in `.env`!
