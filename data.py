#! /usr/bin/env python3 

import pandas as pd 

# wireless -- no boost   
speed1 = pd.DataFrame(
    {
        "download": [39.42, 51.27, 40.69, 36.59, 42.94, 47.45, 43.87, 46.18, 44.18, 59.41], 
        "upload":   [51.25, 51.83, 56.03, 54.73, 58.96, 48.91, 51.15, 56.76, 52.22, 68.43], 
        "ping":     [9, 9, 7, 5, 6, 7, 7, 8, 7, 7], 
        "code":     ["wireless_base"] * 10
    }
)


# wireless -- ORBI boost 
speed2 = pd.DataFrame(
    {
        "download": [414.38, 385.89, 295.05, 231.26, 363.83, 360.19, 393.40, 415.86, 399.73, 392.45], 
        "upload":   [130.25, 105.76, 117.11, 80.88, 123.25, 105.25, 106.09, 104.98, 139.09, 98.42], 
        "ping":     [11, 10, 11, 6, 7, 7, 11, 10, 9, 8], 
        "code":     ["wireless_orbi"] * 10
    }
)


# ethernet -- main ORBI 
speed3 = pd.DataFrame(
    {
        "download": [939.25, 939.03, 940.68, 934.33, 935.80, 927.74, 938.70, 938.85, 893.96, 926.71], 
        "upload":   [258.14, 203.15, 285.02, 272.19, 231.77, 238.71, 204.45, 216.87, 239.87, 234.88], 
        "ping":     [3, 3, 3, 3, 3, 3, 3, 5, 4, 5], 
        "code":     ["ethernet_orbi"] * 10 
    }
)

# ethernet -- secondary ORBI 
speed4 = pd.DataFrame(
    {
        "download": [389.20, 449.61, 398.95, 367.86, 352.90, 337.38, 360.67, 387.81, 338.75, 308.34], 
        "upload":   [129.51, 130.93, 138.18, 152.07, 136.34, 171.24, 90.68, 154.19, 151.05, 152.56], 
        "ping":     [8, 8, 7, 7, 6, 7, 6, 9, 8, 8], 
        "code":     ["ethernet_orbi_v2"] * 10 
    }
)


# ethernet -- verizon router 
speed5 = pd.DataFrame(
    {
        "download": [889.57, 913.01, 939.99, 893.00, 927.26, 941.29, 935.17, 794.72, 939.88, 940.92], 
        "upload":   [228.67, 197.11, 205.25, 157.08, 225.44, 233.71, 222.42, 147.76, 169.41, 207.66], 
        "ping":     [4, 2, 4, 4, 6, 2, 6, 3, 8, 2], 
        "code":     ["ethernet_base"] * 10 
    }
)


# combined dataset 
wifi_df = pd.concat((speed1, speed2, speed3, speed4, speed5), ignore_index=True)

# melting df to use for combined plots 
wifi_melt_df = pd.melt(
    wifi_df, 
    id_vars="code", 
    value_vars=["download", "upload", "ping"], 
    var_name="test_type", 
    value_name="test_result"
)


if __name__ == "__main__": 
	print(wifi_df) 
