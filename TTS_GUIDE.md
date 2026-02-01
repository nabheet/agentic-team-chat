# Text-to-Speech (TTS) Feature Guide

This guide explains how to use the text-to-speech functionality in the Agentic Team Chat system.

## Overview

The TTS feature enables agents to **speak their statements** with distinct voices during meetings using **pyttsx3** and your system's built-in voice library. Each of the 5 corporate executives uses a different system voice with customized speech rate:

- **CEO (Sarah Chen)**: System voice #1 at 180 WPM - Executive presence
- **CFO (Marcus Johnson)**: System voice #2 at 160 WPM - Authoritative and thoughtful
- **CTO (Priya Patel)**: System voice #3 at 200 WPM - Energetic and dynamic
- **COO (James Wilson)**: System voice #4 at 170 WPM - Grounded and methodical
- **VP Marketing (Elena Rodriguez)**: System voice #5 at 190 WPM - Engaging and persuasive

## Installation

The TTS feature uses **pyttsx3**, a cross-platform text-to-speech library that uses your system's built-in voices. It's already added to `pyproject.toml`.

Install dependencies if you haven't already:

```bash
uv sync
```

### Platform-Specific Setup

**macOS**: No additional setup needed (uses NSSpeechSynthesizer)

**Windows**: No additional setup needed (uses SAPI5)

**Linux**: Install a TTS engine:

```bash
sudo apt-get install espeak
# or
sudo apt-get install festival
```

## Usage

### Running with Audio Output

#### Option 1: Main Meeting with Audio

```bash
python main.py --audio
```

This runs the default quarterly strategy meeting with all agents speaking.

#### Option 2: Example Scenarios with Audio

```bash
# Run scenario 2 (Innovation) with audio
python examples.py 2 --audio

# Interactive selection with audio
python examples.py --audio
```

Then select a scenario (1-6) when prompted.

#### Option 3: Programmatic Usage

```python
from src.team_meeting import TeamMeeting

# Create a meeting with audio enabled
meeting = TeamMeeting(enable_audio=True)

# Run the full meeting
meeting.run_full_meeting()
```

## Voice Profiles

Each agent uses a different system voice with customized speech rate. Configuration is in [src/tts.py](src/tts.py):

```python
# Assign different voice indices to each agent
agent_indices = {
    "Sarah Chen": 0,      # CEO - first system voice
    "Marcus Johnson": 1,  # CFO - second system voice
    "Priya Patel": 2,     # CTO - third system voice
    "James Wilson": 3,    # COO - fourth system voice
    "Elena Rodriguez": 4, # VP Marketing - fifth system voice
}

# Vary speech rate for additional differentiation
rate_adjustments = {
    "Sarah Chen": 180,      # CEO - moderate pace
    "Marcus Johnson": 160,  # CFO - slower, thoughtful
    "Priya Patel": 200,     # CTO - faster, energetic
    "James Wilson": 170,    # COO - steady pace
    "Elena Rodriguez": 190, # VP Marketing - dynamic
}
```

### Customizing Voice Properties

Edit [src/tts.py](src/tts.py) to adjust any agent's voice:

1. Find the `get_voice_properties()` method
2. Modify `agent_indices` to use different system voices
3. Adjust `rate_adjustments` to change speech speed (100-250 WPM recommended)
4. The system will automatically cycle through available voices if you have fewer than 5 voices

## Architecture

### TTS Module (`src/tts.py`)

The `AgentVoice` class handles text-to-speech using pyttsx3:

```python
class AgentVoice:
    def __init__(enable_audio: bool = True)
        """Initialize pyttsx3 engine and discover system voices"""
    
    def get_voice_properties(agent_name: str) -> dict
        """Get voice ID and rate for each agent"""
    
    def speak(text: str, agent_name: str, save_audio: bool = False)
        """Generate and play audio using assigned system voice"""
    
    def enable()
        """Enable audio output"""
    
    def disable()
        """Disable audio output"""
```

The system:

1. Discovers all available system voices on initialization
2. Assigns a unique voice to each of the 5 agents
3. Applies custom speech rate adjustments for additional differentiation

### Integration Points

1. **TeamMeeting**: Accepts `enable_audio` parameter
2. **print_speaker()**: Automatically calls `voice_engine.speak()` when audio is enabled
3. **CLI**: `--audio` flag in `main.py` and `examples.py`

## Troubleshooting

### Audio Not Playing

**Problem**: Script runs but no audio is heard.

**Solutions**:

1. Verify pyttsx3 is installed: `pip list | grep pyttsx3`
2. Check system volume is not muted
3. Try disabling and re-enabling audio:

   ```bash
   python main.py --audio  # May need to run twice on first use
   ```

### High CPU Usage

**Problem**: Script is using excessive CPU during TTS synthesis.

**Solutions**:

1. pyttsx3 uses system TTS engines which can be CPU-intensive
2. This is normal during synthesis - it will decrease once audio plays
3. Reduce speech rate if needed in `voice_profiles`

### Voice Not Found

**Problem**: Error about missing voices.

**Solutions**:

1. System may not have default TTS engine installed
2. On macOS: System TTS should be available by default
3. On Windows: Ensure Narrator is enabled
4. On Linux: Install `espeak` or `festival`

## Advanced Configuration

### Disable Audio for Specific Meetings

```python
from src.team_meeting import TeamMeeting

# Create meeting without audio (default)
meeting = TeamMeeting()  # enable_audio=False
meeting.run_full_meeting()
```

### Voice Engine Management

```python
from src.tts import create_voice_engine

# Create voice engine directly
voice_engine = create_voice_engine(enable_audio=True)

# Speak directly
voice_engine.speak("Hello world", agent_name="ceo")

# Disable audio
voice_engine.disable()
```

## Performance Notes

- **First Run**: Initial synthesis may take a few seconds as the system TTS engine initializes
- **Long Speeches**: Agent responses can be 100+ words; synthesis takes proportional time
- **System Resources**: TTS uses system resources; performance depends on OS and system load

## Supported Platforms

- ✅ **macOS**: Uses NSSpeechSynthesizer (184+ voices available by default)
- ✅ **Windows**: Uses SAPI5 TTS engine (multiple voices available)
- ✅ **Linux**: Uses espeak or festival (requires separate installation: `sudo apt-get install espeak`)

## File Structure

```bash
src/
├── tts.py              # Text-to-speech module (pyttsx3 implementation)
├── team_meeting.py     # Updated with audio support
├── agents.py           # Agent definitions
└── ...

main.py                # Updated with --audio flag
test_tts.py            # TTS testing script
```

## Example Output

When running with `--audio`:

```text
[CEO]
Thank you all for being here. We need to discuss our Q1 strategy...
*Agent speaks with measured, executive tone*

[CFO]
From a financial perspective, we need to focus on...
*Agent speaks with authoritative tone*
```

## Future Enhancements

Potential improvements to the TTS system:

1. **Audio File Saving**: Save meeting audio as MP3 files
2. **Voice Selection**: Allow choosing from multiple available voices
3. **Pronunciation Dictionary**: Define custom pronunciations
4. **Meeting Transcript with Audio**: Generate timestamped transcripts with audio links
5. **Real-time Audio Streaming**: Stream audio during synthesis
6. **Voice Cloning**: Use custom voice samples (requires advanced TTS library)

## Support

For issues or questions:

1. Check the troubleshooting section above
2. Review pyttsx3 documentation: <https://pyttsx3.readthedocs.io/>
3. Ensure all dependencies are properly installed
4. Verify `OPENAI_API_KEY` environment variable is set

---

**Status**: ✅ Text-to-speech fully integrated and ready to use!
