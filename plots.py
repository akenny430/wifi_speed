#! /usr/bin/env python3

import plotnine as pn 

from data import wifi_df, wifi_melt_df


# colors 
speed_cyan = "#98fbbd"
speed_purple = "#ee7cd9"
speed_gray = "#d3d3d3"

# download boxplot 
download_fig = (
    pn.ggplot(wifi_df, pn.aes(x="code", y="download")) + 
    pn.geom_boxplot(fill=speed_cyan) + 
    pn.ylim(0, 1000) + 
    pn.labs(x="Configuration", y="Download speed (Mbps)") +
    pn.theme_bw()
)

# upload boxplot 
upload_fig = (
    pn.ggplot(wifi_df, pn.aes(x="code", y="upload")) + 
    pn.geom_boxplot(fill=speed_purple) + 
    pn.ylim(0, 300) + 
    pn.labs(x="Configuration", y="Upload speed (Mbps)") +
    pn.theme_bw()
)

# ping boxplot 
ping_fig = (
    pn.ggplot(wifi_df, pn.aes(x="code", y="ping")) + 
    pn.geom_boxplot(fill=speed_gray) + 
    pn.ylim(0, 12) + 
    pn.labs(x="Configuration", y="Ping (ms)") +
    pn.theme_bw()
)

# combined boxplots (not really good because scaling is so different)
combined_fig = (
    pn.ggplot(wifi_melt_df, pn.aes(x="code", y="test_result")) + 
    pn.geom_boxplot() + 
    pn.facet_wrap("test_type") + 
    pn.lims(y=(0,1000)) + 
    pn.theme_bw()
)

def save_figs(do_combined: bool = False) -> None: 
    """
    Saving boxplots to their respective locations 
    By default does not save the combined plot, set do_combined=True to save 
    """
    print("Saving plots ...")
    plot_params = {"width": 8, "height": 5, "verbose": False}
    download_fig.save("./img/download_box.png", **plot_params)
    upload_fig.save("./img/upload_box.png", **plot_params)
    ping_fig.save("./img/ping_box.png", **plot_params)
    if do_combined: 
        combined_fig.save("./img/combined_box.png")

def print_figs(do_combined: bool = False) -> None: 
    """
    Prints boxplots for all three variables 
    By default does not print the combined plot, set do_combined=True to print  
    """
    print("Printing plots ...")
    print(download_fig)
    print(upload_fig)
    print(ping_fig)
    if do_combined: 
        print(do_combined) 

if __name__ == "__main__": 
    save_figs()
    # print_figs() 