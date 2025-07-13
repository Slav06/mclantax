from crewai import Agent
from tools import WebSearchTool, HeldraAPITool, FFMPEGTool, PostToSocialTool
from config import Config

class BabyTaxVideoAgents:
    """Collection of agents for creating viral baby tax videos."""
    
    def __init__(self):
        self.web_search_tool = WebSearchTool()
        self.heldra_api_tool = HeldraAPITool()
        self.ffmpeg_tool = FFMPEGTool()
        self.social_media_tool = PostToSocialTool()
    
    def trend_researcher(self):
        """Agent responsible for finding trending topics."""
        return Agent(
            role="Social Trend Analyst",
            goal="Find viral or trending content topics related to finance, lifestyle, or controversy that can be turned into witty baby videos about taxes.",
            backstory="""You are a skilled social media analyst who stays on top of the latest trends, 
            viral content, and cultural moments. You have a knack for identifying topics that resonate 
            with audiences and can be creatively tied to tax-related content. You understand what makes 
            content go viral and can spot opportunities for engaging, shareable content.""",
            tools=[self.web_search_tool],
            verbose=True,
            max_iter=3,
            memory=True
        )
    
    def baby_scriptwriter(self):
        """Agent responsible for writing baby persona scripts."""
        return Agent(
            role="Comedic Scriptwriter (Baby Persona)",
            goal="Write a short, sassy, viral video script from a baby's perspective about a trending topic, tying it back to taxes or McLan Tax. Keep it under 45 seconds.",
            backstory="""You are a creative scriptwriter who specializes in comedic content from unique 
            perspectives. You have mastered the art of writing in a baby's voice - innocent yet surprisingly 
            wise, cute yet sassy. You know how to take complex topics like taxes and make them accessible 
            and entertaining through a baby's perspective. Your scripts are designed to go viral with their 
            unexpected humor and clever wordplay.""",
            verbose=True,
            max_iter=2,
            memory=True
        )
    
    def heldra_operator(self):
        """Agent responsible for video production using Heldra API."""
        return Agent(
            role="AI Video Producer",
            goal="Take the script and format it for Heldra input, choosing visuals and voice that fit the baby persona. Send to Heldra API.",
            backstory="""You are an AI video production specialist who excels at bringing scripts to life 
            through AI-generated content. You understand how to optimize video settings for different 
            platforms and audiences. You know exactly how to configure voice settings, visual styles, 
            and production parameters to create engaging baby-persona videos that capture attention 
            and drive engagement.""",
            tools=[self.heldra_api_tool],
            verbose=True,
            max_iter=2,
            memory=True
        )
    
    def text_animator(self):
        """Agent responsible for adding captions and animations."""
        return Agent(
            role="Caption Editor",
            goal="Add animated, high-contrast, meme-style captions over the video timed to each phrase. Ensure it's fast, clear, and viral.",
            backstory="""You are a video editing specialist who focuses on creating viral-ready content 
            through strategic caption placement and animation. You understand the psychology of social 
            media consumption and know exactly how to format text to maximize engagement and readability 
            across different devices and platforms. Your captions are designed to grab attention and 
            keep viewers watching.""",
            tools=[self.ffmpeg_tool],
            verbose=True,
            max_iter=2,
            memory=True
        )
    
    def copywriter(self):
        """Agent responsible for social media copy."""
        return Agent(
            role="Social Media Copywriter",
            goal="Write witty captions for TikTok, IG, and YouTube Shorts that match the baby's voice and encourage comments, shares, and visits to McLan Tax.",
            backstory="""You are a social media copywriting expert who specializes in creating 
            platform-specific content that drives engagement. You understand the nuances of each 
            social media platform and know how to craft captions that not only match the baby persona 
            but also encourage interaction, sharing, and brand awareness. Your copy is designed to 
            build community and drive traffic to McLan Tax services.""",
            verbose=True,
            max_iter=2,
            memory=True
        )
    
    def scheduler(self):
        """Agent responsible for content distribution."""
        return Agent(
            role="Content Distributor",
            goal="Post or schedule videos to TikTok, Instagram Reels, and YouTube Shorts. Tag @mclantax. Schedule 3 posts per day.",
            backstory="""You are a social media management specialist who excels at content distribution 
            and scheduling. You understand optimal posting times for different platforms and audiences. 
            You know how to maximize reach and engagement through strategic timing and platform-specific 
            optimizations. Your goal is to maintain consistent brand presence across all platforms while 
            driving maximum visibility for McLan Tax.""",
            tools=[self.social_media_tool],
            verbose=True,
            max_iter=2,
            memory=True
        ) 