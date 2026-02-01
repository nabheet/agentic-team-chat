# Quick Start - Text-to-Speech Feature

## 🎙️ Enable Agent Voices

The easiest way to use text-to-speech is with the `--audio` flag:

### Option 1: Run Default Meeting with Audio

```bash
python main.py --audio
```

This runs the default quarterly strategy meeting where all 5 agents speak their statements.

### Option 2: Run Example Scenario with Audio

```bash
python examples.py 1 --audio
```

Run any scenario (1-6) with audio. Replace `1` with the scenario number you want.

### Option 3: Interactive Mode with Audio

```bash
python examples.py --audio
```

Prompts you to select a scenario, then runs it with audio enabled.

## 🎤 Agent Voices

Each executive uses a different system voice:

- **CEO (Sarah Chen)**: System voice #1, 180 WPM - Professional, measured tone
- **CFO (Marcus Johnson)**: System voice #2, 160 WPM - Authoritative, thoughtful
- **CTO (Priya Patel)**: System voice #3, 200 WPM - Energetic, dynamic
- **COO (James Wilson)**: System voice #4, 170 WPM - Grounded, methodical
- **VP Marketing (Elena Rodriguez)**: System voice #5, 190 WPM - Engaging, persuasive

On macOS, you have 184+ system voices available!

## ⚙️ Configuration

To customize voice settings, edit `src/tts.py`:

```python
# Change which system voice each agent uses
agent_indices = {
    "Sarah Chen": 0,      # Try different indices (0-183 on macOS)
    "Marcus Johnson": 1,  # Each index is a different voice
    # ...
}

# Adjust speech rate for each agent
rate_adjustments = {
    "Sarah Chen": 180,      # Words per minute (100-250 recommended)
    "Marcus Johnson": 160,  # Slower = more thoughtful
    # ...
}
```

## 🧪 Test TTS Installation

```bash
python test_tts.py
```

This verifies that pyttsx3 is properly installed and all voice profiles are working.

## 🐛 Troubleshooting

**No audio output?**

- Ensure system volume is not muted
- Verify pyttsx3 is installed: `pip list | grep pyttsx3`
- Run `python test_tts.py` to check installation

**High CPU usage?**

- Normal during audio synthesis
- CPU usage decreases after audio plays

**Linux users:**

- Install espeak: `sudo apt-get install espeak`
- Or festival: `sudo apt-get install festival`

## 📚 Learn More

See [TTS_GUIDE.md](TTS_GUIDE.md) for comprehensive documentation.

---

That's it! Start with `python main.py --audio` to hear your AI team in action.
