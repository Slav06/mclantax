import requests
import json
from typing import Dict, Any, List
from crewai_tools import BaseTool
from config import Config

class WebSearchTool(BaseTool):
    name: str = "Web Search Tool"
    description: str = "Search the web for trending topics, viral content, and current events related to finance, lifestyle, or controversy."
    
    def _run(self, query: str) -> str:
        """
        Search the web for trending topics and viral content.
        
        Args:
            query (str): The search query
            
        Returns:
            str: Formatted search results with trending topics
        """
        try:
            # Using SerpAPI for web search
            if Config.SERPAPI_API_KEY == "your_serpapi_key_here":
                return self._mock_trending_results(query)
            
            params = {
                "q": query,
                "api_key": Config.SERPAPI_API_KEY,
                "engine": "google",
                "num": 10,
                "gl": "us",
                "hl": "en"
            }
            
            response = requests.get("https://serpapi.com/search", params=params)
            
            if response.status_code == 200:
                results = response.json()
                return self._format_search_results(results)
            else:
                return f"Error searching: {response.status_code}"
                
        except Exception as e:
            return f"Error during web search: {str(e)}"
    
    def _format_search_results(self, results: Dict[str, Any]) -> str:
        """Format search results for the agent."""
        formatted_results = []
        
        if "organic_results" in results:
            for result in results["organic_results"][:5]:
                formatted_results.append(f"Title: {result.get('title', 'N/A')}")
                formatted_results.append(f"Snippet: {result.get('snippet', 'N/A')}")
                formatted_results.append(f"Link: {result.get('link', 'N/A')}")
                formatted_results.append("---")
        
        return "\n".join(formatted_results)
    
    def _mock_trending_results(self, query: str) -> str:
        """Mock trending results for testing purposes."""
        mock_trends = [
            {
                "title": "Tax Season Memes Go Viral on TikTok",
                "snippet": "Young adults are creating humorous content about tax filing, making financial literacy fun and accessible.",
                "relevance": "Perfect for baby tax content - combines trending memes with tax education"
            },
            {
                "title": "Inflation Concerns Dominate Social Media",
                "snippet": "Rising costs of everyday items spark viral content about budgeting and financial planning.",
                "relevance": "Great angle for baby perspective on expensive diapers vs. tax breaks"
            },
            {
                "title": "Cryptocurrency Tax Confusion",
                "snippet": "Many people are confused about how to report crypto gains on their taxes.",
                "relevance": "Perfect for baby character explaining complex tax topics simply"
            },
            {
                "title": "Work From Home Tax Deductions",
                "snippet": "Remote workers are discovering new tax deductions they can claim.",
                "relevance": "Baby working from home nursery - cute angle for tax tips"
            },
            {
                "title": "Gen Z Financial Stress",
                "snippet": "Young adults are stressed about money management and tax responsibilities.",
                "relevance": "Baby offering tax advice to stressed millennials/Gen Z"
            }
        ]
        
        formatted = []
        for trend in mock_trends:
            formatted.append(f"TRENDING TOPIC: {trend['title']}")
            formatted.append(f"Description: {trend['snippet']}")
            formatted.append(f"Content Angle: {trend['relevance']}")
            formatted.append("---")
        
        return "\n".join(formatted) 