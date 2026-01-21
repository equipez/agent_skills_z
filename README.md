# Equipe Z - Agent Skills Library 🧠

Welcome to **Equipe Z's Agent Skills**, a lightweight, pragmatic collection of "soft skills" and tools designed to enhance AI Agents (like GitHub Copilot or ChatGPT).

## 📖 Philosophy
We believe that for small teams, **Context is the best Code**.
Instead of building complex Agent orchestration frameworks, we define **Skills** as folders containing specific instructions (System Prompts) and executable tools.

## 📂 Repository Structure
The repository is organized by **Skills**. Each folder represents a standalone capability that can be "installed" into an AI session.

```text
root/
├── [Skill Name]/               # Example: "Code_Reviewer", "Data_Analyst"
│   ├── [skill_name].md         # THE CORE: The Prompt, Persona, and Strict Rules.
│   └── [supporting_files]      # Python scripts, reference docs, or templates.
```

### Components of a Skill
1.  **The Manifesto (`.md`)**: A Markdown file defining the Agent's persona, strict rules, and operational workflow.
2.  **The Toolkit**: Helper scripts (e.g., `bibtex_formatter.py`) that the Agent can read to understand how to execute specific tasks.

## 🚀 How to Use

### Method 1: The "VS Code Workspace" Workflow (Recommended) ⭐
This method turns your editor into a powerful, context-aware Agent platform.

1.  **Clone** this repository to your local machine.
2.  **Add** this folder to your current VS Code Workspace.
    *   *File -> Add Folder to Workspace...*
3.  **Summon** the Skill in your AI Chat (e.g., Copilot Chat):
    *   Simply type `@` followed by the skill's filename.
    *   *Example:* `@code_review.md Please review the currently open file.`

### Method 2: The Direct Feed
If you are using a web-based chat model (ChatGPT, Claude):

1.  Open the folder of the skill you want to use.
2.  **Drag and Drop** the `.md` file and any script files into the chat context.
3.  The AI will instantly adopt the persona and understand the available tools.

---
*Equipe Z Agent Skills - A Shared Library for AI Context & Tools.*
