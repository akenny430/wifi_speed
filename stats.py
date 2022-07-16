#! /usr/bin/env python3 

import pandas as pd 

from data import wifi_df 

# summary stats: mean, median, and standard deviation 
mean_df = wifi_df.groupby(["code"])[["download", "upload", "ping"]].mean()
median_df = wifi_df.groupby(["code"])[["download", "upload", "ping"]].median()
std_df = wifi_df.groupby(["code"])[["download", "upload", "ping"]].std()
max_df = wifi_df.groupby(["code"])[["download", "upload", "ping"]].max()
min_df = wifi_df.groupby(["code"])[["download", "upload", "ping"]].min()

# combining all into dict to be used in tables.py 
summary_dict = {
    "Mean": mean_df, 
    "Median": median_df, 
    "Standard deviation": std_df, 
    "Maximum": max_df, 
    "Minimum": min_df
}

if __name__ == "__main__": 
    print("Mean df: ")
    print(mean_df)
    print("\nMedian df: ")
    print(median_df)
    print("\nStandard deviation df: ")
    print(std_df)
    print("\nMaximum df: ")
    print(max_df)
    print("\nMinimum df: ")
    print(min_df)