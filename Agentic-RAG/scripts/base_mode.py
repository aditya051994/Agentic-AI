import os
from langchain.tools import tool
import ollama
import requests

@tool
def web_search(query:str):
    '''
    Perform a live web search using Ollama web Search API

    Input:
    As query passing input as string

    Output:
    As output create JSON result with max_result=2
    '''
    response=ollama.web_search(query,max_results=2)
    return response.results

@tool
def weather_api(location:str):
    '''
    create weather api search tool where location is pass
    Input:
    Ex: what is weather of Mumbai?, What is weather of London
    so based on that seelct location and pass as parameter to Url
    Output:
    return response from weather api in JSON format
    '''
    url=f"http://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API_KEY')}&q={location}&aqi=no"
    response=requests.get(url)
    return response.json()