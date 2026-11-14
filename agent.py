# from agno.agent import Agent
# # from agno.models.openai import OpenAIResponses
# from agno.models.groq import Groq
# from dotenv import load_dotenv

# from agno.tools.duckduckgo import DuckDuckGoTools
# from agno.tools.yfinance import YFinanceTools
# from agno.tools.hackernews import HackerNewsTools
# from agno.tools.file import FileTools

# load_dotenv()

# def build_agent():
#     return Agent(
#         model=Groq(id="openai/gpt-oss-120b"),
#         # tools=[YFinanceTools(), DuckDuckGoTools()],
#         # markdown=True,
#         # add_datetime_to_context=True,
#         # description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
#         # instructions=["Use given tools whenever possible. Format your response using markdown and use tables to display data where possible."],
#         # debug_mode=True

#         tools=[HackerNewsTools()],
#         instructions="Write a report on the topic. Output only the report.",
#         markdown=True,
#     )



# agent = build_agent()
# agent.print_response("Trending startups and products.", stream=True) # for hackernnews
# agent.print_response("Share the MSFT stock price and analyst recommendationss") # for yfinance



from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

from agno.tools.file import FileTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.local_file_system import LocalFileSystemTools
from agno.tools.youtube import YouTubeTools


load_dotenv()

# agent = Agent(
#     model=Groq(id="openai/gpt-oss-120b"),
#     tools=[DuckDuckGoTools(), FileTools()],
#     markdown=True,
#     # show_tool_calls=True
# )

# agent.print_response(
#     "What is the most advanced LLM currently? Save the answer to a file."
# )

# agent = Agent(
#     model=Groq(id="openai/gpt-oss-120b"),
    # instructions=[
    #     "You are a file management assistant that helps save content to local files",
    #     "Create files with appropriate names and extensions",
    #     "Organize files in the specified directory structure",
    #     "Provide clear feedback about file operations",
    # ],
    # tools=[LocalFileSystemTools(target_directory="./output")],
# )

# agent.print_response("Save this meeting summary to a file: 'Discussed Q4 goals and budget allocation'", stream=True)


# ********************** YOUTUBE *****************************

def build_youtube_agent():
    return Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    tools=[YouTubeTools()],
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

# agent.print_response(
#         "Summarize this video https://youtu.be/RNa0Lx4nu80?si=-4nNOM7QPZ2u-g57",
#         markdown=True,
#     )