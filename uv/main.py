from dotenv import load_dotenv
import os
from agents import Agent,Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agents = Agent(
    name = "translator",
    instructions = "you are a helpful translator.Always translate urdu sentences into clear and simple arabic.   "
)
response = Runner.run_sync(
    agents,
    input = "   میرا نام ندا خان ہے۔ میں جی آئی اے آئی سی کی طالبہ ہوں۔",
    run_config = config
)
print(response)
