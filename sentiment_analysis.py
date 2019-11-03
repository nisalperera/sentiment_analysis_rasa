import asyncio
from rasa.core.interpreter import RasaNLUInterpreter

# interpreter = RasaNLUInterpreter("./chatbot/models/nlu/current")

interpreter = RasaNLUInterpreter("./models/nlu/current")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def chat(user_text):
    response = loop.run_until_complete(interpreter.parse(user_text))
    return response['intent']['name']
