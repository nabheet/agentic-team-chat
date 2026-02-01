#!/usr/bin/env python3
"""
Main entry point for the Agentic Team Chat system.

This script demonstrates a corporate strategy meeting where multiple AI agents
representing different C-suite executives discuss business strategy and make decisions.
"""

import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from team_meeting import TeamMeeting
from colorama import Fore, Style


def check_openai_key():
    """Check if OpenAI API key is configured."""
    if not os.getenv("OPENAI_API_KEY"):
        print(
            f"{Fore.RED}Error: OPENAI_API_KEY environment variable is not set.{Style.RESET_ALL}"
        )
        print(f"\n{Fore.YELLOW}To use this application, you need to:")
        print("1. Get your OpenAI API key from https://platform.openai.com/api-keys")
        print("2. Create a .env file in the project root with:")
        print("   OPENAI_API_KEY=your_api_key_here")
        print("\n3. Or set the environment variable directly:")
        print("   export OPENAI_API_KEY=your_api_key_here")
        print(f"{Style.RESET_ALL}\n")
        return False
    return True


def main():
    """Main function to run the corporate strategy meeting."""
    parser = argparse.ArgumentParser(
        description="Run the Agentic Team Chat corporate strategy meeting."
    )
    parser.add_argument(
        "--audio",
        action="store_true",
        help="Enable text-to-speech output with agent-specific voices",
    )
    args = parser.parse_args()

    print(f"{Fore.CYAN}{'=' * 80}{Style.RESET_ALL}")
    print(
        f"{Fore.CYAN}{'Agentic Team Chat - Corporate Strategy Meeting'.center(80)}{Style.RESET_ALL}"
    )
    print(f"{Fore.CYAN}{'=' * 80}{Style.RESET_ALL}\n")

    if not check_openai_key():
        sys.exit(1)

    print(
        f"{Fore.GREEN}OpenAI API key found. Initializing team meeting...{Style.RESET_ALL}\n"
    )

    if args.audio:
        print(
            f"{Fore.CYAN}Audio output enabled. Agents will speak their statements.{Style.RESET_ALL}\n"
        )

    try:
        meeting = TeamMeeting(enable_audio=args.audio)
        meeting.run_full_meeting()
        print(f"\n{Fore.GREEN}Meeting completed successfully!{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}Error during meeting: {str(e)}{Style.RESET_ALL}")
        print(
            f"{Fore.YELLOW}Make sure your OpenAI API key is valid and you have sufficient credits.{Style.RESET_ALL}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
