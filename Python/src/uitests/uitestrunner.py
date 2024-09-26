import shutil
from argparse import Namespace
from pathlib import Path

from behave.__main__ import main as run_behave


def run(args: Namespace) -> None:
    params = [(Path(__file__).parent / "features").absolute()]
    if args.reports:
        params += ["--junit"]

    report_path = Path("./reports").absolute()
    params += ["--junit-directory", "."]

    try:
        shutil.rmtree(report_path)
    except:
        pass

    test_result = run_behave(params)
    print(test_result)
