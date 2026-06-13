from time import sleep

from app.modules.research.services import generate_queries, search_internet, synthesize_answer
from app.worker import celery_app

@celery_app.task
def start_process_research(topic: str):
    print("Generating queries....")
    queries = generate_queries(topic)

    full_results_content = ""

    for query in queries:
        print("Searching in internet...")
        result = search_internet(query)
        if result is not None:
            full_results_content += result

    print("Synthezing answer")
    raw_report = synthesize_answer(topic, full_results_content)
    if raw_report is None:
        raise ValueError("Fail to synthesize")

    print("Save Report")
    with open("report.md", "w") as file:
        file.write(raw_report)
    