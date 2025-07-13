# 🍼 McLan Tax Baby Video Creator

A CrewAI-powered system for creating viral baby tax videos automatically for social media platforms.

## 🎯 Overview

This project uses CrewAI to orchestrate a team of AI agents that work together to create engaging, viral baby tax videos. The system researches trending topics, writes scripts from a baby's perspective, generates videos, adds captions, creates social media copy, and posts to multiple platforms.

## 🤖 Agents & Workflow

### 1. **Trend Researcher** 🔍
- **Role**: Social Trend Analyst
- **Goal**: Find viral trending topics related to finance, lifestyle, or controversy
- **Tools**: WebSearchTool (SerpAPI)

### 2. **Baby Scriptwriter** ✍️
- **Role**: Comedic Scriptwriter (Baby Persona)
- **Goal**: Write short, sassy viral scripts from a baby's perspective
- **Duration**: 3-45 seconds

### 3. **Heldra Operator** 🎬
- **Role**: AI Video Producer
- **Goal**: Generate videos using Heldra API with baby persona
- **Tools**: HeldraAPITool

### 4. **Text Animator** 🎨
- **Role**: Caption Editor
- **Goal**: Add viral-style captions with high contrast and meme formatting
- **Tools**: FFMPEGTool

### 5. **Copywriter** 📝
- **Role**: Social Media Copywriter
- **Goal**: Create platform-specific captions for TikTok, Instagram, YouTube
- **Focus**: Engagement, shares, McLan Tax promotion

### 6. **Scheduler** 📅
- **Role**: Content Distributor
- **Goal**: Post/schedule videos across social platforms
- **Tools**: PostToSocialTool
- **Frequency**: 3 posts per day

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- API keys (see Configuration section)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd mclantax

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (create .env file)
cp .env.example .env
# Edit .env with your API keys
```

### Configuration
Create a `.env` file with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
HELDRA_API_KEY=your_heldra_api_key_here
SERPAPI_API_KEY=your_serpapi_key_here
TIKTOK_ACCESS_TOKEN=your_tiktok_access_token_here
INSTAGRAM_ACCESS_TOKEN=your_instagram_access_token_here
YOUTUBE_API_KEY=your_youtube_api_key_here
BRAND_NAME=McLan Tax
BRAND_HANDLE=@mclantax
POSTS_PER_DAY=3
```

### Usage

#### Basic Usage
```bash
# Create a single video
python main.py

# Create multiple videos in batch
python main.py --batch 5

# Run in demo mode (no API calls)
python main.py --demo

# Show current configuration
python main.py --config
```

#### Advanced Usage
```bash
# Run with verbose output
python main.py --verbose

# Direct crew execution
python crew.py
```

## 📁 Project Structure

```
mclantax/
├── main.py                 # Main entry point
├── crew.py                 # CrewAI crew configuration
├── agents.py               # Agent definitions
├── tasks.py                # Task definitions
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── tools/                 # Custom tools
│   ├── __init__.py
│   ├── web_search_tool.py     # Trend research
│   ├── heldra_api_tool.py     # Video generation
│   ├── ffmpeg_tool.py         # Caption animation
│   └── social_media_tool.py   # Social posting
├── outputs/               # Generated videos (created automatically)
└── logs/                  # Application logs (created automatically)
```

## 🔧 API Configuration

### Required APIs

1. **OpenAI API** - For AI agents
   - Get key from: https://platform.openai.com/

2. **Heldra API** - For video generation
   - Get key from: https://heldra.com/

3. **SerpAPI** - For web search
   - Get key from: https://serpapi.com/

### Optional APIs (for full functionality)

4. **TikTok API** - For posting to TikTok
5. **Instagram API** - For posting to Instagram
6. **YouTube API** - For posting to YouTube

## 🎬 Video Creation Process

1. **Research** → Find trending topics related to finance/lifestyle
2. **Script** → Write baby-voice script tying topic to taxes
3. **Video** → Generate video with baby persona using Heldra
4. **Captions** → Add viral-style captions with FFMPEG
5. **Copy** → Create platform-specific social media captions
6. **Post** → Schedule and post to TikTok, Instagram, YouTube

## 📊 Output Examples

### Video Specifications
- **Format**: MP4, 9:16 aspect ratio
- **Duration**: 3-45 seconds
- **Quality**: 1080p
- **Voice**: High-pitched baby voice
- **Visuals**: Animated baby character, nursery theme

### Caption Style
- **Font**: Large, bold for mobile
- **Colors**: High contrast (white text, black background)
- **Timing**: 3-word segments, 0.5s per word
- **Style**: Meme-style formatting, uppercase text

### Social Media Optimization
- **TikTok**: Trending hashtags, engagement questions
- **Instagram**: Story-style captions, bio link mentions
- **YouTube**: SEO-optimized titles and descriptions

## 🛠️ Customization

### Brand Configuration
Edit `config.py` to customize:
- Brand name and handle
- Target platforms
- Content topics
- Video specifications

### Agent Behavior
Modify agent backstories and goals in `agents.py`

### Task Requirements
Update task descriptions in `tasks.py`

### Tool Configuration
Customize tool behavior in the `tools/` directory

## 📝 Development

### Adding New Tools
1. Create tool class in `tools/`
2. Inherit from `BaseTool`
3. Implement `_run()` method
4. Add to `tools/__init__.py`

### Adding New Agents
1. Create agent method in `BabyTaxVideoAgents`
2. Configure role, goal, backstory, and tools
3. Add to crew in `crew.py`

### Adding New Tasks
1. Create task method in `BabyTaxVideoTasks`
2. Define description and expected output
3. Add to crew workflow

## 🔍 Troubleshooting

### Common Issues

1. **Missing API Keys**: System will run in demo mode
2. **FFMPEG Not Found**: Install FFMPEG for caption functionality
3. **Rate Limits**: APIs may have rate limits - adjust batch sizes

### Debug Mode
```bash
python main.py --verbose
```

### Log Files
Check `logs/` directory for detailed execution logs

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## 📄 License

This project is for McLan Tax internal use.

## 🆘 Support

For issues and questions:
- Check the troubleshooting section
- Review log files
- Contact the development team

---

**Created with ❤️ by the McLan Tax team using CrewAI** 