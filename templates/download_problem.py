import math
import os
import requests

from pyquery import PyQuery as pq
from mako.template import Template

TEMPLATE_PATH = './templates'
PROBLEM_TEMPLATE_PATH = Template(filename=f'{TEMPLATE_PATH}/template_solution.txt', )
TEST_TEMPLATE_PATH = Template(filename=f'{TEMPLATE_PATH}/template_test.txt')
README_PATH = './README.md'
README_PROBLEMS = '## Solved Problems'


class Problem:
    def __init__(self, id, mock_input, expected):
        self.id = id
        self.mock_input = mock_input
        self.expected = expected


def parse_html_pre(pre):
    lines = pre.split("\n")
    return lines if len(lines) <= 1 else pre.split("\n")[1:-1]


def parse_data(html_markdown):
    q = pq(html_markdown.text)
    tests = q(".sample-tests")

    inputs = [parse_html_pre(i.text) for i in tests(".input pre")]
    results = [parse_html_pre(i.text) for i in tests(".output pre")]

    return [Problem(i + 1, input, "/n".join(result)) for i, (input, result) in
            enumerate(zip(inputs, results))]


def output_templates(problem_id, data):
    problems_path = f"problems/P_{problem_id}"
    os.mkdir(problems_path)
    save_problem(problems_path, problem_id)
    save_test(problems_path, data, problem_id)
    save_init(problems_path)


def save_init(problem_path):
    init = open(os.path.join(problem_path, "__init__.py"), "w")
    init.write("")
    init.close()


def save_problem(problem_path, problem_id):
    problem_file = os.path.join(problem_path, f"solution_{problem_id}.py")
    pf = open(problem_file, "w")
    pf.write(PROBLEM_TEMPLATE_PATH.render(problem_id=problem_id))
    pf.close()


def save_test(base_path, data, problem_id):
    test_file = os.path.join(base_path, f"test_solution_{problem_id}.py")
    tf = open(test_file, "w")
    tf.write(TEST_TEMPLATE_PATH.render(problem_id=problem_id, examples=data))
    tf.close()


def insert_markdown_info(html_markdown, problem_id, url):
    q = pq(html_markdown.text)
    title = q(".header .title").text()
    file_content = [line for line in open(README_PATH)]

    writer = open(README_PATH, "w")
    problem_section_line = 0

    for i, line in enumerate(file_content):
        if line.startswith(README_PROBLEMS):
            _, solved_tasks = line.split("-")
            line = f"{README_PROBLEMS} - {int(solved_tasks.strip()) + 1}\n"
            problem_section_line = i

        if problem_section_line + 1 < i and line == "\n":
            writer.write(f"* [{title} ({problem_id})]({url})  ✅\n")
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
