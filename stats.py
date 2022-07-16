import pandas as pd 

from data import wifi_df 

mean_df = wifi_df.groupby(["code"])[["download", "upload", "ping"]].mean()
median_df = wifi_df.groupby(["code"])[["download", "upload", "ping"]].median()
std_df = wifi_df.groupby(["code"])[["download", "upload", "ping"]].std()

if __name__ == "__main__": 
    print("Mean df: ")
    print(mean_df)
    print("\nMedian df: ")
    print(median_df)
    print("\nStandard deviation df: ")
    print(std_df)