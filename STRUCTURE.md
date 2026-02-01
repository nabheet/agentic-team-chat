# Complete Project Directory Structure

```
agentic-team-chat/
│
├── 📄 main.py                    # DEFAULT ENTRY POINT
│   └── Runs standard corporate strategy meeting
│
├── 📄 examples.py                # EXAMPLE SCENARIOS
│   ├── Scenario 1: Standard quarterly meeting
│   ├── Scenario 2: Innovation & digital transformation
│   ├── Scenario 3: Market expansion strategy
│   ├── Scenario 4: Cost optimization
│   ├── Scenario 5: Crisis response
│   └── Scenario 6: Growth vs profitability debate
│
├── 📄 utils.py                   # UTILITY FUNCTIONS
│   ├── create_custom_agent()
│   ├── create_tech_startup_team()
│   ├── create_consulting_firm_team()
│   └── create_healthcare_organization_team()
│
├── 📂 src/                       # SOURCE CODE DIRECTORY
│   ├── __init__.py               # Package initialization
│   │
│   ├── agents.py                 # AGENT DEFINITIONS
│   │   ├── CorporateAgent (base class)
│   │   ├── CEO (Sarah Chen)
│   │   ├── CFO (Marcus Johnson)
│   │   ├── CTO (Priya Patel)
│   │   ├── COO (James Wilson)
│   │   └── VPMarketing (Elena Rodriguez)
│   │
│   └── team_meeting.py           # MEETING ORCHESTRATION
│       ├── TeamMeeting class
│       ├── open_meeting()
│       ├── discuss_topic()
│       ├── facilitate_debate()
│       ├── round_table_discussion()
│       ├── closing_remarks()
│       └── save_transcript()
│
├── 📚 DOCUMENTATION FILES
│   ├── README.md                 # COMPLETE DOCUMENTATION
│   │   ├── System overview
│   │   ├── Team member descriptions
│   │   ├── Features and architecture
│   │   ├── Installation & setup
│   │   ├── Usage examples
│   │   ├── Project structure
│   │   ├── Configuration options
│   │   └── Troubleshooting guide
│   │
│   ├── QUICKSTART.md             # 5-MINUTE SETUP GUIDE
│   │   ├── Get OpenAI API key
│   │   ├── Configure environment
│   │   ├── Run first meeting
│   │   ├── Example scenarios
│   │   ├── Customization quick tips
│   │   └── Troubleshooting
│   │
│   ├── SUMMARY.md                # PROJECT OVERVIEW
│   │   ├── What you built
│   │   ├── Quick start (3 steps)
│   │   ├── Key features
│   │   ├── Common use cases
│   │   ├── Example output
│   │   └── Next steps
│   │
│   ├── ARCHITECTURE.md           # TECHNICAL DEEP DIVE
│   │   ├── System overview
│   │   ├── Core components breakdown
│   │   ├── Agent system architecture
│   │   ├── Meeting orchestration flow
│   │   ├── LLM integration
│   │   ├── Data flow diagrams
│   │   ├── Message format specifications
│   │   ├── System prompt design
│   │   ├── Extensibility patterns
│   │   ├── Performance characteristics
│   │   ├── Configuration options
│   │   ├── Error handling
│   │   ├── Security considerations
│   │   └── Testing strategy
│   │
│   └── ADVANCED.md               # ADVANCED CUSTOMIZATION
│       ├── Creating custom agents
│       ├── Custom meeting scenarios
│       ├── Advanced response techniques
│       ├── Real-world scenario examples
│       ├── Performance optimization
│       ├── Integration examples
│       ├── Troubleshooting advanced features
│       └── Parallel processing patterns
│
├── 📋 CONFIGURATION FILES
│   ├── .env.example              # ENVIRONMENT TEMPLATE
│   │   └── OPENAI_API_KEY configuration
│   │
│   ├── .env                      # YOUR LOCAL ENVIRONMENT (create this)
│   │   └── Add your actual API key here
│   │
│   ├── pyproject.toml            # PROJECT CONFIGURATION
│   │   ├── Project metadata
│   │   ├── Dependencies
│   │   │   ├── langchain
│   │   │   ├── langchain-openai
│   │   │   ├── python-dotenv
│   │   │   ├── pydantic
│   │   │   ├── colorama
│   │   │   └── requests
│   │   └── Development dependencies
│   │
│   ├── uv.lock                   # LOCKED DEPENDENCIES
│   │   └── Exact version pinning for reproducibility
│   │
│   └── .python-version           # PYTHON VERSION PINNING
│       └── Python 3.10+
│
├── 📁 .venv/                     # VIRTUAL ENVIRONMENT (auto-created)
│   └── Isolated Python environment with all packages
│
└── 📁 .git/                      # GIT REPOSITORY
    └── Version control history
```

