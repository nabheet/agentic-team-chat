# Advanced Usage & Customization

## Creating Custom Agents

### Basic Custom Agent

```python
from src.agents import CorporateAgent

class CHRO(CorporateAgent):
    """Chief Human Resources Officer"""
    def __init__(self):
        super().__init__(
            name="Patricia Chen",
            role="Chief Human Resources Officer",
            expertise=[
                "Talent Acquisition",
                "Organizational Development",
                "Compensation Strategy",
                "Company Culture"
            ],
            personality="People-focused, strategic about talent, concerned with retention and engagement. "
                        "Advocates for employee well-being while ensuring organizational effectiveness."
        )
```

### Using Utility Functions

```python
from utils import create_custom_agent

agent = create_custom_agent(
    name="Chief Sustainability Officer",
    role="CSO",
    expertise=["ESG Strategy", "Carbon Footprint", "Sustainable Supply Chain"],
    personality="Forward-thinking, mission-driven, committed to environmental and social responsibility."
)
```

## Custom Meeting Scenarios

### Extending TeamMeeting

```python
from src.team_meeting import TeamMeeting
from src.agents import CEO, CFO, CTO

class InvestorMeeting(TeamMeeting):
    def __init__(self):
        super().__init__()
        # Customize agent selection
        self.agents = {
            "ceo": CEO(),
            "cfo": CFO(),
            "cto": CTO(),
            # Could add investor agent here
        }
    
    def run_pitch(self):
        """Run an investor pitch meeting"""
        self.print_header("INVESTOR PITCH MEETING")
        
        self.open_meeting()
        
        # Business overview
        self.discuss_topic(
            "Provide an overview of TechVenture's market position and growth potential",
            primary_speaker="ceo"
        )
        
        # Financial performance debate
        self.facilitate_debate(
            "Revenue growth vs. profitability trajectory over next 3 years",
            side1="ceo",
            side2="cfo"
        )
        
        # Technology roadmap
        self.discuss_topic(
            "What's our product roadmap and competitive differentiation?",
            primary_speaker="cto"
        )
        
        self.closing_remarks()
        self.save_transcript("investor_pitch.txt")
```

### Running Custom Meetings

```python
meeting = InvestorMeeting()
meeting.run_pitch()
```

## Advanced Response Techniques

### Getting Specific Opinions

```python
from src.agents import CEO, CTO

cto = CTO()
opinion = cto.think(
    "What's your view on building our own AI infrastructure vs using cloud providers like Bedrock?"
)
print(opinion)
```

### Debate Between Specific Agents

```python
from src.team_meeting import TeamMeeting

meeting = TeamMeeting()

ceo = meeting.agents["ceo"]
cfo = meeting.agents["cfo"]

# CEO's position
position1 = ceo.think("Why we should invest heavily in R&D")

# CFO's counter
position2 = cfo.respond_to_colleague(
    ceo.name, 
    position1,
    "R&D Investment Strategy"
)

# CEO's rebuttal
rebuttal = ceo.respond_to_colleague(
    cfo.name,
    position2, 
    "R&D Investment Strategy"
)

print(position1)
print(position2)
print(rebuttal)
```

## Modifying Agent Behavior

### System Prompt Customization

```python
class AggressiveCTO(CorporateAgent):
    def __init__(self):
        super().__init__(
            name="Tech Leader",
            role="Chief Technology Officer",
            expertise=["AI/ML", "Cloud", "Architecture"],
            personality="Aggressive, pushes boundaries, skeptical of corporate constraints."
        )
    
    def get_system_prompt(self) -> str:
        """Override to add custom behavior"""
        base_prompt = super().get_system_prompt()
        addition = "\n\nBe especially critical of legacy systems and push for modernization."
        return base_prompt + addition
```

### Temperature Tuning

Modify agent creativity levels:

```python
agent.llm.temperature = 0.3  # More logical
agent.llm.temperature = 0.9  # More creative
```

## Real-world Scenarios

### Scenario 1: Product Launch Review

```python
from src.team_meeting import TeamMeeting

class ProductLaunchReview(TeamMeeting):
    def run_review(self):
        self.open_meeting()
        self.print_header("PRODUCT LAUNCH REVIEW")
        
        # Market positioning
        self.round_table_discussion(
            "What are the key features and market positioning for our new AI product?"
        )
        
        # Go-to-market strategy
        self.discuss_topic(
            "What's our pricing strategy and target customer segments?",
            primary_speaker="marketing"
        )
        
        # Resource allocation
        self.facilitate_debate(
            "Should we launch in one market or multiple markets simultaneously?",
            side1="marketing",
            side2="coo"
        )
        
        # Financial projections
        self.discuss_topic(
            "What are revenue and cost projections for year 1?",
            primary_speaker="cfo"
        )
        
        self.closing_remarks()
        self.save_transcript("product_launch_review.txt")

meeting = ProductLaunchReview()
meeting.run_review()
```

### Scenario 2: Crisis Management

```python
class CrisisResponse(TeamMeeting):
    def respond_to_crisis(self, crisis_type: str):
        self.print_header(f"CRISIS RESPONSE: {crisis_type}")
        
        # CEO opens
        ceo = self.agents["ceo"]
        response = ceo.think(
            f"We're facing a critical {crisis_type} crisis. What are immediate actions?"
        )
        self.print_speaker("ceo", ceo.role, response)
        
        # All hands on deck
        self.round_table_discussion(
            "What's each department's action plan for the first 24 hours?"
        )
        
        # Communication strategy
        self.discuss_topic(
            "How do we communicate with stakeholders?",
            primary_speaker="marketing"
        )
        
        self.save_transcript(f"crisis_{crisis_type.lower().replace(' ', '_')}.txt")

meeting = CrisisResponse()
meeting.respond_to_crisis("Security Breach")
```

