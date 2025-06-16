from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# from study_crew_v2.config import agents_config, tasks_config

from study_crew_v2.config.llm_loader import get_azure_llm
azure_llm = get_azure_llm()

from study_crew_v2.tools.extraction_tool import extract_tool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class StudyCrewV2():
    """StudyCrewV2 crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

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
    def summarizer_agent(self) -> Agent:
        """Agent to summarize text."""
        return Agent(
            config=self.agents_config['summarizer_agent'], # type: ignore[index]
            llm=azure_llm,
            verbose=True
        )

    # @agent
    # def researcher(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['researcher'], # type: ignore[index]
    #         llm=azure_llm,
    #         verbose=True
    #     )

    # @agent
    # def reporting_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['reporting_analyst'], # type: ignore[index]
    #         llm=azure_llm,
    #         verbose=True
    #     )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def pdf_extraction_task(self) -> Task:
        """Task to extract text from PDF documents."""
        return Task(
            config=self.tasks_config['pdf_extraction_task'], # type: ignore[index]
        )

    @task
    def summarization_task(self) -> Task:
        """Task to summarize text."""
        return Task(
            config=self.tasks_config['summarization_task'], # type: ignore[index]
            output_file='summary.md'
        )

    # @task
    # def research_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['research_task'], # type: ignore[index]
    #     )

    # @task
    # def reporting_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['reporting_task'], # type: ignore[index]
    #         output_file='report.md'
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the StudyCrewV2 crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
