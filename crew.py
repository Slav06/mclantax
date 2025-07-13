from crewai import Crew, Process
from agents import BabyTaxVideoAgents
from tasks import BabyTaxVideoTasks
from config import Config

class BabyTaxVideoCrew:
    """Main crew for creating viral baby tax videos."""
    
    def __init__(self):
        self.agents = BabyTaxVideoAgents()
        self.tasks = BabyTaxVideoTasks()
    
    def create_crew(self):
        """Create and configure the crew with all agents and tasks."""
        
        # Initialize agents
        trend_researcher = self.agents.trend_researcher()
        baby_scriptwriter = self.agents.baby_scriptwriter()
        heldra_operator = self.agents.heldra_operator()
        text_animator = self.agents.text_animator()
        copywriter = self.agents.copywriter()
        scheduler = self.agents.scheduler()
        
        # Create tasks
        research_task = self.tasks.research_trending_topic(trend_researcher)
        script_task = self.tasks.write_baby_script(baby_scriptwriter)
        video_task = self.tasks.generate_video(heldra_operator)
        caption_task = self.tasks.add_viral_captions(text_animator)
        copy_task = self.tasks.create_social_captions(copywriter)
        post_task = self.tasks.schedule_and_post(scheduler)
        
        # Create crew with sequential process
        crew = Crew(
            agents=[
                trend_researcher,
                baby_scriptwriter,
                heldra_operator,
                text_animator,
                copywriter,
                scheduler
            ],
            tasks=[
                research_task,
                script_task,
                video_task,
                caption_task,
                copy_task,
                post_task
            ],
            process=Process.sequential,
            verbose=True,
            memory=True,
            planning=True,
            output_log_file="baby_tax_crew_log.txt"
        )
        
        return crew
    
    def run_daily_content_creation(self):
        """Run the daily content creation process."""
        print("🍼 Starting Baby Tax Video Creation Process...")
        print(f"📱 Target platforms: {', '.join(Config.PLATFORMS)}")
        print(f"📅 Daily posts: {Config.POSTS_PER_DAY}")
        print(f"🏢 Brand: {Config.BRAND_NAME} ({Config.BRAND_HANDLE})")
        
        crew = self.create_crew()
        result = crew.kickoff()
        
        print("\n🎉 Daily content creation completed!")
        print("📊 Results:")
        print(result)
        
        return result
    
    def run_batch_content_creation(self, num_videos=3):
        """Run batch content creation for multiple videos."""
        print(f"🍼 Starting Batch Creation: {num_videos} videos")
        
        results = []
        for i in range(num_videos):
            print(f"\n📹 Creating video {i+1}/{num_videos}...")
            try:
                result = self.run_daily_content_creation()
                results.append(result)
            except Exception as e:
                print(f"❌ Error creating video {i+1}: {str(e)}")
                results.append(f"Error: {str(e)}")
        
        print(f"\n🎬 Batch creation completed: {len(results)} videos processed")
        return results

if __name__ == "__main__":
    # Example usage
    baby_crew = BabyTaxVideoCrew()
    
    # Run single video creation
    baby_crew.run_daily_content_creation()
    
    # Or run batch creation
    # baby_crew.run_batch_content_creation(num_videos=5) 