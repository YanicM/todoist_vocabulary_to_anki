from todoist_api_python.api import TodoistAPI

API_TOKEN = "<INSERT-YOUR-TOKEN>"  # TODO: Add you REST API token.


def main(my_project_name=None):
    api = TodoistAPI(API_TOKEN)
    projects = api.get_projects()
    for project in projects:
        project_str = str(project)
        if f"name='{my_project_name}'" in project_str:
            start_pos = project_str.index("=")+1
            end_pos = project_str.index(",")
            return project_str[start_pos:end_pos]


if __name__ == "__main__":
    print(main(my_project_name="Vocabulary"))
