from langchain.tools import structured_tool as tool
from pathlib import Path
import fitz  # PyMuPDF

def extract_all_pdfs_from_knowledge() -> str:
    knowledge_path = Path("knowledge")
    if not knowledge_path.exists():
        return "The knowledge folder does not exist."

    pdf_files = list(knowledge_path.glob("*.pdf"))
    if not pdf_files:
        return "No PDF files found in the knowledge folder."

    combined_text = ""

    for pdf_file in pdf_files:
        try:
            doc = fitz.open(pdf_file)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()

            combined_text += f"\n\n--- {pdf_file.name} ---\n\n" + text.strip()

        except Exception as e:
            combined_text += f"\n\n[Error reading {pdf_file.name}]: {str(e)}"

    return combined_text.strip()

extract_tool = StructuredTool.from_function(
    func=extract_all_pdfs_from_knowledge,
    name="extract_text",
    description="Extracts plain text from all PDF files in the knowledge folder."
)
