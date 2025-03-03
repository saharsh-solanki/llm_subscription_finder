import json
from helper import config


def load_json(file_path):
    with open(file_path, "r") as f:
        plans = json.load(f)
        return plans

def open_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

SINGLE_PLAN_TEMPLATE = open_file(config.SINGLE_PLAN_TEMPLATE_PATH)
def format_plan(plan):
    return SINGLE_PLAN_TEMPLATE.format(**plan)