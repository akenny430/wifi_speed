import plotnine as pn 

from data import wifi_df, wifi_melt_df


speed_cyan = "#98fbbd"
speed_purple = "#ee7cd9"
speed_gray = "#d3d3d3"

download_fig = (
    pn.ggplot(wifi_df, pn.aes(x="code", y="download")) + 
    pn.geom_boxplot(fill=speed_cyan) + 
    pn.ylim(0, 1000) + 
    pn.labs(x="Configuration", y="Download speed (mbps)") +
    pn.theme_bw()
)

upload_fig = (
    pn.ggplot(wifi_df, pn.aes(x="code", y="upload")) + 
    pn.geom_boxplot(fill=speed_purple) + 
    pn.ylim(0, 300) + 
    pn.labs(x="Configuration", y="Upload speed (mbps)") +
    pn.theme_bw()
)

ping_fig = (
    pn.ggplot(wifi_df, pn.aes(x="code", y="ping")) + 
    pn.geom_boxplot(fill=speed_gray) + 
    pn.ylim(0, 12) + 
    pn.labs(x="Configuration", y="Ping (ms)") +
    pn.theme_bw()
)

combined_fig = (
    pn.ggplot(wifi_melt_df, pn.aes(x="code", y="value")) + 
    pn.geom_boxplot() + 
    pn.facet_wrap("variable") + 
    pn.lims(y=(0,1000)) + 
    pn.theme_bw()
)

print(download_fig)
print(upload_fig)
print(ping_fig)
# print(combined_fig)
# download_fig.save("./img/download_box.png")