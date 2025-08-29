from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="Summarize the research paper '{paper}' in a {style} style with a {length} length.",
    input_variables=["paper", "style", "length"],
    validate_template=True
)

template.save('template.json')