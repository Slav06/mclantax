import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")
    HELDRA_API_KEY = os.getenv("HELDRA_API_KEY", "your_heldra_api_key_here")
    HELDRA_API_URL = os.getenv("HELDRA_API_URL", "https://api.heldra.com/v1")
    TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN", "your_tiktok_access_token_here")
    INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN", "your_instagram_access_token_here")
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "your_youtube_api_key_here")
    ZAPIER_NLA_API_KEY = os.getenv("ZAPIER_NLA_API_KEY", "your_zapier_nla_api_key_here")
    SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "your_serpapi_key_here")
    
    # Brand Configuration
    BRAND_NAME = os.getenv("BRAND_NAME", "McLan Tax")
    BRAND_HANDLE = os.getenv("BRAND_HANDLE", "@mclantax")
    POSTS_PER_DAY = int(os.getenv("POSTS_PER_DAY", "3"))
    
    # Video Configuration
    VIDEO_DURATION_MIN = 3
    VIDEO_DURATION_MAX = 45
    
    # Social Media Platforms
    PLATFORMS = ["tiktok", "instagram", "youtube_shorts"]
    
    # Content Topics
    CONTENT_TOPICS = [
        "finance",
        "lifestyle", 
        "controversy",
        "taxes",
        "trending_topics"
    ] 