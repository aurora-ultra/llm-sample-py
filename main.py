import json
import logging

from openai import OpenAI
from lib import funcs

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

client = OpenAI(
    api_key="",
    base_url="",
)


def call_model(messages, tools):
    logging.info("message = %s", messages)
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        tools=tools
    )
    return completion


def call_tools(messages, completion):
    if completion.choices[0].message.tool_calls is not None:
        messages.append(completion.choices[0].message)
        for tool_call in completion.choices[0].message.tool_calls:
            func_name = tool_call.function.name
            func_args = json.loads(tool_call.function.arguments)
            func_result = funcs.dispatch(func_name, func_args)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(func_result)
            })
    return messages


# messages = [
    # {"role": "user", "content": "东京昨天天气如何？ 是否影响了我们的苹果手机销量，和上个月相比的话有什么变化吗？请用HTML的形式告诉我。"}]
# messages = [{"role": "user", "content": "每天上午8点给我推送国际新闻"}]
messages = [{"role": "user", "content": "昨天大连天气如何？"}]
# messages = [{"role": "user", "content": "帮我给客厅的灯关掉"}]

completion = call_model(messages=messages, tools=funcs.tools)
messages = call_tools(messages=messages, completion=completion)
completion = call_model(messages=messages, tools=funcs.tools)

print(completion.choices[0].message.content)
