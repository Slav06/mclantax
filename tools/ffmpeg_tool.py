import ffmpeg
import os
import json
import tempfile
from typing import Dict, Any, List
from crewai_tools import BaseTool
from config import Config
import time

class FFMPEGTool(BaseTool):
    name: str = "FFMPEG Tool"
    description: str = "Add animated, high-contrast, meme-style captions to videos with precise timing."
    
    def _run(self, video_url: str, script: str, caption_style: str = "viral_meme") -> str:
        """
        Add animated captions to a video.
        
        Args:
            video_url (str): URL or path to the source video
            script (str): The script to create captions from
            caption_style (str): Style of captions to apply
            
        Returns:
            str: Path to the captioned video or error message
        """
        try:
            # For demonstration, return mock result
            if "example.com" in video_url:
                return self._mock_caption_generation(video_url, script, caption_style)
            
            # Parse script into timed segments
            caption_segments = self._parse_script_to_segments(script)
            
            # Generate caption files
            srt_file = self._generate_srt_file(caption_segments)
            
            # Apply captions to video
            output_path = self._apply_captions_to_video(video_url, srt_file, caption_style)
            
            # Clean up temporary files
            if os.path.exists(srt_file):
                os.remove(srt_file)
            
            return f"Captions added successfully! Output: {output_path}"
            
        except Exception as e:
            return f"Error adding captions: {str(e)}"
    
    def _parse_script_to_segments(self, script: str) -> List[Dict[str, Any]]:
        """Parse script into timed segments for captions."""
        words = script.split()
        segments = []
        words_per_segment = 3  # Short segments for viral content
        
        for i in range(0, len(words), words_per_segment):
            segment_words = words[i:i + words_per_segment]
            start_time = i * 0.5  # 0.5 seconds per word
            end_time = (i + len(segment_words)) * 0.5
            
            segments.append({
                "text": " ".join(segment_words).upper(),  # Uppercase for meme style
                "start": start_time,
                "end": end_time
            })
        
        return segments
    
    def _generate_srt_file(self, segments: List[Dict[str, Any]]) -> str:
        """Generate SRT subtitle file."""
        srt_content = []
        
        for i, segment in enumerate(segments, 1):
            start_time = self._format_time(segment["start"])
            end_time = self._format_time(segment["end"])
            
            srt_content.append(f"{i}")
            srt_content.append(f"{start_time} --> {end_time}")
            srt_content.append(segment["text"])
            srt_content.append("")  # Empty line between segments
        
        # Write to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.srt', delete=False) as f:
            f.write("\n".join(srt_content))
            return f.name
    
    def _format_time(self, seconds: float) -> str:
        """Format time for SRT format."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millisecs = int((seconds % 1) * 1000)
        
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millisecs:03d}"
    
    def _apply_captions_to_video(self, video_path: str, srt_file: str, style: str) -> str:
        """Apply captions to video using FFMPEG."""
        output_path = f"output_with_captions_{int(time.time())}.mp4"
        
        # Caption style configurations
        styles = {
            "viral_meme": {
                "fontsize": 60,
                "fontcolor": "white",
                "box": 1,
                "boxcolor": "black@0.8",
                "borderw": 3,
                "bordercolor": "black"
            },
            "high_contrast": {
                "fontsize": 50,
                "fontcolor": "yellow",
                "box": 1,
                "boxcolor": "black@0.9",
                "borderw": 2,
                "bordercolor": "black"
            }
        }
        
        style_config = styles.get(style, styles["viral_meme"])
        
        # Build FFMPEG command
        input_video = ffmpeg.input(video_path)
        
        # Create subtitle filter
        subtitle_filter = f"subtitles={srt_file}:force_style='FontSize={style_config['fontsize']},PrimaryColour=&H{self._color_to_hex(style_config['fontcolor'])},BorderStyle=3,Outline={style_config['borderw']},BackColour=&H{self._color_to_hex(style_config['boxcolor'])}'"
        
        # Apply filter and output
        out = ffmpeg.output(
            input_video,
            output_path,
            vf=subtitle_filter,
            **{"c:a": "copy"}  # Copy audio without re-encoding
        )
        
        # Run FFMPEG
        ffmpeg.run(out, overwrite_output=True)
        
        return output_path
    
    def _color_to_hex(self, color: str) -> str:
        """Convert color name to hex for FFMPEG."""
        color_map = {
            "white": "FFFFFF",
            "black": "000000",
            "yellow": "FFFF00",
            "red": "FF0000",
            "blue": "0000FF"
        }
        return color_map.get(color.lower(), "FFFFFF")
    
    def _mock_caption_generation(self, video_url: str, script: str, style: str) -> str:
        """Mock caption generation for testing."""
        mock_output = f"captioned_video_{int(time.time())}.mp4"
        
        # Parse script to show caption breakdown
        words = script.split()
        num_segments = len(words) // 3 + (1 if len(words) % 3 else 0)
        
        return f"""
CAPTIONS ADDED SUCCESSFULLY!

Input Video: {video_url}
Output Video: {mock_output}
Caption Style: {style}
Total Segments: {num_segments}
Duration: {len(words) * 0.5:.1f} seconds

Caption Features:
- High-contrast, meme-style text
- Uppercase for viral appeal
- 3-word segments for readability
- Precise timing (0.5s per word)
- Black background with white text
- Bold borders for mobile viewing
- Auto-positioned at bottom center

Sample Caption Segments:
{self._generate_sample_captions(script)}

Status: Ready for social media posting
"""
    
    def _generate_sample_captions(self, script: str) -> str:
        """Generate sample caption segments for preview."""
        words = script.split()
        samples = []
        
        for i in range(0, min(9, len(words)), 3):  # Show first 3 segments
            segment_words = words[i:i + 3]
            start_time = i * 0.5
            end_time = (i + len(segment_words)) * 0.5
            
            samples.append(f"[{start_time:.1f}s-{end_time:.1f}s] {' '.join(segment_words).upper()}")
        
        return "\n".join(samples) 