from crewai import Task
from config import Config

class BabyTaxVideoTasks:
    """Task definitions for viral baby tax video creation workflow."""
    
    def research_trending_topic(self, agent):
        """Task for researching trending topics."""
        return Task(
            description="""Research and identify current trending topics related to finance, lifestyle, 
            or controversy that can be creatively adapted into baby tax content. Focus on:
            
            1. Search for viral trends on social media platforms
            2. Identify financial news or controversies people are discussing
            3. Find lifestyle trends that relate to money/expenses
            4. Look for topics that can be tied to tax season or financial planning
            5. Evaluate potential for viral baby content adaptation
            
            Provide 3-5 trending topic options with:
            - Brief description of the trend
            - Why it's trending/viral potential
            - How it can be tied to taxes/McLan Tax
            - Suggested baby persona angle
            
            Choose the BEST topic for today's video and explain why.""",
            agent=agent,
            expected_output="A detailed trending topic analysis with the selected topic and creative angle for baby tax content."
        )
    
    def write_baby_script(self, agent):
        """Task for writing the baby persona script."""
        return Task(
            description="""Write a witty, viral video script from a baby's perspective based on the trending topic. 
            Requirements:
            
            1. Duration: 3-45 seconds when spoken
            2. Tone: Sassy, innocent yet wise baby voice
            3. Content: Tie the trending topic to taxes or McLan Tax services
            4. Structure: Hook, main point, call-to-action
            5. Viral elements: Unexpected humor, relatable situations, quotable phrases
            
            The script should:
            - Start with an attention-grabbing opening
            - Present the tax angle in a fun, accessible way
            - Include subtle McLan Tax promotion
            - End with engagement hook (question, challenge, etc.)
            - Be written in baby-speak but still clear and understandable
            
            Format as spoken dialogue with timing notes.""",
            agent=agent,
            expected_output="A complete video script with timing, baby-voice dialogue, and viral elements."
        )
    
    def generate_video(self, agent):
        """Task for generating the video using Heldra API."""
        return Task(
            description="""Transform the script into a professional video using Heldra API. Configure:
            
            1. Voice settings:
               - High-pitched, playful baby voice
               - Slightly faster pace for viral content
               - Emotional tone matching script content
            
            2. Visual settings:
               - Vertical format (9:16) for social media
               - Animated baby character or avatar
               - Nursery-themed or baby-appropriate background
               - Visual elements that match script content
            
            3. Production settings:
               - 1080p quality
               - Auto-timing based on script
               - Format: MP4 for social media compatibility
            
            Submit to Heldra API and monitor generation progress.
            Return video URL and production details.""",
            agent=agent,
            expected_output="Generated video URL with production specifications and readiness confirmation."
        )
    
    def add_viral_captions(self, agent):
        """Task for adding animated captions to the video."""
        return Task(
            description="""Add high-impact, viral-style captions to the video. Requirements:
            
            1. Caption style:
               - High-contrast colors (white text, black background)
               - Large, bold fonts for mobile viewing
               - Meme-style formatting
               - Animated entrance/exit effects
            
            2. Timing:
               - Precise synchronization with audio
               - 3-word segments for easy reading
               - Fast-paced for viral content
               - Strategic pauses for emphasis
            
            3. Positioning:
               - Bottom-center placement
               - Safe area for all social platforms
               - Non-overlapping with key visuals
            
            4. Additional effects:
               - Highlight key phrases
               - Emphasize call-to-action
               - Brand name emphasis
            
            Output final captioned video ready for social media.""",
            agent=agent,
            expected_output="Final video with professional captions, optimized for viral social media consumption."
        )
    
    def create_social_captions(self, agent):
        """Task for creating platform-specific social media captions."""
        return Task(
            description="""Create engaging captions for each social media platform that match the baby persona:
            
            Platform-specific requirements:
            
            1. TikTok:
               - Baby-voice text style
               - Trending hashtags integration
               - Engagement questions
               - Call-to-action for McLan Tax
            
            2. Instagram:
               - Story-style caption with baby personality
               - Relevant hashtags for reach
               - Bio link mention
               - Reels-optimized formatting
            
            3. YouTube Shorts:
               - Descriptive title incorporating trending topic
               - Detailed description with baby character
               - Strategic keyword placement
               - Subscription encouragement
            
            Each caption should:
            - Maintain baby persona consistency
            - Encourage comments and shares
            - Include McLan Tax branding
            - Use platform-specific viral strategies
            - Include relevant hashtags and mentions""",
            agent=agent,
            expected_output="Platform-specific social media captions optimized for engagement and brand awareness."
        )
    
    def schedule_and_post(self, agent):
        """Task for scheduling and posting to social media."""
        return Task(
            description=f"""Schedule and post the video content across all social media platforms:
            
            1. Platform distribution:
               - TikTok: Post with viral optimization
               - Instagram Reels: Story and feed posting
               - YouTube Shorts: Upload with SEO optimization
            
            2. Scheduling strategy:
               - Post at optimal times for each platform
               - Schedule {Config.POSTS_PER_DAY} posts per day
               - Stagger posting times for maximum reach
               - Consider audience timezone preferences
            
            3. Post optimization:
               - Use platform-specific captions
               - Include {Config.BRAND_HANDLE} tag
               - Apply appropriate hashtags
               - Enable engagement features
            
            4. Tracking preparation:
               - Record post URLs and IDs
               - Set up engagement monitoring
               - Prepare performance metrics tracking
            
            Execute posting and confirm successful distribution.""",
            agent=agent,
            expected_output="Confirmation of successful posts across all platforms with URLs and scheduling details."
        ) 