## File Purposes Summary

### Entry Points

- **main.py**: Start here - runs standard corporate meeting
- **examples.py**: Run specific scenarios (use with arguments 1-6)

### Source Code

- **src/agents.py**: AI agent definitions with personalities and expertise
- **src/team_meeting.py**: Meeting orchestration and discussion management

### Utilities

- **utils.py**: Helper functions for creating custom agents and teams

### Documentation (Read in Order)

1. **SUMMARY.md**: Project overview (start here)
2. **QUICKSTART.md**: Get running in 5 minutes
3. **README.md**: Complete feature documentation
4. **ARCHITECTURE.md**: Technical system design
5. **ADVANCED.md**: Advanced customization examples

### Configuration

- **.env.example**: Template for environment variables
- **.env**: Your local configuration (add API key here)
- **pyproject.toml**: Project and dependency configuration

## Quick Reference

### Running the System

```bash
# Standard meeting
python main.py

# With specific scenario
python examples.py 1      # Quarterly meeting
python examples.py 2      # Innovation focus
python examples.py 3      # Market expansion
python examples.py 4      # Cost optimization
python examples.py 5      # Crisis response
python examples.py 6      # Debate scenario
```

### Key Classes

```
CorporateAgent (base)
├── CEO
├── CFO
├── CTO
├── COO
└── VPMarketing

TeamMeeting
├── open_meeting()
├── discuss_topic()
├── facilitate_debate()
├── round_table_discussion()
├── closing_remarks()
└── save_transcript()
```

### Core Functions

**Agents**: `think()`, `respond_to_colleague()`, `get_system_prompt()`
**Meetings**: `open_meeting()`, `discuss_topic()`, `facilitate_debate()`, `round_table_discussion()`, `closing_remarks()`, `save_transcript()`

## Data Flow

```
User Request
    ↓
TeamMeeting.discuss_topic()
    ↓
Agent.think() or Agent.respond_to_colleague()
    ↓
Create LangChain Messages
    ↓
LLM.invoke() → OpenAI API
    ↓
Format Response
    ↓
Print to Console + Add to Transcript
    ↓
Save Transcript to File
```

## Environment Setup

```bash
# Copy template
cp .env.example .env

# Edit .env
OPENAI_API_KEY=sk-... (your actual key)

# Dependencies installed via
pip install -e .
# or
uv sync
```

## System Requirements

- Python 3.10+
- OpenAI API key
- Internet connection
- ~50MB disk space (including dependencies)

## Dependencies

| Package | Purpose |
|---------|---------|
| langchain | Multi-agent framework |
| langchain-openai | OpenAI integration |
| python-dotenv | Environment variables |
| pydantic | Data validation |
| colorama | Console colors |

## Next Steps After Setup

1. ✅ Create `.env` with your API key
2. ✅ Run `python main.py`
3. ✅ Try `python examples.py 2` for innovation scenario
4. ✅ Read ADVANCED.md for customization
5. ✅ Create your own custom agents
6. ✅ Build specialized meeting scenarios
7. ✅ Integrate with your applications

## File Size Reference

- `src/agents.py`: ~3KB (agent definitions)
- `src/team_meeting.py`: ~6KB (meeting orchestration)
- `utils.py`: ~2KB (helper functions)
- `main.py`: ~1KB (entry point)
- `examples.py`: ~7KB (scenario examples)
- `pyproject.toml`: <1KB (configuration)
- `Total code`: ~20KB (very lean)

---

**Enjoy your agentic AI system!** 🚀
