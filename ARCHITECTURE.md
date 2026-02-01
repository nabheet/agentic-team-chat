# System Architecture

## Overview

The Agentic Team Chat system is built on LangChain's multi-agent framework, allowing multiple AI agents to simulate a corporate team discussing strategy and making decisions.

## Core Components

### 1. Agent System (`src/agents.py`)

#### `CorporateAgent` Base Class

The foundation for all agent types. Features:

- **Attributes**:
  - `name`: Agent's full name
  - `role`: Job title
  - `expertise`: List of subject matter specialties
  - `personality`: Decision-making style and values
  - `llm`: LangChain ChatOpenAI instance
  - `conversation_history`: Maintains discussion context

- **Methods**:
  - `get_system_prompt()`: Generates context-aware system prompt
  - `think()`: Generate independent thoughts on a topic
  - `respond_to_colleague()`: Respond to other agents' statements

#### Specialized Agent Classes

```
CorporateAgent (Base)
├── CEO (Sarah Chen)
├── CFO (Marcus Johnson)
├── CTO (Priya Patel)
├── COO (James Wilson)
└── VPMarketing (Elena Rodriguez)
```

Each subclass initializes with specific expertise and personality traits.

### 2. Meeting Orchestration (`src/team_meeting.py`)

#### `TeamMeeting` Class

Manages multi-agent discussions with:

- **Agent Management**: Dictionary of agents indexed by role
- **Discussion Methods**:
  - `discuss_topic()`: Primary agent opens, others respond
  - `facilitate_debate()`: Structured 3-round debate
  - `round_table_discussion()`: All agents contribute
  
- **Output Formatting**:
  - Color-coded console output per agent
  - Meeting transcript collection
  - File-based transcript saving

#### Meeting Flow

```
1. Open Meeting (CEO opens)
   ↓
2. Topic Discussion 1 → Primary agent + responses
   ↓
3. Structured Debate → Two agents debate in rounds
   ↓
4. Round Table → All agents contribute sequentially
   ↓
5. Topic Discussion 2-N → Various topics
   ↓
6. Close Meeting (CEO closes)
   ↓
7. Save Transcript
```

### 3. LLM Integration

Each agent has its own `ChatOpenAI` instance:

```python
llm = ChatOpenAI(
    model_name="gpt-4o-mini",  # Model selection
    temperature=0.7             # Creativity level
)
```

**API Calls Flow**:

```
User Request
    ↓
TeamMeeting.discuss_topic()
    ↓
Agent.think() → Creates messages → LLM.invoke()
    ↓
OpenAI API (gpt-4o-mini)
    ↓
Response → Formatted → Console + Transcript
```

## Data Flow

### Single Agent Response

```
Input: topic, context
    ↓
get_system_prompt() → Creates specialized prompt
    ↓
Messages: [SystemMessage(prompt), HumanMessage(topic)]
    ↓
llm.invoke(messages)
    ↓
Response Content
    ↓
Output: Formatted text
```

### Multi-Agent Discussion

```
1. Primary Agent (think on topic)
    ↓ Response
2. Secondary Agent 1 (respond_to_colleague)
    ↓ Response
3. Secondary Agent 2 (respond_to_colleague)
    ↓ Response
4. Secondary Agent 3 (respond_to_colleague)
    ↓ Response
→ Formatted output to console + transcript
```

### Debate Structure

```
Side 1: Opens position
    ↓ Position 1 Response
Side 2: Responds
    ↓ Position 2 Response
Side 1: Rebuttal
    ↓ Rebuttal Response
→ Display all three exchanges
```

## Message Format

LangChain messages follow this structure:

```python
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are an expert..."),  # Agent context
    HumanMessage(content="Topic: ...")              # User input
]

response = llm.invoke(messages)
print(response.content)  # Extract text response
```

## System Prompt Design

Each agent receives a specialized system prompt:

```
You are [NAME], the [ROLE] at TechVenture Corp.

Your expertise: [EXPERTISE LIST]
Your personality: [PERSONALITY TRAITS]

You are participating in a corporate strategy meeting. Provide thoughtful, 
data-driven insights from your perspective...
```

