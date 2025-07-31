"""
Demo: Channel Agent Test
Simple test of the marketing channel selection agent
"""
import os
from crewai import Agent, Task, Crew, LLM

# Setup
api_key = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key

# Create LLM
llm = LLM(model="gemini/gemini-1.5-flash")

# Create channel agent
channel_agent = Agent(
    llm=llm,
    role="Digital Marketing Channel Expert",
    goal="Recommend the most effective marketing channels and platforms based on target audience, budget, and campaign objectives",
    backstory="""You are a digital marketing strategist with deep expertise in all major advertising and 
    marketing platforms. You've managed millions in ad spend across Google Ads, Meta, LinkedIn, TikTok, 
    YouTube, and emerging platforms. You understand audience behavior on each platform and can optimize 
    channel mix for maximum ROI.""",
    memory=True,
    verbose=True
)

# Sample test data
product = "AI-powered fitness tracker with personalized coaching"
budget = "Medium ($5K-25K monthly)"
goal = "Acquire 50,000 new users and achieve 10,000 premium subscriptions"

# Create task
channel_task = Task(
    description=f"""
    Recommend optimal marketing channels for:
    Product: {product}
    Budget Range: {budget}
    Marketing Goal: {goal}
    
    Provide:
    1. Top 5 recommended channels ranked by priority
    2. Budget allocation suggestions (percentages)
    3. Rationale for each channel selection
    4. Expected performance metrics
    5. Channel-specific strategies
    6. Timeline recommendations
    
    Focus on ROI and scalability.
    """,
    agent=channel_agent,
    expected_output="Prioritized list of marketing channels with budget allocation, performance expectations, and strategic recommendations."
)

# Run test
print("📱 Testing Channel Agent...")
print("=" * 50)

crew = Crew(agents=[channel_agent], tasks=[channel_task], verbose=True)
result = crew.kickoff()

print("\n" + "=" * 50)
print("✅ Channel Agent Results:")
print("=" * 50)
print(result)