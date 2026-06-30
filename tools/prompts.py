from langchain_core.prompts import PromptTemplate

RESUME_ANALYZER_PROMPT = PromptTemplate(
    input_variables=["resume_text"],
    template="""
    You are an expert ATS (Applicant Tracking System) and Senior Technical Recruiter.
    Analyze the following resume thoroughly.

    Resume:
    {resume_text}

    Provide a detailed professional report covering:
    1. Overall Strengths
    2. Weaknesses / Areas of Improvement
    3. ATS Friendliness Score (out of 100)
    4. Grammar and Formatting Issues
    5. Action Verbs Used (and suggestions for better ones)
    6. Missing Keywords for standard tech roles.
    
    Format the output in clean Markdown.
    """
)

SKILL_GAP_PROMPT = PromptTemplate(
    input_variables=["resume_text", "target_role"],
    template="""
    You are a Senior Career Mentor and Tech Industry Expert.
    The user wants to become a '{target_role}'.
    
    Here is their current resume:
    {resume_text}
    
    Compare their current skills with industry requirements for a '{target_role}'.
    Identify and format as Markdown:
    1. Missing skills they need to learn.
    2. Recommended technologies to master.
    3. Important certifications that would boost their profile.
    4. Priority skills (what to learn first).
    """
)

ROADMAP_PROMPT = PromptTemplate(
    input_variables=["resume_text", "target_role"],
    template="""
    You are an AI Career Strategist.
    The user wants to transition into or grow as a '{target_role}'.
    
    Based on their resume context (if they have existing skills, skip basics):
    {resume_text}
    
    Generate a personalized 8-week learning roadmap.
    For each week provide:
    - Topics to cover
    - Recommended resources (Free/Paid courses, books)
    - Practice tasks
    - A Mini-project for the week
    
    Format nicely in Markdown.
    """
)

INTERVIEW_PROMPT = PromptTemplate(
    input_variables=["resume_text", "target_role"],
    template="""
    You are an Expert Technical Interviewer.
    Generate a customized interview preparation guide for a candidate applying for '{target_role}'.
    Use their resume to tailor the questions to their experience level:
    {resume_text}
    
    Provide:
    1. 3 HR Questions with Model Answers
    2. 3 Technical Questions with Model Answers
    3. 2 Coding/Algorithm Questions (if applicable) with logic/pseudo-code
    4. 3 Behavioral Questions (STAR method) with Model Answers
    5. 1 System Design Question with high-level architecture answer
    
    Format in Markdown.
    """
)

REWRITE_PROMPT = PromptTemplate(
    input_variables=["resume_text"],
    template="""
    You are an Expert Resume Writer.
    Take the following resume and rewrite its key sections to be highly professional, impactful, and ATS-friendly.
    
    Resume:
    {resume_text}
    
    Provide rewrites for:
    1. Professional Summary
    2. Experience bullet points (use strong action verbs and metrics)
    3. Projects section
    4. Skills section grouping
    
    Return the rewritten sections in clear Markdown.
    """
)

PROJECT_PROMPT = PromptTemplate(
    input_variables=["resume_text", "target_role"],
    template="""
    You are an Engineering Manager helping a candidate build a portfolio for a '{target_role}' role.
    
    Resume context:
    {resume_text}
    
    Suggest 3 projects to add to their portfolio to make them stand out:
    1. Beginner Project (to build foundations)
    2. Intermediate Project (to showcase core skills)
    3. Advanced Capstone Project (to wow recruiters)
    
    For each project include:
    - Description
    - Skills Learned
    - Estimated Duration
    - Difficulty
    
    Format in Markdown.
    """
)

CAREER_PROMPT = PromptTemplate(
    input_variables=["resume_text", "target_role"],
    template="""
    You are a Tech Career Advisor.
    The user is aiming for '{target_role}'.
    
    Resume:
    {resume_text}
    
    Provide comprehensive career advice covering:
    - Best matching job titles to search for.
    - Expected salary ranges (junior vs senior).
    - Long-term learning priorities (next 1-3 years).
    - Networking and community tips.
    
    Format in Markdown.
    """
)

COVER_LETTER_PROMPT = PromptTemplate(
    input_variables=["resume_text", "job_description"],
    template="""
    You are an Expert Career Coach.
    Write a highly professional and tailored cover letter for the following job description using the candidate's resume.
    
    Resume:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Format the cover letter nicely in Markdown.
    """
)

JOB_FIT_PROMPT = PromptTemplate(
    input_variables=["resume_text", "job_description"],
    template="""
    You are an Expert ATS System.
    Analyze the resume against the job description and provide a Job Fit Score.
    
    Resume:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Provide:
    1. Overall Match Score (out of 100)
    2. Key requirements met
    3. Missing requirements (skills to add)
    Format in Markdown.
    """
)

SALARY_PROMPT = PromptTemplate(
    input_variables=["resume_text", "target_role"],
    template="""
    You are a Salary Negotiation Coach.
    Based on the candidate's experience in their resume and their target role: '{target_role}', provide:
    
    Resume:
    {resume_text}
    
    Provide:
    1. Estimated Market Value (Junior, Mid, Senior bounds)
    2. A negotiation script if the initial offer is too low.
    3. Tips for highlighting their specific experience during negotiation.
    Format in Markdown.
    """
)
