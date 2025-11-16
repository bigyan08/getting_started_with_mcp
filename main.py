from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP('AI Sticky Notes')

NOTES_FILE = os.path.join(os.path.dirname(__file__),"notes.txt")

def ensure_file():
    '''
    Ensure the file exists. If not then creates a file.
    '''
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE,"w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str:
    '''
    Append a new note to the sticky note file.

    Args:
        message(str) : The note content to be added.
    
    Returns:
        str: Confirmation message for adding the note.

    '''
    ensure_file()
    with open(NOTES_FILE,"a") as f:
        f.write(message + '\n')
    return "NOTE SAVED!"


@mcp.tool()
def read_note() -> str:
    '''
    Read the contents of the note file.

    Args: None

    Returns:
        str: Contents of the note file. 
    '''
    ensure_file()
    with open(NOTES_FILE,'r') as f:
        contents = f.read().strip()
    return contents or "No notes yet."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    '''
    Read the contents of the last line of note file and display.

    Args: None

    Returns:
        str: Contents of the latest note. 
    '''
    ensure_file()
    with open(NOTES_FILE,'r') as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."


@mcp.prompt()
def note_summary_prompt() ->str:
    '''
    Read the contents of the note file and generate a summary.

    Args: None

    Returns:
        str: Summary of all notes. 
    '''
    ensure_file()
    with open(NOTES_FILE,'r') as f:
        contents = f.read().strip()
    if not contents:
        return "There are no notes yet."
    
    return f"Summarize the current notes:{contents}"
