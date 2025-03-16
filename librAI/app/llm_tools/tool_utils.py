import json
import os
from pathlib import Path 


def get_book_location(book_name: str):
    base = Path(__file__).resolve().parent
    book_loc_path = base / "book_location.json"
    book_name = book_name.lower()
    
    # print(base)
    # print(book_loc_path)
    
    with open(book_loc_path, "r") as f:
        if os.path.getsize(book_loc_path) > 0:
            book_location = json.load(f)
        else:
            print("The file is Empty")
    
    print(f"Tool get_book_location called for {book_name}")
    
    matched_book = {key.lower():value for key, value in book_location.items()}
    
    return matched_book.get(book_name, "Unknown")


def handle_tool_call(msg) -> dict:
    tool_call = msg.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    book_name = args.get("book_name")
    book_location = get_book_location(book_name)
    
    return {
        "role": "tool",
        "content": json.dumps({"book_name": book_name, "book_location": book_location}),
        "tool_call_id": tool_call.id
    }
    

# print(get_book_location("Sherlock Holmes"))
# print(get_book_location("Sherlock Holmes".lower()))