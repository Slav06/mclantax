#!/usr/bin/env python3
"""
Demo script for McLan Tax Baby Video Creator
Shows the system workflow with mock data
"""

import time
from datetime import datetime
from config import Config

def print_header(title):
    """Print a formatted header."""
    print(f"\n{'='*60}")
    print(f"🍼 {title}")
    print(f"{'='*60}")

def print_step(step_num, title, description):
    """Print a formatted step."""
    print(f"\n📋 STEP {step_num}: {title}")
    print(f"{'—'*40}")
    print(f"Description: {description}")
    print("")

def simulate_agent_work(agent_name, duration=2):
    """Simulate agent working with progress indicator."""
    print(f"🤖 {agent_name} is working...")
    
    # Simulate progress
    for i in range(duration):
        print(".", end="", flush=True)
        time.sleep(0.5)
    
    print(" ✅ Complete!")

def demo_workflow():
    """Demonstrate the complete workflow."""
    
    print_header("McLan Tax Baby Video Creator - DEMO")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🏢 Brand: {Config.BRAND_NAME} ({Config.BRAND_HANDLE})")
    print(f"📱 Target Platforms: {', '.join(Config.PLATFORMS)}")
    print(f"🎯 Goal: Create viral baby tax videos automatically")
    
    # Step 1: Trend Research
    print_step(1, "TREND RESEARCH", "Finding viral topics related to finance, lifestyle, or controversy")
    simulate_agent_work("Trend Researcher Agent")
    
    trending_topic = {
        "title": "Tax Season Memes Go Viral on TikTok",
        "description": "Young adults are creating humorous content about tax filing",
        "angle": "Perfect for baby tax content - combines trending memes with tax education",
        "viral_potential": "High - relatable financial stress + cute baby perspective"
    }
    
    print("📊 RESEARCH RESULTS:")
    print(f"   • Topic: {trending_topic['title']}")
    print(f"   • Description: {trending_topic['description']}")
    print(f"   • Baby Angle: {trending_topic['angle']}")
    print(f"   • Viral Potential: {trending_topic['viral_potential']}")
    
    # Step 2: Script Writing
    print_step(2, "SCRIPT WRITING", "Creating sassy baby script with tax twist")
    simulate_agent_work("Baby Scriptwriter Agent")
    
    script = """
    *baby voice, adorable but sassy*
    
    "Hey grownups! *giggles* So I heard you're all stressed about taxes again? 
    Like, seriously? *eye roll* 
    
    I'm literally three months old and even I know you should call McLan Tax! 
    *baby babbles excitedly*
    
    They make taxes as easy as... well, taking candy from a baby! 
    *cute laugh*
    
    So stop crying about your W-2s and go to McLan Tax dot com! 
    *blows kiss*
    
    This baby knows what's up! 💰👶"
    """
    
    print("📝 GENERATED SCRIPT:")
    print(script)
    print(f"⏱️ Duration: ~22 seconds")
    print(f"🎯 Tone: Sassy, innocent, surprisingly wise")
    
    # Step 3: Video Generation
    print_step(3, "VIDEO GENERATION", "Creating video with Heldra API using baby persona")
    simulate_agent_work("Heldra Operator Agent", 3)
    
    video_specs = {
        "format": "MP4, 9:16 aspect ratio",
        "duration": "22 seconds",
        "quality": "1080p",
        "voice": "High-pitched, playful baby voice",
        "visuals": "Animated baby character in nursery setting",
        "background": "Soft pastel nursery theme",
        "character": "Cute animated baby with expressive eyes"
    }
    
    mock_video_url = "https://example.com/videos/baby_tax_viral_1701234567.mp4"
    
    print("🎬 VIDEO GENERATED:")
    print(f"   • URL: {mock_video_url}")
    print(f"   • Format: {video_specs['format']}")
    print(f"   • Duration: {video_specs['duration']}")
    print(f"   • Voice: {video_specs['voice']}")
    print(f"   • Visuals: {video_specs['visuals']}")
    
    # Step 4: Caption Animation
    print_step(4, "CAPTION ANIMATION", "Adding viral-style captions with FFMPEG")
    simulate_agent_work("Text Animator Agent", 2)
    
    caption_features = {
        "style": "High-contrast meme-style",
        "segments": 15,
        "timing": "3-word segments, 0.5s per word",
        "colors": "White text, black background",
        "font": "Large, bold for mobile viewing",
        "animation": "Pop-in effects with emphasis"
    }
    
    sample_captions = [
        "[0.0s-1.5s] HEY GROWNUPS! *GIGGLES*",
        "[1.5s-3.0s] SO I HEARD",
        "[3.0s-4.5s] YOU'RE ALL STRESSED",
        "[4.5s-6.0s] ABOUT TAXES AGAIN?",
        "[6.0s-7.5s] LIKE, SERIOUSLY? *EYE ROLL*"
    ]
    
    print("🎨 CAPTION FEATURES:")
    for key, value in caption_features.items():
        print(f"   • {key.title()}: {value}")
    
    print("\n📄 SAMPLE CAPTIONS:")
    for caption in sample_captions:
        print(f"   {caption}")
    
    # Step 5: Social Media Copy
    print_step(5, "SOCIAL MEDIA COPY", "Creating platform-specific captions for engagement")
    simulate_agent_work("Copywriter Agent")
    
    platform_captions = {
        "TikTok": {
            "caption": "When this baby knows more about taxes than you do 😂👶 Comment 'BABY TAX' if you need help with your returns! #BabyTax #TaxSeason #Viral #McLanTax #TaxTips #FYP",
            "hashtags": "#fyp #viral #tax #baby #comedy #foryou #mclantax",
            "cta": "Follow for more baby tax wisdom! 🍼💰"
        },
        "Instagram": {
            "caption": "POV: A baby gives better tax advice than your accountant 💀\n\nThis little one knows what's up! 👶✨\n\nTax season got you stressed? Let @mclantax handle it while you focus on the important stuff... like this adorable content! 😍\n\nLink in bio for tax services! 💰",
            "hashtags": "#reels #viral #tax #baby #comedy #explore #mclantax #taxseason",
            "cta": "Double tap if you agree! 💕"
        },
        "YouTube": {
            "title": "Baby Gives SAVAGE Tax Advice (You Won't Believe What Happens Next!)",
            "description": "This baby knows more about taxes than most adults! 😂 Watch as our littlest financial advisor drops some serious tax knowledge and promotes McLan Tax Services. If a baby can figure out taxes, so can you! Visit McLanTax.com for professional tax help. #Shorts #Tax #Baby #Comedy #Viral",
            "hashtags": "#shorts #tax #finance #baby #comedy #viral #mclantax"
        }
    }
    
    print("📱 PLATFORM-SPECIFIC CAPTIONS:")
    for platform, content in platform_captions.items():
        print(f"\n   🎯 {platform.upper()}:")
        print(f"      Caption: {content.get('caption', content.get('title', 'N/A'))}")
        print(f"      Hashtags: {content.get('hashtags', 'N/A')}")
    
    # Step 6: Social Media Posting
    print_step(6, "SOCIAL MEDIA POSTING", "Scheduling and posting to all platforms")
    simulate_agent_work("Scheduler Agent", 2)
    
    post_results = {
        "TikTok": {
            "status": "Posted successfully!",
            "url": "https://tiktok.com/@mclantax/video/tiktok_1701234567",
            "expected_engagement": "12.5K views, 890 likes, 45 comments"
        },
        "Instagram": {
            "status": "Posted successfully!",
            "url": "https://instagram.com/p/instagram_1701234567",
            "expected_engagement": "8.2K views, 654 likes, 32 comments"
        },
        "YouTube": {
            "status": "Posted successfully!",
            "url": "https://youtube.com/shorts/youtube_1701234567",
            "expected_engagement": "15.3K views, 1.2K likes, 67 comments"
        }
    }
    
    print("🚀 POSTING RESULTS:")
    for platform, result in post_results.items():
        print(f"\n   📱 {platform.upper()}:")
        print(f"      Status: {result['status']}")
        print(f"      URL: {result['url']}")
        print(f"      Expected: {result['expected_engagement']}")
    
    # Final Summary
    print_header("WORKFLOW COMPLETE!")
    print("🎉 Success! One viral baby tax video created and posted!")
    print(f"📊 Total platforms: {len(Config.PLATFORMS)}")
    print(f"⏱️ Total time: ~12 minutes (estimated)")
    print(f"🎯 Next run: Scheduled for optimal posting times")
    print(f"📈 Expected reach: 35,000+ views across all platforms")
    print(f"💰 Brand exposure: {Config.BRAND_NAME} prominently featured")
    
    print("\n🔄 AUTOMATION READY:")
    print(f"   • System can run {Config.POSTS_PER_DAY} times daily")
    print(f"   • Each run creates fresh, trending content")
    print(f"   • Fully automated from research to posting")
    print(f"   • Brand consistency maintained across platforms")
    
    print("\n🍼 Thanks for watching the McLan Tax Baby Video Creator demo!")
    print("This system is ready to create viral content automatically! 🚀")

if __name__ == "__main__":
    demo_workflow() 