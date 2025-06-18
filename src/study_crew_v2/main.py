import sys
import warnings

from datetime import datetime

from study_crew_v2.crew import StudyCrewV2
from study_crew_v2.tools.extraction_tool import extract_tool

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from study_crew_v2.crew import StudyCrewV2

if __name__ == "__main__":
    crew_instance = StudyCrewV2()
    result = crew_instance.crew().kickoff()
    print("\n📝 Final Output:\n")
    print(result)

def run():
    try:
        StudyCrewV2().crew().kickoff()

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        StudyCrewV2().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        StudyCrewV2().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        StudyCrewV2().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
