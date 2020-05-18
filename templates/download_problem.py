import math
import os
import requests

from mako.template import Template
from bs4 import BeautifulSoup

TEMPLATE_PATH = "./templates"
SOLUTION_TEMPLATE_PATH = Template(
    filename=f"{TEMPLATE_PATH}/template_solution.txt",
)
TEST_TEMPLATE_PATH = Template(filename=f"{TEMPLATE_PATH}/template_test.txt")
README_PATH = "./README.md"
README_PROBLEMS = "## Solved Problems"


class Problem:
    def __init__(self, problem_id, mock_input, expected):
        self.id = problem_id
        self.mock_input = mock_input
        self.expected = expected


def get_solution_folder(problem_id):
    return f"solutions/S_{problem_id}"


def get_solution_file_name(problem_id):
    return f"solution_{problem_id}.py"


def get_test_file_name(problem_id):
    return f"test_solution_{problem_id}.py"


def trim_new_lines(string):
    return string.strip("\n")


def parse_data(html_markdown):
    soup = BeautifulSoup(html_markdown.text, "html.parser")
    inputs = [
        test.find("pre").text.strip("\n").split("\n")
        for test in soup.find_all(class_="input")
    ]
    results = [
        test.find("pre").text.strip("\n").replace("\n", "\\n")
        for test in soup.find_all(class_="output")
    ]
    return [
        Problem(i + 1, input, result)
        for i, (input, result) in enumerate(zip(inputs, results))
    ]


def output_templates(problem_id, data):
    problems_path = get_solution_folder(problem_id)
    os.mkdir(problems_path)
    save_problem(problems_path, problem_id)
    save_test(problems_path, data, problem_id)
    save_init(problems_path)


def save_init(problem_path):
    init = open(os.path.join(problem_path, "__init__.py"), "w")
    init.write("")
    init.close()


def save_problem(problem_path, problem_id):
    problem_file = os.path.join(
        problem_path, get_solution_file_name(problem_id)
    )
    pf = open(problem_file, "w")
    pf.write(SOLUTION_TEMPLATE_PATH.render(problem_id=problem_id))
    pf.close()


def save_test(base_path, data, problem_id):
    test_file = os.path.join(base_path, get_test_file_name(problem_id))
    tf = open(test_file, "w")
    tf.write(TEST_TEMPLATE_PATH.render(problem_id=problem_id, tests=data))
    tf.close()


def insert_markdown_info(html_markdown, problem_id, url):
    soup = BeautifulSoup(html_markdown.text, "html.parser")
    title_without_id = soup.find(class_="title").text.split(" ")[1:]
    difficulty = soup.find(title="Difficulty").text.strip().replace("*", "")
    title = " ".join(title_without_id)
    file_content = [line for line in open(README_PATH)]

    writer = open(README_PATH, "w")
    problem_section_line = math.inf

    for i, line in enumerate(file_content):
        if line.startswith(README_PROBLEMS):
            _, solved_tasks = line.split("-")
            line = f"{README_PROBLEMS} - {int(solved_tasks.strip()) + 1}\n"
            problem_section_line = i

        if problem_section_line + 1 < i and line == "\n":
            writer.write(
                f"* [{title} ({problem_id})]({url})"
                f" [✅]({get_solution_folder(problem_id)}"
                f"/{get_solution_file_name(problem_id)})"
                f" 🔥 {difficulty} \n"
            )
            problem_section_line = math.inf

        writer.write(line)

    writer.close()


def main():
    print("Enter CodeForces problem url:")
    url = input()
    if "codeforces.com" not in url:
        raise ValueError("Invalid CodeForces url")
    html_markdown = requests.get(url)
    data = parse_data(html_markdown)
    problem_id = "".join(url.split("/")[-2:])
    output_templates(problem_id, data)
    insert_markdown_info(html_markdown, problem_id, url)
    print(f"Problem {problem_id} saved!")


if __name__ == "__main__":
    main()
