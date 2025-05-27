import asyncio

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from browser_use import Agent

load_dotenv()

llm = ChatOllama(model='qwen3:8b', base_url='http://localhost:11434')

website = 'https://xchux.github.io/Resume/'

# https://github.com/browser-use/awesome-prompts?tab=readme-ov-file
task = f"""
Test the entire user registration flow on {website} to identify any usability issues or bugs.

1. Navigate to {website}
2. Test the following registration methods:
   - Verify the resume page loads correctly.
   - Validate resume content accuracy, Cross-check details against the resume owner’s LinkedIn/profile.
   - Test anchor links (if applicable), Check if the page scrolls to the correct section.
   - Verify links (e.g., LinkedIn, GitHub) work correctly.

Provide a detailed report with screenshots of any issues found, along with severity ratings and suggestions for improvement.
"""

# task = """
# 1. Go to https://www.reddit.com/.
# 2. If any pop up, close them.
# 3. Typing 'browser use' in the search input and search. 
# 4. Get the first post url.
# """

async def run_search():
	agent = Agent(
		task=task,
		llm=llm,
		use_vision=True,
		max_failures=2,
		max_actions_per_step=3,
	)

	await agent.run(
		max_steps=25,
	)


if __name__ == '__main__':
	asyncio.run(run_search())
