from setuptools import find_packages, setup
from typing import List

def get_reqd(file_path: str) -> List[str]:
    reqd = []
    with open(file_path) as file_obj:
        reqd = file_obj.readlines()
        reqd = [req.replace("\n", "") for req in reqd]

        # Optional: remove -e . if present
        if "-e ." in reqd:
            reqd.remove("-e .")

    return reqd


setup(
    name="diamondpriceprediction_project",
    version="0.22.2",
    author="hohiyaar",
    author_email="hahah@gmail.com",
    packages=find_packages(),
    install_requires=get_reqd("requirements.txt")
)