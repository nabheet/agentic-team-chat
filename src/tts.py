"""Text-to-Speech functionality for agents using pyttsx3."""

import pyttsx3
from pathlib import Path


class AgentVoice:
    """Manages text-to-speech for each agent using pyttsx3 with different system voices."""

    def __init__(self, enable_audio: bool = True):
        """Initialize the TTS engine.

        Args:
            enable_audio: Whether to enable audio output
        """
        self.enable_audio = enable_audio
        self.engine = None
        self.audio_dir = Path("audio_output")
        self.available_voices = []

        if self.enable_audio:
            try:
                self.engine = pyttsx3.init()
                self.available_voices = self.engine.getProperty("voices")
                self.audio_dir.mkdir(exist_ok=True)
                print(
                    f"✓ pyttsx3 initialized with {len(self.available_voices)} available voices"
                )
            except Exception as e:
                print(f"Warning: Could not initialize TTS: {e}")
                self.enable_audio = False
                self.engine = None

    def get_voice_properties(self, agent_name: str) -> dict:
        """Get voice properties for an agent.

        Args:
            agent_name: Name of the agent (CEO, CFO, CTO, COO, VP Marketing)

        Returns:
            Dictionary with voice properties (voice_id, rate, volume)

        Note:
            Assigns different system voices to each agent for distinct voices.
            Falls back to rate/volume adjustments if not enough voices available.
        """
        # Assign different voice indices to each agent
        agent_indices = {
            "Sarah Chen": 0,  # CEO - first voice
            "Marcus Johnson": 1,  # CFO - second voice
            "Priya Patel": 2,  # CTO - third voice
            "James Wilson": 3,  # COO - fourth voice
            "Elena Rodriguez": 4,  # VP Marketing - fifth voice
        }

        agent_index = agent_indices.get(agent_name, 0)

        # Get the voice ID if available, otherwise use different rates
        if agent_index < len(self.available_voices):
            voice_id = self.available_voices[agent_index].id
        else:
            # Not enough voices, cycle through available ones
            voice_id = (
                self.available_voices[agent_index % len(self.available_voices)].id
                if self.available_voices
                else None
            )

        # Also vary rate and volume for additional differentiation
        rate_adjustments = {
            "Sarah Chen": 180,  # CEO - moderate pace
            "Marcus Johnson": 160,  # CFO - slower, thoughtful
            "Priya Patel": 200,  # CTO - faster, energetic
            "James Wilson": 170,  # COO - steady pace
            "Elena Rodriguez": 190,  # VP Marketing - dynamic
        }

        return {
            "voice_id": voice_id,
            "rate": rate_adjustments.get(agent_name, 175),
            "volume": 1.0,
        }

    def speak(self, text: str, agent_name: str, save_audio: bool = False) -> str:
        """Convert text to speech using pyttsx3.

        Args:
            text: The text to speak
            agent_name: Name of the agent speaking
            save_audio: Whether to save the audio to file

        Returns:
            Path to saved audio file (if saved) or empty string
        """
        if not self.enable_audio or not self.engine:
            return ""

        try:
            voice_props = self.get_voice_properties(agent_name)

            # Set voice properties
            if voice_props["voice_id"]:
                self.engine.setProperty("voice", voice_props["voice_id"])
            self.engine.setProperty("rate", voice_props["rate"])
            self.engine.setProperty("volume", voice_props["volume"])

            if save_audio:
                # Save to file
                filename = self.audio_dir / f"{agent_name.replace(' ', '_')}.wav"
                self.engine.save_to_file(text, str(filename))
                self.engine.runAndWait()
                return str(filename)
            else:
                # Speak directly
                self.engine.say(text)
                self.engine.runAndWait()
                return ""

        except Exception as e:
            print(f"Error in TTS for {agent_name}: {e}")
            return ""

    def speak_all(self, speaker_name: str, text: str, save_audio: bool = False):
        """Speak text with agent's voice and handle display.

        Args:
            speaker_name: Name of the speaker
            text: Text to speak
            save_audio: Whether to save audio files
        """
        if self.enable_audio and self.engine:
            audio_file = self.speak(text, speaker_name, save_audio=save_audio)
            return audio_file
        return ""

    def disable(self):
        """Disable audio output."""
        self.enable_audio = False

    def enable(self):
        """Enable audio output."""
        if not self.enable_audio:
            try:
                self.engine = pyttsx3.init()
                self.available_voices = self.engine.getProperty("voices")
                self.audio_dir.mkdir(exist_ok=True)
                self.enable_audio = True
            except Exception as e:
                print(f"Could not enable TTS: {e}")


def create_voice_engine(enable_audio: bool = False) -> AgentVoice:
    """Factory function to create a voice engine.

    Args:
        enable_audio: Whether to enable audio output

    Returns:
        AgentVoice instance
    """
    return AgentVoice(enable_audio=enable_audio)
