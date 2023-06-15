from autochain.chain.chain import Chain
from autochain.memory.buffer_memory import BufferMemory
from autochain.models.chat_openai import ChatOpenAI
from autochain.tools.base import Tool
from autochain.agent.conversational_agent.conversational_agent import (
    ConversationalAgent,
)

llm = ChatOpenAI(temperature=0)
tools = [
    Tool(
        name="Get weather",
        func=lambda *args, **kwargs: "Today is a sunny day",
        description="""This function returns the weather information""",
    )
]

memory = BufferMemory()
agent = ConversationalAgent.from_llm_and_tools(llm=llm, tools=tools)
chain = Chain(agent=agent, memory=memory)

print(chain.run("what is the weather today")["message"])
