#! /usr/bin/env python3 

import pandas as pd

from stats import summary_dict


# converting column names to be more professional 
col_convert = {
    "download": "Download Speed (Mbps)", 
    "upload": "Upload Speed (Mbps)", 
    "ping": "Ping (ms)"
}

def print_summary_tabs(summary_dict: dict[str, pd.DataFrame]) -> None: 
    """
    Prints out tables in terminal that can be copied to README 
    Takes in dict where key is the name and the value is the df corresponding to that 
    e.g. "Mean" and a df with the mean of your test results 
    """
    print("\n")
    for name, df in summary_dict.items(): 
        df.index.names = ["Configuration"]
        print(f"{name} of test results: ")
        print( df.rename(columns=col_convert).to_markdown() )
        print("\n")


if __name__ == "__main__": 
    print_summary_tabs(summary_dict)