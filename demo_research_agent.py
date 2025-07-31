"""
Demo: Research Agent Test
Simple test of the market research agent
"""
import os
from crewai import Agent, Task, Crew, LLM

# Setup
api_key = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key

# Create LLM
llm = LLM(model="gemini/gemini-1.5-flash")

# Create research agent
research_agent = Agent(
    llm=llm,
    role="Market Research Specialist",
    goal="Analyze target markets, customer segments, and competitive landscapes to provide actionable insights",
    backstory="""You are a seasoned market researcher with 15 years of experience in digital marketing and 
    consumer behavior analysis. You excel at identifying target audiences, analyzing market trends, and 
    providing strategic insights that drive successful marketing campaigns.""",
    memory=True,
    verbose=True
)

# Sample test data
product = "AI-powered fitness tracker with personalized coaching"
goal = "Launch product and acquire 50,000 users in 6 months"

# Create task
research_task = Task(
    description=f"""
    Analyze the product and marketing goal:
    Product: {product}
    Goal: {goal}
    
    Provide:
    1. Target audience analysis
    2. Market size and opportunity
    3. Competitive landscape
    4. Key market trends
    5. Positioning recommendations
    """,
    agent=research_agent,
    expected_output="Comprehensive market research analysis with target audience insights and strategic recommendations."
)

# Run test
print("🔍 Testing Research Agent...")
print("=" * 50)

crew = Crew(agents=[research_agent], tasks=[research_task], verbose=True)
result = crew.kickoff()

print("\n" + "=" * 50)
print("✅ Research Agent Results:")
print("=" * 50)
print(result)