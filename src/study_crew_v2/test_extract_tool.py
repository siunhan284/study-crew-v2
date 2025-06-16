from study_crew_v2.tools import tools

if __name__ == "__main__":
    # Replace with an actual PDF filename inside your knowledge folder
    file_name = "study.pdf"

    result = tools["extract_tool"]().run(file_name)

    print("\n--- Extracted Text ---\n")
    print(result[:2000])  # Print first 2000 characters only to avoid overload