### Scenario 3: Multi-Department Coordination

```python
class StrategicInitiative(TeamMeeting):
    def plan_initiative(self, initiative: str):
        self.open_meeting()
        self.print_header(f"STRATEGIC INITIATIVE: {initiative}")
        
        # CEO vision
        self.discuss_topic(
            f"Vision and strategic importance of: {initiative}",
            primary_speaker="ceo"
        )
        
        # Technical feasibility
        self.discuss_topic(
            "Technical requirements and architecture",
            primary_speaker="cto"
        )
        
        # Operational plan
        self.discuss_topic(
            "Timeline, resources, and execution plan",
            primary_speaker="coo"
        )
        
        # Financial impact
        self.discuss_topic(
            "Investment required, ROI, and financial projections",
            primary_speaker="cfo"
        )
        
        # Market implications
        self.discuss_topic(
            "Market impact, competitive response, customer implications",
            primary_speaker="marketing"
        )
        
        # Final debate on priorities
        self.facilitate_debate(
            f"Speed to market vs. quality and risk mitigation for {initiative}",
            side1="ceo",
            side2="cfo"
        )
        
        self.closing_remarks()
        self.save_transcript(f"initiative_{initiative.lower().replace(' ', '_')}.txt")

meeting = StrategicInitiative()
meeting.plan_initiative("AI Integration across all products")
```

## Advanced Features

### Conversation History

Each agent maintains conversation history:

```python
agent = meeting.agents["ceo"]
print(f"Conversation history length: {len(agent.conversation_history)}")

# Clear history for new topic
agent.conversation_history = []
```

### Custom Output Formatting

```python
class FormattedMeeting(TeamMeeting):
    def print_speaker(self, agent_name: str, role: str, content: str):
        # Custom formatting
        separator = "─" * 60
        print(f"\n{separator}")
        print(f"SPEAKER: {role}")
        print(f"─" * 60)
        print(f"\n{content}\n")

meeting = FormattedMeeting()
# Use as normal - will have custom formatting
```

### Saving Custom Outputs

```python
import json
from datetime import datetime

class AnalyticsMeeting(TeamMeeting):
    def save_analysis(self):
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "agents": list(self.agents.keys()),
            "transcript_length": len(self.meeting_transcript),
            "topics_discussed": 5,
            "transcript": "\n".join(self.meeting_transcript)
        }
        
        with open("meeting_analysis.json", "w") as f:
            json.dump(analysis, f, indent=2)
```

## Performance Optimization

### Parallel Agent Responses

```python
import concurrent.futures

def get_parallel_responses(meeting, topic):
    """Get all agent responses in parallel"""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {}
        for key, agent in meeting.agents.items():
            future = executor.submit(agent.think, topic)
            futures[key] = future
        
        results = {}
        for key, future in futures.items():
            results[key] = future.result()
        
        return results

meeting = TeamMeeting()
responses = get_parallel_responses(meeting, "What's our top priority?")
for agent, response in responses.items():
    print(f"{agent}: {response}")
```

### Batch Processing

```python
def run_multiple_meetings(scenarios: list[dict]):
    """Run multiple meetings efficiently"""
    results = []
    for scenario in scenarios:
        meeting = TeamMeeting()
        meeting.run_full_meeting()
        results.append({
            "name": scenario["name"],
            "transcript": meeting.meeting_transcript
        })
    return results

scenarios = [
    {"name": "Q1 Planning"},
    {"name": "Q2 Review"},
    {"name": "Q3 Planning"},
]

all_results = run_multiple_meetings(scenarios)
```

## Troubleshooting Advanced Features

### Agent Not Responding

```python
# Check if LLM is initialized
agent = meeting.agents["ceo"]
assert agent.llm is not None, "LLM not initialized"

# Verify API key
import os
assert os.getenv("OPENAI_API_KEY"), "API key not set"
```

### Slow Responses

- Reduce number of agents
- Reduce temperature (less creative = faster)
- Use lighter model (gpt-3.5-turbo vs gpt-4o)
- Run agents in parallel

### Memory Issues

```python
# Clear old transcripts
meeting.meeting_transcript = []

# Reset agent history
for agent in meeting.agents.values():
    agent.conversation_history = []
```

## Integration Examples

### With Flask Web App

```python
from flask import Flask, jsonify
from src.team_meeting import TeamMeeting

app = Flask(__name__)

@app.route("/api/meeting", methods=["POST"])
def run_meeting():
    meeting = TeamMeeting()
    meeting.run_full_meeting()
    return jsonify({"transcript": meeting.meeting_transcript})
```

### With Streamlit Dashboard

```python
import streamlit as st
from src.team_meeting import TeamMeeting

st.title("Corporate Strategy Meetings")

if st.button("Run Meeting"):
    meeting = TeamMeeting()
    meeting.run_full_meeting()
    st.text_area("Transcript", "\n".join(meeting.meeting_transcript))
```

### With Database

```python
from datetime import datetime
import sqlite3

def save_meeting_to_db(meeting):
    conn = sqlite3.connect("meetings.db")
    c = conn.cursor()
    
    c.execute("""INSERT INTO meetings 
                 (timestamp, agents, transcript_length, transcript)
                 VALUES (?, ?, ?, ?)""",
              (datetime.now(), str(list(meeting.agents.keys())),
               len(meeting.meeting_transcript),
               "\n".join(meeting.meeting_transcript)))
    
    conn.commit()
    conn.close()
```
