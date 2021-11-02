import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from jinja2 import Template

test_template = Template(Path(os.path.join(os.path.dirname(__file__), "templates/test.txt")).read_text())
problem_template = Template(Path(os.path.join(os.path.dirname(__file__), "templates/problem.txt")).read_text())


def main(url: str) -> None:
    url_parts = url.split("/")
    group = url_parts[-1]
    problem_number = url_parts[-3] if url_parts[-2] == "problem" else url_parts[-2]

    html = requests.get(url).text
    html.replace("\n", os.linesep)
    soup = BeautifulSoup(html, features="html.parser")
    for br in soup.find_all("br"):
        br.replace_with(os.linesep)

    title = soup.select_one(".problem-statement .header .title").text \
        .replace(f"{group}. ", "").replace(" ", "_").lower()
    inputs = soup.select(".sample-tests .input pre")
    outputs = soup.select(".sample-tests .output pre")

    problem_name = f"_{problem_number}_{group}_{title}"
    test_name = f"_{problem_number}_{group}_{title}_test"
    folder_name = f"_{problem_number}"

    tests_folder = "tests"

    problem_folder = os.path.join(os.path.dirname(__file__), '..', 'problems', folder_name)

    path = Path(os.path.join(problem_folder, tests_folder))
    path.mkdir(exist_ok=True, parents=True)

    for i, content in enumerate(inputs):
        with open(os.path.join(problem_folder, tests_folder, f"{i}.in.txt"), "w") as f:
            f.write(content.text)

    for i, content in enumerate(outputs):
        with open(os.path.join(problem_folder, tests_folder, f"{i}.out.txt"), "w") as f:
            f.write(content.text)

    with open(os.path.join(problem_folder, problem_name + ".py"), "w") as f:
        f.write(problem_template.render())

    with open(os.path.join(problem_folder, test_name + ".py"), "w") as f:
        f.write(test_template.render(problem_name=problem_name))

    with open(os.path.join(problem_folder, "__init__.py"), "w") as f:
        f.write("")
