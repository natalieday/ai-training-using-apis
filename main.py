from markdown_parser import extract_qa_from_md
from openai_integration import get_question_variations
from personal_ai_integration import stack_memory

def process_markdown_and_stack(file_path):
    qa_pairs = extract_qa_from_md(file_path)

    for question, answer in qa_pairs[:3]:
        print(f"Processing: {question}")
        variations = get_question_variations(question)
        
        for variation in variations:
            status, response = stack_memory(variation, answer)
            print(f"Stacked: {variation} | Status: {status}")

# Run the script
process_markdown_and_stack("questions.md")
