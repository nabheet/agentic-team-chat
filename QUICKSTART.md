# Quick Start Guide

## 5-Minute Setup

### Step 1: Get Your OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy the key (keep it secret!)

### Step 2: Configure Environment

```bash
# Create .env file
cp .env.example .env

# Edit .env and add your API key
# OPENAI_API_KEY=your_key_here
```

### Step 3: Run Your First Meeting

```bash
# Run the default strategy meeting (text only)
uv run python main.py

# Run with audio (agents speak with different voices)
uv run python main.py --audio
```

## What Happens When You Run It

1. **Meeting Opens**: CEO provides opening remarks
2. **Discussions**: Agents debate and discuss 5 corporate topics
3. **Debates**: Structured debates between executives
4. **Closing**: CEO summarizes decisions
5. **Output**: Meeting transcript saved to `meeting_transcript.txt`

## Audio Support

Enable text-to-speech to hear agents speak:

```bash
# Run with audio enabled
uv run python main.py --audio
```

Each agent speaks with a unique voice:

- CEO: System voice #1 at 180 WPM
- CFO: System voice #2 at 160 WPM  
- CTO: System voice #3 at 200 WPM
- COO: System voice #4 at 170 WPM
- VP Marketing: System voice #5 at 190 WPM

## Customization

### Create a Custom Agent

```python
from src.agents import CorporateAgent

class CFO(CorporateAgent):
    def __init__(self):
        super().__init__(
            name="Your Name",
            role="Your Role",
            expertise=["Area1", "Area2"],
            personality="Your description"
        )
```

### Run a Custom Meeting

```python
from src.team_meeting import TeamMeeting

meeting = TeamMeeting()
meeting.open_meeting()
meeting.discuss_topic("Your topic")
meeting.closing_remarks()
meeting.save_transcript("custom_meeting.txt")
```

## Troubleshooting

### OPENAI_API_KEY not set

- Verify `.env` file exists
- Check file has correct format: `OPENAI_API_KEY=your_key`
- Run: `python -c "import os; print(os.getenv('OPENAI_API_KEY'))"`

### API Errors

- Check API key is valid
- Verify you have API credits
- Check OpenAI status page

### Python Import Errors

- Run: `pip install -e .`
- Or use: `uv sync`

## Performance Tips

- **Faster responses**: Use `gpt-4o-mini` (default)
- **Better quality**: Use `gpt-4o` (more expensive)
- **Reduce cost**: Lower number of topics or agents
- **Speed up**: Run fewer discussion rounds

## Next Steps

1. Try different scenarios
2. Create custom agents
3. Modify system prompts
4. Add new discussion types
5. Integrate with your application

## Files Overview

- `main.py` - Default meeting entry point
- `examples.py` - 6 different scenario examples
- `utils.py` - Helper functions for agent creation
- `src/agents.py` - Agent definitions
- `src/team_meeting.py` - Meeting orchestration
- `.env.example` - Environment configuration template

## Cost Estimate

Each meeting (~10 API calls) costs approximately:

- **gpt-4o-mini**: $0.10-0.20
- **gpt-4o**: $0.50-1.00

Set your OpenAI usage limits in the dashboard.
