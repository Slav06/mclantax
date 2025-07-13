#!/usr/bin/env python3
"""
McLan Tax Baby Video Creator
A CrewAI-powered system for creating viral baby tax videos
"""

import argparse
import sys
import os
from datetime import datetime
from crew import BabyTaxVideoCrew
from config import Config

def check_configuration():
    """Check if all required API keys are configured."""
    required_keys = [
        ("OPENAI_API_KEY", Config.OPENAI_API_KEY),
        ("HELDRA_API_KEY", Config.HELDRA_API_KEY),
        ("SERPAPI_API_KEY", Config.SERPAPI_API_KEY)
    ]
    
    missing_keys = []
    for key_name, key_value in required_keys:
        if key_value == f"your_{key_name.lower()}_here":
            missing_keys.append(key_name)
    
    if missing_keys:
        print("⚠️  Missing API Keys:")
        for key in missing_keys:
            print(f"   - {key}")
        print("\n📝 Please update your environment variables or config.py file")
        print("🔧 The system will use mock data for demonstration purposes")
        return False
    
    return True

def setup_environment():
    """Set up the environment for the application."""
    # Create output directories
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    print("🍼 McLan Tax Baby Video Creator")
    print("=" * 50)
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🏢 Brand: {Config.BRAND_NAME} ({Config.BRAND_HANDLE})")
    print(f"📱 Platforms: {', '.join(Config.PLATFORMS)}")
    print(f"📊 Daily Posts: {Config.POSTS_PER_DAY}")
    print("")
    
    config_status = check_configuration()
    if config_status:
        print("✅ Configuration: All API keys configured")
    else:
        print("🔄 Configuration: Running in demo mode")
    
    print("")

def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description="Create viral baby tax videos using CrewAI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Create one video
  python main.py --batch 5          # Create 5 videos
  python main.py --demo             # Show demo workflow
  python main.py --config           # Show configuration
        """
    )
    
    parser.add_argument(
        "--batch", 
        type=int, 
        metavar="N",
        help="Create N videos in batch mode"
    )
    
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run in demo mode (no actual API calls)"
    )
    
    parser.add_argument(
        "--config",
        action="store_true",
        help="Show current configuration"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Setup environment
    setup_environment()
    
    # Handle configuration display
    if args.config:
        print("📋 Current Configuration:")
        print(f"   Brand Name: {Config.BRAND_NAME}")
        print(f"   Brand Handle: {Config.BRAND_HANDLE}")
        print(f"   Posts Per Day: {Config.POSTS_PER_DAY}")
        print(f"   Video Duration: {Config.VIDEO_DURATION_MIN}-{Config.VIDEO_DURATION_MAX} seconds")
        print(f"   Platforms: {', '.join(Config.PLATFORMS)}")
        print(f"   Content Topics: {', '.join(Config.CONTENT_TOPICS)}")
        return
    
    # Initialize the crew
    try:
        baby_crew = BabyTaxVideoCrew()
        
        # Run batch creation
        if args.batch:
            print(f"🎬 Starting batch creation: {args.batch} videos")
            results = baby_crew.run_batch_content_creation(args.batch)
            print(f"✅ Batch completed: {len(results)} videos processed")
            
        # Run demo mode
        elif args.demo:
            print("🎭 Demo Mode: Showing workflow without API calls")
            print("📖 This demonstrates the full process flow:")
            print("   1. Trend Research → 2. Script Writing → 3. Video Generation")
            print("   4. Caption Addition → 5. Copy Writing → 6. Social Media Posting")
            print("")
            result = baby_crew.run_daily_content_creation()
            
        # Run single video creation
        else:
            print("🎥 Creating single video...")
            result = baby_crew.run_daily_content_creation()
            
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 