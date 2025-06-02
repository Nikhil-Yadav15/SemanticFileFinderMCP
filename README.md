# 🚀 MCP Claude Integration

This project showcases how to integrate the **Modular Command Platform (MCP)** with **Claude Desktop**, providing two smart tools:

1. 🔍 `search_file_by_name` – Uses semantic similarity to locate files on a given disk.
2. 💽 `list_drives` – Lists all available drives on your system.

---

## ✨ Features

* 🧠 **Semantic Search** – Powered by `sentence-transformers`, it finds files whose names are close to your hint.
* 🗂️ **Disk Scanning** – Search within specific folders or the entire disk.
* 🛠️ **Modular Tooling** – Uses MCP’s `@tool` decorator for clean, extensible design.

---

## ⚙️ Setup Instructions

### 📋 Prerequisites

* Install dependencies using [`uv`](https://github.com/astral-sh/uv):

```bash
uv init
uv add sentence-transformers
```

### 🗃️ Project Structure

```bash
project_root/
├── main.py  # Contains the MCP tools
```

### ▶️ Running the Integration

To install the MCP server into Claude Desktop:

```bash
uv run mcp install main.py
```

Make sure `main.py` is present and MCP initializes the tools successfully.

---

## 🧰 Tool Descriptions

### 🔍 `search_file_by_name`

**Purpose**: Find files of a specified type on a given disk—optionally within certain folders—based on name similarity.

**Inputs:**

* `disk` (str): Disk to search (e.g., `C`, `D`, `E`).
* `file_type` (str): File type/extension (e.g., `pdf`, `txt`).
* `name_hint` (str): A name hint to match against (e.g., `environment`).
* `folders` (list, optional): Specific folders to narrow the search.

**Output:**
Top 5 most relevant file paths, or a message if no matches are found.

### 💽 `list_drives`

**Purpose**: Display all available disk drives.

**Output:**
List of drives, or a message if none are found.

