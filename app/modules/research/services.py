from app.modules.research.utils import oai_client
from app.modules.research.utils import tavily_client
from pydantic import BaseModel, Field

class Queries(BaseModel):    
    queries: list[str] = Field(description="The queries to search for")

GENERATE_QUERIES = """
You are expert on researching about certain topics.
And you always suggest with 5 powerful queries i can search in internet.
"""

SUMMARIZE_SYSTEM_PROMPT = """
Summarize the user content and extract following important points:
- Claims
- Date
- Numbers
- Source (Should be link where the claims come from)
"""

SYNTHESIZE_SYSTEM_PROMPT = """
You are a report editor. you have really good skill to create report based on topic.

The output should be include:
- Background research
- Claims, each claim has to citate the web source.
- Conclusion
"""

def generate_queries(topic: str):
    res = oai_client.chat.completions.parse(
        model="gpt-5.4",
        messages=[{
            "role" : "system",
            "content" : GENERATE_QUERIES
        }, {
            "role" : "user",
            "content" : topic
            
        }],
        response_format=Queries
    )

    content = res.choices[0].message.parsed
    if content is None:
        raise ValueError("No queries were generated")
    
    return content.queries

def search_internet(query: str):
    response = tavily_client.search(
        query=query,
        include_answer="advanced",
        search_depth="advanced",
        max_results=5
    )

    answer = response.get("answer") # type: ignore
    results = response.get("results") # type: ignore

    full_text = f"""
        User Original Query: {query}

        Answer from web search: {answer}

        Full raw_results from web_search:
        {results}
    """
    return summarize(full_text)

def summarize(text: str):
    res = oai_client.chat.completions.parse(
        model="gpt-5.4",
        messages=[{
            "role" : "system",
            "content" : SUMMARIZE_SYSTEM_PROMPT
        }, {
            "role" : "user",
            "content" : text
            
        }],       
    )

    content = res.choices[0].message.content
    return content

def synthesize_answer(topic: str, context: str):
    res = oai_client.chat.completions.parse(
        model="gpt-5.4",
        messages=[{
            "role" : "system",
            "content" : SYNTHESIZE_SYSTEM_PROMPT
        }, {
            "role" : "user",
            "content" : f"Topic: {topic}, Context: {context}",
            
        }],       
    )

    content = res.choices[0].message.content
    return content