"""
Demo: Schedule Agent Test
Simple test of the timing optimization and scheduling agent
"""
import os
from crewai import Agent, Task, Crew, LLM

# Setup
api_key = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key

# Create LLM
llm = LLM(model="gemini/gemini-1.5-flash")

# Create schedule agent
schedule_agent = Agent(
    llm=llm,
    role="Campaign Timing & Schedule Optimization Expert",
    goal="Create optimal posting schedules and timing strategies to maximize reach, engagement, and conversions",
    backstory="""You are a data-driven marketing timing specialist who understands audience behavior patterns 
    across different platforms and time zones. You've optimized thousands of campaigns and know exactly when 
    different demographics are most active and likely to engage with content.""",
    memory=True,
    verbose=True
)

# Sample test data
channels = "Google Ads, Meta (Facebook/Instagram), LinkedIn, YouTube"
duration = "6 weeks"
audience = "Health-conscious professionals aged 25-45"

# Create task
schedule_task = Task(
    description=f"""
    Create optimal posting schedule for:
    Selected Channels: {channels}
    Campaign Duration: {duration}
    Target Audience: {audience}
    
    Provide:
    1. Weekly posting frequency for each channel
    2. Best days and times for each platform
    3. Content calendar structure
    4. Seasonal considerations
    5. A/B testing schedule recommendations
    6. Performance monitoring milestones
    
    Optimize for maximum engagement and conversions.
    """,
    agent=schedule_agent,
    expected_output="Comprehensive posting schedule with optimal timing, frequency recommendations, and strategic calendar for maximum campaign performance."
)

# Run test
print("📅 Testing Schedule Agent...")
print("=" * 50)

crew = Crew(agents=[schedule_agent], tasks=[schedule_task], verbose=True)
result = crew.kickoff()

print("\n" + "=" * 50)
print("✅ Schedule Agent Results:")
print("=" * 50)
print(result)