from crewai import Crew, Agent

class ResearcherAgent(Agent):
    def run(self, input_data):
        # minimal: return a task to download a URL and ingest
        return {"action": "download_and_ingest", "url": input_data.get("url")}

crew = Crew("research-crew", agents=[ResearcherAgent("researcher")])

if __name__ == '__main__':
    out = crew.run({"url": "https://arxiv.org/pdf/2306.03672.pdf"})
    print(out)
