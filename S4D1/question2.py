employees = [
    {"name": "John", "skills": ["Python", "Database"], "current_project": None},
    {"name": "Emma", "skills": ["Java", "Testing"], "current_project": None},
    {"name": "Kelly", "skills": ["Python", "Java"], "current_project": None},
]

projects = [
    {"name": "Project A", "required_skills": ["Python", "Database"]},
    {"name": "Project B", "required_skills": ["Java", "Testing"]},
    {"name": "Project C", "required_skills": ["Python", "Java"]},
]

def allocate_projects(employees, projects):
    assignments = []

    for project in projects:
        project_name = project["name"]
        project_skills = set(project["required_skills"])

        for employee in employees:
            employee_name = employee["name"]
            employee_skills = employee["skills"]

            if employee["current_project"] is None and project_skills.issubset(employee_skills):
                employee["current_project"] = project_name
                assignments.append({"employee": employee_name, "project": project_name})
                break 

    return assignments

assignments = allocate_projects(employees, projects)
for assignment in assignments:
    print(assignment)