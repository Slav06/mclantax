import requests
import json
import time
from typing import Dict, Any, Optional
from crewai_tools import BaseTool
from config import Config

class HeldraAPITool(BaseTool):
    name: str = "Heldra API Tool"
    description: str = "Generate AI videos using Heldra API with baby persona visuals and voice."
    
    def _run(self, script: str, voice_style: str = "baby", visual_style: str = "cute_baby") -> str:
        """
        Generate a video using Heldra API.
        
        Args:
            script (str): The video script
            voice_style (str): Voice style for the video
            visual_style (str): Visual style for the video
            
        Returns:
            str: Video generation result with URL or error message
        """
        try:
            if Config.HELDRA_API_KEY == "your_heldra_api_key_here":
                return self._mock_video_generation(script, voice_style, visual_style)
            
            # Prepare video generation request
            payload = {
                "script": script,
                "voice_settings": {
                    "style": voice_style,
                    "speed": 1.1,  # Slightly faster for viral content
                    "pitch": "high",  # Baby voice
                    "emotion": "playful"
                },
                "visual_settings": {
                    "style": visual_style,
                    "aspect_ratio": "9:16",  # Vertical for social media
                    "duration": "auto",  # Based on script length
                    "background": "nursery_themed",
                    "character": "animated_baby"
                },
                "format": "mp4",
                "quality": "1080p"
            }
            
            headers = {
                "Authorization": f"Bearer {Config.HELDRA_API_KEY}",
                "Content-Type": "application/json"
            }
            
            # Submit video generation request
            response = requests.post(
                f"{Config.HELDRA_API_URL}/generate",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                job_id = result.get("job_id")
                
                # Poll for completion
                return self._poll_video_status(job_id, headers)
            else:
                return f"Error generating video: {response.status_code} - {response.text}"
                
        except Exception as e:
            return f"Error during video generation: {str(e)}"
    
    def _poll_video_status(self, job_id: str, headers: Dict[str, str]) -> str:
        """Poll the video generation status until completion."""
        max_attempts = 60  # 5 minutes max
        attempt = 0
        
        while attempt < max_attempts:
            try:
                response = requests.get(
                    f"{Config.HELDRA_API_URL}/status/{job_id}",
                    headers=headers
                )
                
                if response.status_code == 200:
                    result = response.json()
                    status = result.get("status")
                    
                    if status == "completed":
                        video_url = result.get("video_url")
                        return f"Video generated successfully! URL: {video_url}"
                    elif status == "failed":
                        error = result.get("error", "Unknown error")
                        return f"Video generation failed: {error}"
                    else:
                        time.sleep(5)  # Wait 5 seconds before next check
                        attempt += 1
                else:
                    return f"Error checking status: {response.status_code}"
                    
            except Exception as e:
                return f"Error polling status: {str(e)}"
        
        return "Video generation timed out"
    
    def _mock_video_generation(self, script: str, voice_style: str, visual_style: str) -> str:
        """Mock video generation for testing purposes."""
        mock_video_url = f"https://example.com/videos/baby_tax_video_{int(time.time())}.mp4"
        
        return f"""
VIDEO GENERATED SUCCESSFULLY!

Script: {script[:100]}...
Voice Style: {voice_style}
Visual Style: {visual_style}
Duration: {len(script.split()) * 0.5:.1f} seconds
Video URL: {mock_video_url}

Video Features:
- Vertical format (9:16) for social media
- Animated baby character
- Nursery-themed background
- High-pitched, playful voice
- Auto-timed to script
- 1080p quality
- Ready for caption overlay

Status: Ready for Text Animator agent
""" 