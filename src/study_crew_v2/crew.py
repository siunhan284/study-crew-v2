from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from study_crew_v2.config.llm_loader import get_azure_llm
azure_llm = get_azure_llm()

from study_crew_v2.tools.extraction_tool import extract_tool

@CrewBase
class StudyCrewV2():
    """StudyCrewV2 crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def pdf_extractor_agent(self) -> Agent:
        """Agent to extract text from PDF documents."""
        return Agent(
            config=self.agents_config['pdf_extractor_agent'], # type: ignore[index]
            llm=azure_llm,
            tools=[extract_tool],
            verbose=True
        )

    @agent
    def summariser_agent(self) -> Agent:
        """Agent to summarise text."""
        return Agent(
            config=self.agents_config['summariser_agent'], # type: ignore[index]
            llm=azure_llm,
            verbose=True
        )

    @task
    def pdf_extraction_task(self) -> Task:
        """Task to extract text from PDF documents."""
        return Task(
            config=self.tasks_config['pdf_extraction_task'], # type: ignore[index]
        )

    @task
    def summarisation_task(self) -> Task:
        """Task to summarise text."""
        return Task(
            config=self.tasks_config['summarisation_task'], # type: ignore[index]
            output_file='summary.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the StudyCrewV2 crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
