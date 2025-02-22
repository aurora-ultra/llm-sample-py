import datetime
import logging


def subscribe_news(time, topic):
    return ""


def today():
    return "2025 年 2 月 22 日"


def get_weather(latitude, longitude, date):
    return "16°C"


def statistics_report(month, type):
    return {
        "huawei mate p70": 200000,
        "Apple Model 15": 90000,
    }


def turn_off_light(where):
    return ""


def dispatch(func, args):
    result = None

    if func == "get_weather":
        result = get_weather(args["latitude"], args["longitude"], args['date'])

    if func == "statistics_report":
        result = statistics_report(args["month"], args["type"])

    if func == "turn_off_light":
        result = turn_off_light(args["where"])

    if func == "today":
        result = today()

    logging.info("call func %s with args %s , result is %s",
                 func, args, result)
    return result


tools = [
    {
        "type": "function",
        "function": {
            "name": subscribe_news.__name__,
            "description": "subscribe the news, than the system will push the news on the given time everyday",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "the topic the user wants to subscribe"},
                },
                "required": ["topic"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": subscribe_news.__name__,
            "description": "subscribe the news, than the system will push the news on the given time everyday",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "the topic the user wants to subscribe"},
                },
                "required": ["topic"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": today.__name__,
            "description": "返回今天的日期",
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": turn_off_light.__name__,
            "description": "turn off the light for the user, the light is placed in some places.",
            "parameters": {
                "type": "object",
                "properties": {
                    "where": {"type": "string"},
                },
                "required": ["where"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_weather.__name__,
            "description": "Get current temperature for provided coordinates in celsius.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"},
                    "date": {"type": "string"}
                },
                "required": ["latitude", "longitude", "date"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": statistics_report.__name__,
            "description": "查看指定月份下的产品销量报表",
            "parameters": {
                "type": "object",
                "properties": {
                    "month": {"type": "number"},
                    "type": {"type": "string", "description": "产品类型"}
                },
                "required": ["month", "productType"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]
