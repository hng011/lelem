# FOR OPENAI
book_location_function = {
    "name": "get_book_location",
    "description": "Get the location of a book. Call this whenever you need to know where is the location of the book, for example when a visitor asks where is a book of book's name",
    "parameters": {
        "type": "object",
        "properties": {
            "book_name": {
                "type": "string",
                "description": "The location of the book"
            },
        },
        "required": ["book_name"],
        "additionalProperties": False   
    },
    "strict": True
}

openai_tool_functions = [{
    "type": "function",
    "function": book_location_function
}]