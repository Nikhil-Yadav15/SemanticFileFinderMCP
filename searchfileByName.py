from mcp.server.fastmcp import FastMCP
import os
from sentence_transformers import SentenceTransformer, util

mcp = FastMCP("SearchFileByName", dependencies=["sentence_transformers"])

model = SentenceTransformer('all-MiniLM-L6-v2')
@mcp.tool(description="Find files of a specified type on a given disk, either within a specified folder or anywhere on the disk, whose names are similar to a provided hint. Example: 'Find a PDF file on disk P with a name similar to environment, 'Find a PDF file on disk P in the Notes folder with a name similar to environment")
def search_file_by_name(disk: str, file_type: str, name_hint: str, folders: list = None) -> str:
    """Search for files on the specified disk by file type and name similarity."""
    root_path = os.path.expanduser("~") if disk.upper() == 'C' else f"{disk.upper()}:\\"
    extension = f".{file_type.lower()}"
    matches = []

    if folders:
        for folder in folders:
            folder_path = os.path.join(root_path, folder)
            for dirpath, _, filenames in os.walk(folder_path):
                for filename in filenames:
                    if filename.lower().endswith(extension):
                        emb_filename = model.encode(filename.split('.')[0].lower(), convert_to_tensor=True)
                        emb_hint = model.encode(name_hint.lower(), convert_to_tensor=True)
                        similarity = util.pytorch_cos_sim(emb_filename, emb_hint).item()
                        score = round(similarity * 100)
                        if score >= 50:
                            full_path = os.path.join(dirpath, filename)
                            matches.append((full_path, score))
    else:
        for dirpath, _, filenames in os.walk(root_path):
            for filename in filenames:
                if filename.lower().endswith(extension):
                    emb_filename = model.encode(filename.split('.')[0].lower(), convert_to_tensor=True)
                    emb_hint = model.encode(name_hint.lower(), convert_to_tensor=True)
                    similarity = util.pytorch_cos_sim(emb_filename, emb_hint).item()
                    score = round(similarity * 100)
                    if score >= 40:
                        full_path = os.path.join(dirpath, filename)
                        matches.append((full_path, score))

    if not matches:
        return "No files found matching the criteria."
    else:
        to_show = []
        matches.sort(key=lambda x: x[1], reverse=True)
        top_matches = matches[:5]
        
        for path, _ in top_matches:
            to_show.append(path)
        return to_show


@mcp.tool(description="List all available disk drives on the system.")
def list_drives() -> str:
    """Return a list of available disk drives."""
    drives = [f"{chr(d)}:" for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")]
    return "\n".join(drives) if drives else "No drives available."