from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents.resume_agent import analyze_resume
from agents.skill_gap_agent import analyze_skill_gap
from agents.roadmap_agent import generate_roadmap
from agents.interview_agent import generate_interview_questions
from agents.rewrite_agent import rewrite_resume
from agents.project_agent import recommend_projects
from agents.career_agent import advise_career
from agents.cover_letter_agent import generate_cover_letter
from agents.job_fit_agent import score_job_fit
from agents.salary_agent import negotiate_salary

class AgentState(TypedDict):
    resume_text: str
    target_role: str
    job_description: str
    selected_feature: str
    final_response: str

def resume_node(state: AgentState):
    response = analyze_resume(state["resume_text"])
    return {"final_response": response}

def skill_gap_node(state: AgentState):
    response = analyze_skill_gap(state["resume_text"], state["target_role"])
    return {"final_response": response}

def roadmap_node(state: AgentState):
    response = generate_roadmap(state["resume_text"], state["target_role"])
    return {"final_response": response}

def interview_node(state: AgentState):
    response = generate_interview_questions(state["resume_text"], state["target_role"])
    return {"final_response": response}

def rewrite_node(state: AgentState):
    response = rewrite_resume(state["resume_text"])
    return {"final_response": response}

def project_node(state: AgentState):
    response = recommend_projects(state["resume_text"], state["target_role"])
    return {"final_response": response}

def career_node(state: AgentState):
    response = advise_career(state["resume_text"], state["target_role"])
    return {"final_response": response}

def cover_letter_node(state: AgentState):
    response = generate_cover_letter(state["resume_text"], state["job_description"])
    return {"final_response": response}

def job_fit_node(state: AgentState):
    response = score_job_fit(state["resume_text"], state["target_role"], state["job_description"])
    return {"final_response": response}

def salary_node(state: AgentState):
    response = negotiate_salary(state["resume_text"], state["target_role"])
    return {"final_response": response}

def route_request(state: AgentState):
    feature = state["selected_feature"]
    if feature == "Resume Analyzer":
        return "resume_node"
    elif feature == "Skill Gap Analysis":
        return "skill_gap_node"
    elif feature == "Learning Roadmap":
        return "roadmap_node"
    elif feature == "Interview Prep":
        return "interview_node"
    elif feature == "Resume Rewrite":
        return "rewrite_node"
    elif feature == "Project Recommendations":
        return "project_node"
    elif feature == "Career Advice":
        return "career_node"
    elif feature == "Cover Letter Generator":
        return "cover_letter_node"
    elif feature == "Job Fit Scorer":
        return "job_fit_node"
    elif feature == "Salary Negotiation":
        return "salary_node"
    else:
        return END

def build_graph():
    """
    Builds the LangGraph supervisor workflow.
    """
    workflow = StateGraph(AgentState)
    
    workflow.add_node("resume_node", resume_node)
    workflow.add_node("skill_gap_node", skill_gap_node)
    workflow.add_node("roadmap_node", roadmap_node)
    workflow.add_node("interview_node", interview_node)
    workflow.add_node("rewrite_node", rewrite_node)
    workflow.add_node("project_node", project_node)
    workflow.add_node("career_node", career_node)
    workflow.add_node("cover_letter_node", cover_letter_node)
    workflow.add_node("job_fit_node", job_fit_node)
    workflow.add_node("salary_node", salary_node)
    
    workflow.set_conditional_entry_point(
        route_request,
        {
            "resume_node": "resume_node",
            "skill_gap_node": "skill_gap_node",
            "roadmap_node": "roadmap_node",
            "interview_node": "interview_node",
            "rewrite_node": "rewrite_node",
            "project_node": "project_node",
            "career_node": "career_node",
            "cover_letter_node": "cover_letter_node",
            "job_fit_node": "job_fit_node",
            "salary_node": "salary_node",
            END: END
        }
    )
    
    workflow.add_edge("resume_node", END)
    workflow.add_edge("skill_gap_node", END)
    workflow.add_edge("roadmap_node", END)
    workflow.add_edge("interview_node", END)
    workflow.add_edge("rewrite_node", END)
    workflow.add_edge("project_node", END)
    workflow.add_edge("career_node", END)
    workflow.add_edge("cover_letter_node", END)
    workflow.add_edge("job_fit_node", END)
    workflow.add_edge("salary_node", END)
    
    return workflow.compile()
