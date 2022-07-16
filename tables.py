import pandas as pd
from pyparsing import col

from stats import summary_dict


col_convert = {
    "download": "Download Speed (Mbps)", 
    "upload": "Upload Speed (Mbps)", 
    "ping": "Ping (ms)"
}

def print_summary_tabs(summary_dict: dict[str, pd.DataFrame]) -> None: 
    print("\n")
    for name, df in summary_dict.items(): 
        df.index.names = ["Configuration"]
        print(f"{name} of test results: ")
        print( df.rename(columns=col_convert).to_markdown() )
        print("\n")


if __name__ == "__main__": 
    print_summary_tabs(summary_dict)