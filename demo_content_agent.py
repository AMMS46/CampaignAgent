"""
Demo: Content Agent Test
Simple test of the creative content generation agent
"""
import os
from crewai import Agent, Task, Crew, LLM

# Setup
api_key = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key

# Create LLM
llm = LLM(model="gemini/gemini-1.5-flash")

# Create content agent
content_agent = Agent(
    llm=llm,
    role="Creative Content Strategist",
    goal="Create compelling, conversion-focused marketing content that resonates with target audiences",
    backstory="""You are a creative marketing genius with a track record of creating viral campaigns and 
    high-converting content. You understand consumer psychology and can craft messages that inspire action. 
    Your content consistently drives engagement and conversions across all platforms.""",
    memory=True,
    verbose=True
)

# Sample test data
product = "AI-powered fitness tracker with personalized coaching"
audience = "Health-conscious professionals aged 25-45"

# Create task
content_task = Task(
    description=f"""
    Create compelling marketing content for:
    Product: {product}
    Target Audience: {audience}
    
    Generate:
    1. 3 compelling headline variations
    2. 3 different ad copy variations (short form)
    3. 1 long-form marketing description
    4. Key messaging themes
    5. Call-to-action suggestions
    
    Make it persuasive and conversion-focused.
    """,
    agent=content_agent,
    expected_output="Multiple content variations with headlines, ad copy, and messaging strategies optimized for conversions."
)

# Run test
print("✨ Testing Content Agent...")
print("=" * 50)

crew = Crew(agents=[content_agent], tasks=[content_task], verbose=True)
result = crew.kickoff()

print("\n" + "=" * 50) 
print("✅ Content Agent Results:")
print("=" * 50)
print(result)