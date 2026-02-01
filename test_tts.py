#!/usr/bin/env python3
"""
Test script to verify TTS integration without requiring OpenAI API key.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from tts import AgentVoice, create_voice_engine


def test_tts_module():
    """Test the TTS module functionality."""
    print("\n" + "=" * 60)
    print("TTS Module Integration Test")
    print("=" * 60 + "\n")

    # Test 1: Create voice engine with audio disabled
    print("Test 1: Creating voice engine (audio disabled)...")
    try:
        engine = create_voice_engine(enable_audio=False)
        print("✓ Voice engine created successfully")
    except Exception as e:
        print(f"✗ Failed to create voice engine: {e}")
        return False

    # Test 2: Check voice profiles
    print("\nTest 2: Checking voice profiles...")
    try:
        profiles = [
            ("ceo", "CEO (Sarah Chen)"),
            ("cfo", "CFO (Marcus Johnson)"),
            ("cto", "CTO (Priya Patel)"),
            ("coo", "COO (James Wilson)"),
            ("marketing", "VP Marketing (Elena Rodriguez)"),
        ]

        for agent_name, agent_title in profiles:
            props = engine.get_voice_properties(agent_name)
            print(f"  ✓ {agent_title}")
            print(f"    - Rate: {props['rate']} WPM")
            print(f"    - Pitch: {props['pitch']}")
            print(f"    - Volume: {props['volume']}")
    except Exception as e:
        print(f"✗ Failed to get voice properties: {e}")
        return False

    # Test 3: Test speak method (without audio)
    print("\nTest 3: Testing speak method (audio disabled)...")
    try:
        test_text = "Hello, this is a test message from the AI agent."
        engine.speak(test_text, "ceo", save_audio=False)
        print("✓ Speak method executed successfully")
    except Exception as e:
        print(f"✗ Failed to execute speak method: {e}")
        return False

    # Test 4: Test disable/enable
    print("\nTest 4: Testing enable/disable functionality...")
    try:
        engine.disable()
        print("✓ Audio disabled successfully")
        engine.enable()
        print("✓ Audio enabled successfully")
    except Exception as e:
        print(f"✗ Failed to enable/disable audio: {e}")
        return False

    # Test 5: Direct AgentVoice instantiation
    print("\nTest 5: Testing direct AgentVoice instantiation...")
    try:
        agent_voice = AgentVoice(enable_audio=False)
        print("✓ AgentVoice instantiated successfully")

        # Test speak_all method
        agent_voice.speak_all(
            "CEO", "Strategic decisions require careful analysis.", save_audio=False
        )
        print("✓ speak_all method executed successfully")
    except Exception as e:
        print(f"✗ Failed with AgentVoice: {e}")
        return False

    print("\n" + "=" * 60)
    print("✓ All TTS tests passed!")
    print("=" * 60 + "\n")

    print("TTS Features Available:")
    print("  • 5 agents with distinct voice profiles")
    print("  • Customizable rate, pitch, and volume per agent")
    print("  • Enable/disable audio functionality")
    print("  • Support for audio file saving")
    print("  • Cross-platform TTS support (Windows, macOS, Linux)")
    print("\nTo use TTS in meetings:")
    print("  python main.py --audio")
    print("  python examples.py 1 --audio\n")

    return True


if __name__ == "__main__":
    success = test_tts_module()
    sys.exit(0 if success else 1)