This ensures responses are:

- Role-appropriate
- Expertise-aligned
- Personality-consistent
- Meeting-context-aware

## Extensibility

### Adding New Agent Types

```python
class CHRO(CorporateAgent):
    def __init__(self):
        super().__init__(
            name="...",
            role="Chief Human Resources Officer",
            expertise=[...],
            personality="..."
        )
```

### Adding New Discussion Types

```python
class TeamMeeting:
    def panel_discussion(self, topic: str, participants: list[str]):
        # Implementation for panel format
        pass
    
    def ranked_voting(self, question: str):
        # Implementation for voting on options
        pass
```

### Custom Meeting Scenarios

```python
class StrategyRetreat(TeamMeeting):
    def run_retreat(self):
        self.open_meeting()
        self.round_table_discussion("Topic 1")
        self.facilitate_debate("Topic 2", side1="cto", side2="cfo")
        self.closing_remarks()
```

## Performance Characteristics

### API Calls per Meeting

Standard meeting = ~10 API calls:

- 1 CEO opening
- 5 discussion topics (1 primary + 4 responses) = 5 calls
- 1 debate with 3 rounds = 3 calls
- 1 CEO closing

### Latency

- Single response: 2-5 seconds
- Full meeting: 30-60 seconds (depending on network)

### Cost

- gpt-4o-mini: ~$0.10-0.20 per meeting
- gpt-4o: ~$0.50-1.00 per meeting

## Configuration Options

### Model Selection

```python
# Fast and cheap
ChatOpenAI(model_name="gpt-4o-mini")

# Higher quality, more expensive
ChatOpenAI(model_name="gpt-4o")

# Older but reliable
ChatOpenAI(model_name="gpt-3.5-turbo")
```

### Temperature Settings

```python
# Logical, consistent responses
ChatOpenAI(temperature=0.3)

# Balanced
ChatOpenAI(temperature=0.7)

# Creative, diverse responses
ChatOpenAI(temperature=1.0)
```

## Error Handling

### API Errors

LangChain automatically handles:

- Rate limiting (with exponential backoff)
- Timeout errors
- Invalid API keys

### Custom Error Handling

```python
try:
    meeting.run_full_meeting()
except Exception as e:
    print(f"Meeting error: {e}")
    # Fallback logic
```

## Future Architecture Enhancements

### Planned Features

1. **Agent Memory**
   - Persistent conversation context
   - Learning across meetings
   - Historical context injection

2. **Decision Making**
   - Consensus algorithms
   - Voting mechanisms
   - Risk scoring

3. **Advanced Interactions**
   - Async parallel agent responses
   - Dynamic team composition
   - Real-time sentiment analysis

4. **Integration Points**
   - Database persistence
   - Real business data feeds
   - External API consumption

5. **Scalability**
   - Support for 10+ agents
   - Distributed agent processing
   - Streaming responses

## Security Considerations

- **API Key Management**: Use environment variables, never hardcode
- **Data Privacy**: Meeting transcripts may contain sensitive data
- **Rate Limiting**: Monitor API usage to prevent abuse
- **Agent Constraints**: System prompts prevent harmful outputs

## Testing Strategy

```python
# Unit tests for agent responses
def test_agent_expertise():
    cto = CTO()
    assert "AI/ML" in cto.get_system_prompt()

# Integration tests for meetings
def test_meeting_transcript():
    meeting = TeamMeeting()
    meeting.run_full_meeting()
    assert len(meeting.meeting_transcript) > 0

# Mock LLM for testing
from unittest.mock import patch
with patch("ChatOpenAI.invoke") as mock:
    mock.return_value.content = "Test response"
```

## Deployment Considerations

- **Serverless**: Can run on Lambda/Cloud Functions
- **Long-running**: Consider background jobs for multi-hour meetings
- **Monitoring**: Track API usage, response quality, costs
- **Scaling**: Each meeting can run independently in parallel
