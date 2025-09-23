import dotenv

dotenv.load_dotenv()

from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class NewsReaderAgent:
    @agent
    def news_reader(self):
        return Agent(
            config=self.agents_config["news_reader"]
        )
    
    @task
    def read_news(self):
        return Task(
            config=self.tasks_config["read_news"]
        )

    @crew
    def news_reader_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )

NewsReaderAgent().news_reader_crew().kickoff(
    inputs={"sentence":"지난 10년간의 데이터를 분석"}
)