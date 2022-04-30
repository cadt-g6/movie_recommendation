import json
import pandas as pd


def write_csv(path: str, df: pd.DataFrame):
    # prevent export int as float
    df = df.convert_dtypes()
    df.to_csv(
        path,
        encoding='utf-8',
        index_label=False,
        index=False
    )


def print_dict(dict: dict):
    json_dumps = json.dumps(
        dict,
        indent=4,
        default=str,
        sort_keys=False,
    )
    print(json_dumps)