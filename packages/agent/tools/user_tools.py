
def Write_to_file(topic: str, file_name: str, file_content) -> str:
    """Create MarkDown or Text file with notes based on what context was given."""

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(file_content)

    return f"File created for {topic}, with name: {file_name}"
