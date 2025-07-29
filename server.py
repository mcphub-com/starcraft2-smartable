import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/SmartableAI/api/starcraft2-smartable'

mcp = FastMCP('starcraft2-smartable')

@mcp.tool()
def get_sponsorships() -> dict: 
    '''Get StarCraft 2 sponsorships.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/sponsorships/today/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_topics() -> dict: 
    '''Get StarCraft 2 topics.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/topics/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_games(page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get StarCraft 2 gameplays.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/games/page/1/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_games_by_topic(topic: Annotated[str, Field(description='')],
                       page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get StarCraft 2 gameplays by topic.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/games/zerg/page/1/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'topic': topic,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_game_collections(page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get game collections'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/games/collections/page/1/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_guides(page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get StartCraft 2 guides and tutorials.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/learning/page/1/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_guides_by_topic(topic: Annotated[str, Field(description='')],
                        page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get StarCraft 2 guides & tutorials by topic.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/learning/zerg/page/1/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'topic': topic,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_news(page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get StarCraft 2 news.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/news/page/1/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_news_by_topic(topic: Annotated[str, Field(description='')],
                      page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get StarCraft 2 news by topic.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/news/zerg/page/1/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'topic': topic,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_people(page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get StarCraft 2 top players, influencers and celebrities.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/people/page/1/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_people_by_topic(topic: Annotated[str, Field(description='')],
                        page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''Get StarCraft 2 top players, influencers and celebrities by topic.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/people/zerg/page/1/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'topic': topic,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_newsletters() -> dict: 
    '''Get StarCraft 2 newsletters.'''
    url = 'https://starcraft2-smartable.p.rapidapi.com/newsletters/'
    headers = {'x-rapidapi-host': 'starcraft2-smartable.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
