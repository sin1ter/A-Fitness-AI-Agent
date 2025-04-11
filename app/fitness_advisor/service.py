from pydantic_ai import Agent, RunContext, capture_run_messages
from app.fitness_advisor.models import FitnessProfile, FitnessReportResult

from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

fitness_agent = Agent(
    'gpt-3.5-turbo', 
    deps_type=FitnessProfile,
    result_type=FitnessReportResult,
    result_retries=3,
    system_prompt = "Create personalized FitnessReportResult base on user's information provided."
    "for motivational quates call the get_motivation tool and pic the single best one from the list"
)

motivational_agent = Agent(
    'gpt-3.5-turbo', 
    result_type = list[str],
    system_prompt="Give motivational quotes based on the user's fitness goals and current status."
)

@fitness_agent.system_prompt
async def add_user_fitness_data(ctx: RunContext[FitnessProfile])->str:
    fitness_data = ctx.deps
    return f"User fitness profile and goals: {fitness_data!r}"

@fitness_agent.tool
async def motivation(ctx: RunContext)->list[str]:
    return await motivational_agent(
        f"Please generate 5 motivational quotes about working out and eating healhy"
    )


async def analyze_profile(profile: FitnessProfile) -> FitnessProfile:
    result = await fitness_agent.run("Create a personalized fitness and nutrition plan.", deps=profile)
    return result.data