# AI Career Mentor Agent

An intelligent, multi-agent AI system built to help students and job seekers improve their careers using Generative AI. 
This project leverages LangGraph, Google Gemini 2.5 Flash, and Streamlit to provide personalized career guidance.

🚀 **Live Demo:** [https://aicareer-mentor-agent-9od8ktqtq8uywntsqn5nsb.streamlit.app/](https://aicareer-mentor-agent-9od8ktqtq8uywntsqn5nsb.streamlit.app/)



## Features

- **Resume Upload**: Upload PDF resumes, extract and clean text for analysis.
- **Resume Analyzer Agent**: Identifies strengths, weaknesses, ATS friendliness, grammar, formatting, and missing keywords.
- **Skill Gap Agent**: Compares user skills with target roles (e.g., AI Engineer, Data Scientist) and recommends technologies and certifications.
- **Learning Roadmap Agent**: Generates an 8-week personalized learning roadmap with topics, resources, and practice tasks.
- **Interview Agent**: Generates HR, Technical, Coding, Behavioral, and System Design questions with model answers.
- **Resume Rewrite Agent**: Re-writes summary, projects, and experience sections to improve ATS score.
- **Project Recommendation Agent**: Suggests beginner to advanced projects with required skills and estimated duration.
- **Career Advice Agent**: Recommends job roles, salary expectations, and future learning priorities.

## Architecture

This application employs a Multi-Agent architecture using **LangGraph**. A **Supervisor Agent** acts as a router, directing the user's request and context to the specialized agents:
- Resume Agent
- Skill Gap Agent
- Roadmap Agent
- Interview Agent
- Resume Rewrite Agent
- Project Recommendation Agent
- Career Advisor Agent

The application uses **FAISS** for storing vector embeddings of resumes and learning resources, enabling Retrieval-Augmented Generation (RAG).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/career-mentor-agent.git
   cd career-mentor-agent
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Copy `.env.example` to `.env` and add your Google Gemini API key:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and set: `GEMINI_API_KEY=your_api_key_here`

## Usage

Start the Streamlit application:
```bash
streamlit run app.py
```

Upload your resume from the sidebar, select your target role, and interact with the various AI agents using the feature tabs in the dashboard.

## Folder Structure

```
career_mentor_agent/
│
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .env.example             # Environment variables template
│
├── agents/                  # LangGraph agents
│   ├── supervisor.py        # LangGraph workflow orchestration
│   ├── resume_agent.py      # Resume analysis
│   ├── skill_gap_agent.py   # Skill comparison
│   ├── roadmap_agent.py     # Roadmap generation
│   ├── interview_agent.py   # Interview prep
│   ├── rewrite_agent.py     # Resume improvement
│   ├── project_agent.py     # Project ideas
│   └── career_agent.py      # Career guidance
│
├── tools/                   # Helper tools for agents
│   ├── pdf_reader.py        # PDF extraction
│   ├── gemini_client.py     # LLM initialization
│   ├── embeddings.py        # Vector embeddings
│   ├── vector_store.py      # FAISS operations
│   ├── resume_parser.py     # Structured parsing
│   └── prompts.py           # Agent prompt templates
│
├── utils/                   # Shared utilities
│   ├── helpers.py           # UI and text helpers
│   └── constants.py         # App configuration
│
└── data/                    # Vector store and static resources
    └── resources/
```

## Screenshots Placeholder
*(Add screenshots of your Streamlit UI here)*

## Future Improvements
- Integration with LinkedIn API for real-time job matching.
- Adding a mock interview audio mode (Speech-to-Text).
- Cloud database (Pinecone/Weaviate) for persistent cross-session storage.

## License
MIT License
