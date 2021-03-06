# Testing WiFi Speed 

## Background 

My building recently got fiber-optic cable installed, 
and my brother and I were able to finally switch over to a reliable WiFi provider. 
Our plan is now the 
[Verizon 1 Gig plan](https://www.verizon.com/home/fios-fastest-internet/), 
which supposedly offers speeds of "up to 940/880 Mbps". 
While we were paying for 1G speed with our last provider 
([Optimum's 1 GigFiber Internet plan](https://www.optimum.com/?utm_source=Google&utm_medium=bps&utm_campaign=Opt_Fixed_Google_Brand_InFootprint_Optimum_Core_Exact&bsp=optgmOCTsearchBrand914&off=1P39.99&s_cid=OptimumSEM1P39.99-_-gm-_-acq-_-bps-_-cpc-_-ggl-_-X-X-X-X&s_kwcid=AL!%3c9112%3e!3!596964362398!e!!g!!optimum%20wifi&gclsrc=aw.ds&gclid=CjwKCAjww8mWBhABEiwAl6-2RfzRJkAeVsQTRd8bMu_DVFu0vwxKNpmp-rKuio7wGLb6v5QOcHQt0hoCkNsQAvD_BwE)), 
we had consistent WiFi disconnects and speeds much lower than promised, 
so the switch to Verizon was pretty much required. 

During our time with Optimum, we bough the 
[Orbi Tri-band Mesh Wifi 6 System](https://www.netgear.com/home/wifi/mesh/rbk853/); 
it is an incredible device, and is a good setup since we can each put one of the satellites in our rooms. 
There is a "main" Orbi device that connects directly to your router, 
and two "satellites" that you plug somewhere else to boost your connection. 

With the new WiFi installed, we wanted to try and answer a few questions: 
1. Are we able to truly reach the maximum speed offered by our provider? 
2. Does the Orbi provide a significant boost to Wifi speed, either wireless or via ethernet? 
3. Does using wired connection through a satellite have the same impact as with the main Orbi? 

## Methodology 

Three accepted criteria of testing internet connection are download speed in Mbps 
(megabits per second), upload speed in Mbps, and ping (a.k.a. latency) in ms (milliseconds). 
A good summary of these can be found [here](https://www.speedtest.net/about/knowledge/glossary). 

The easiest and most convenient way was to use 
[Speedtest](https://www.speedtest.net), which provides estimates for the three criteria mentioned above. 
Testing was done on a 
[COOFUN Mini PC AMD Ryzen 7 3750H UM700](https://www.amazon.com/dp/B093BBLB4K?psc=1&ref=ppx_yo2ov_dt_b_product_details)
using 
[Speedtest's app for Windows 10](https://www.speedtest.net/apps/windows), 
and all testing was done in my bedroom. 
For wired connection, 
[DanYee Cat 7 Ethernet Cables](https://www.amazon.com/dp/B073RZNGQ5?psc=1&ref=ppx_yo2ov_dt_b_product_details)
were used. 

To answer the questions, the following configurations were used: 
- *wireless_base*: internet speed purely through Verizon's router. 
- *wireless_orbi*: wireless connection speed but having the WiFi boosted through the Orbi. 
- *ethernet_base*: wired connection with the ethernet cable plugged into the Verizon router. 
- *ethernet_orbi*: wired connection with the ethernet cable plugged into the main Orbi. 
- *ethernet_orbi_v2*: wired connection with the ethernet cable plugged into the satellite Orbi in my room. 

For a given configuration, 10 runs of the Speedtest test were recorded manually. 
Perhaps a more sophisticated test can be done using something like 
[speedtest-cli](https://github.com/sivel/speedtest-cli), but even for this small test 
we can get a lot of insight. 

## Relevant figures 

Below shows two relevant figures: 
- Box plots for the test results for each of the three criteria, split by each of the five configurations. 
- Tables showing the mean, median, and standard deviation of each of the tests. 

<figure>
    <img src="./img/download_box.png" alt="Download tests box plot" width="100%"/>
    <img src="./img/upload_box.png" alt="Upload tests box plot" width="100%"/>
    <img src="./img/ping_box.png" alt="Ping tests box plot" width="100%"/>
    <!-- <figcaption> 
        Box plots of the results from each of the three tests. 
    </figcaption> -->
</figure>

Mean of test results: 
| Configuration    |   Download Speed (Mbps) |   Upload Speed (Mbps) |   Ping (ms) |
|:-----------------|------------------------:|----------------------:|------------:|
| ethernet_base    |                 911.481 |               199.451 |         4.1 |
| ethernet_orbi    |                 931.505 |               238.505 |         3.5 |
| ethernet_orbi_v2 |                 369.147 |               140.675 |         7.4 |
| wireless_base    |                  45.2   |                55.027 |         7.2 |
| wireless_orbi    |                 365.204 |               111.108 |         9   |


Median of test results: 
| Configuration    |   Download Speed (Mbps) |   Upload Speed (Mbps) |   Ping (ms) |
|:-----------------|------------------------:|----------------------:|------------:|
| ethernet_base    |                 931.215 |               206.455 |         4   |
| ethernet_orbi    |                 937.25  |               236.795 |         3   |
| ethernet_orbi_v2 |                 364.265 |               144.615 |         7.5 |
| wireless_base    |                  44.025 |                53.475 |         7   |
| wireless_orbi    |                 389.17  |               105.925 |         9.5 |


Standard deviation of test results: 
| Configuration    |   Download Speed (Mbps) |   Upload Speed (Mbps) |   Ping (ms) |
|:-----------------|------------------------:|----------------------:|------------:|
| ethernet_base    |                 45.5116 |              31.1031  |    2.02485  |
| ethernet_orbi    |                 14.0623 |              27.1253  |    0.849837 |
| ethernet_orbi_v2 |                 39.5545 |              21.7045  |    0.966092 |
| wireless_base    |                  6.5029 |               5.61764 |    1.22927  |
| wireless_orbi    |                 58.7189 |              16.7771  |    1.88562  |


Maximum of test results: 
| Configuration    |   Download Speed (Mbps) |   Upload Speed (Mbps) |   Ping (ms) |
|:-----------------|------------------------:|----------------------:|------------:|
| ethernet_base    |                  941.29 |                233.71 |           8 |
| ethernet_orbi    |                  940.68 |                285.02 |           5 |
| ethernet_orbi_v2 |                  449.61 |                171.24 |           9 |
| wireless_base    |                   59.41 |                 68.43 |           9 |
| wireless_orbi    |                  415.86 |                139.09 |          11 |


Minimum of test results: 
| Configuration    |   Download Speed (Mbps) |   Upload Speed (Mbps) |   Ping (ms) |
|:-----------------|------------------------:|----------------------:|------------:|
| ethernet_base    |                  794.72 |                147.76 |           2 |
| ethernet_orbi    |                  893.96 |                203.15 |           3 |
| ethernet_orbi_v2 |                  308.34 |                 90.68 |           6 |
| wireless_base    |                   36.59 |                 48.91 |           5 |
| wireless_orbi    |                  231.26 |                 80.88 |           6 |

## Conclusions 

Overall, it appears that the best possible configuration is the 
**wired connection to the main Orbi**. 
This configuration has (or at least is on par with) the highest download speed, highest upload speed, 
and lowest ping. 
When compared to the wired connection to the Verizon router, 
it also seems to be more consistent, in the sense that the results do not vary nearly as much, 
i.e. a much lower standard deviation. 

Several key inferences can be made regarding the entire experiment:  
- *The Orbi provides a significant boost in wireless connection over the basic router.* 
Comparing *wireless_orbi* to *wireless_base*, 
we see that there is about about an eightfold increase in download speed, 
a doubling of upload speed, and lower ping. 
- *Using wired connection, it is possible to obtain speeds extremely close to the theoretical maximum.*
This can be seen from both *ethernet_base* and *ethernet_orbi*, 
as the average speeds are both very close to the supposed limit of 940 Mbps. 
In fact, the maximum download speed for both (slightly) exceeds 940 Mbps. 
- *Using wired connection with the satellite Orbi does not offer any significant speed improvements over wireless.*
Comparing *wireless_orbi* to *ethernet_orbi_v2*, we can see that 
there is little difference between the download speeds. 
While the upload speed is slightly faster on average for *ethernet_orbi_v2*, 
the difference does not seem to be significant. 

All of these results imply the following: 
1. The service offered by Verizon does in fact live up to its potential, at least when using wired connection. 
2. The Orbi only serves to improve its performance, especially for wireless connection. 

## Appendix: full dataset 

| Configuration    |   Download Speed (Mbps) |   Upload Speed (Mbps) |   Ping (ms) |
|:-----------------|------------------------:|----------------------:|------------:|
| wireless_base    |                   39.42 |                 51.25 |           9 |
| wireless_base    |                   51.27 |                 51.83 |           9 |
| wireless_base    |                   40.69 |                 56.03 |           7 |
| wireless_base    |                   36.59 |                 54.73 |           5 |
| wireless_base    |                   42.94 |                 58.96 |           6 |
| wireless_base    |                   47.45 |                 48.91 |           7 |
| wireless_base    |                   43.87 |                 51.15 |           7 |
| wireless_base    |                   46.18 |                 56.76 |           8 |
| wireless_base    |                   44.18 |                 52.22 |           7 |
| wireless_base    |                   59.41 |                 68.43 |           7 |
| wireless_orbi    |                  414.38 |                130.25 |          11 |
| wireless_orbi    |                  385.89 |                105.76 |          10 |
| wireless_orbi    |                  295.05 |                117.11 |          11 |
| wireless_orbi    |                  231.26 |                 80.88 |           6 |
| wireless_orbi    |                  363.83 |                123.25 |           7 |
| wireless_orbi    |                  360.19 |                105.25 |           7 |
| wireless_orbi    |                  393.4  |                106.09 |          11 |
| wireless_orbi    |                  415.86 |                104.98 |          10 |
| wireless_orbi    |                  399.73 |                139.09 |           9 |
| wireless_orbi    |                  392.45 |                 98.42 |           8 |
| ethernet_orbi    |                  939.25 |                258.14 |           3 |
| ethernet_orbi    |                  939.03 |                203.15 |           3 |
| ethernet_orbi    |                  940.68 |                285.02 |           3 |
| ethernet_orbi    |                  934.33 |                272.19 |           3 |
| ethernet_orbi    |                  935.8  |                231.77 |           3 |
| ethernet_orbi    |                  927.74 |                238.71 |           3 |
| ethernet_orbi    |                  938.7  |                204.45 |           3 |
| ethernet_orbi    |                  938.85 |                216.87 |           5 |
| ethernet_orbi    |                  893.96 |                239.87 |           4 |
| ethernet_orbi    |                  926.71 |                234.88 |           5 |
| ethernet_orbi_v2 |                  389.2  |                129.51 |           8 |
| ethernet_orbi_v2 |                  449.61 |                130.93 |           8 |
| ethernet_orbi_v2 |                  398.95 |                138.18 |           7 |
| ethernet_orbi_v2 |                  367.86 |                152.07 |           7 |
| ethernet_orbi_v2 |                  352.9  |                136.34 |           6 |
| ethernet_orbi_v2 |                  337.38 |                171.24 |           7 |
| ethernet_orbi_v2 |                  360.67 |                 90.68 |           6 |
| ethernet_orbi_v2 |                  387.81 |                154.19 |           9 |
| ethernet_orbi_v2 |                  338.75 |                151.05 |           8 |
| ethernet_orbi_v2 |                  308.34 |                152.56 |           8 |
| ethernet_base    |                  889.57 |                228.67 |           4 |
| ethernet_base    |                  913.01 |                197.11 |           2 |
| ethernet_base    |                  939.99 |                205.25 |           4 |
| ethernet_base    |                  893    |                157.08 |           4 |
| ethernet_base    |                  927.26 |                225.44 |           6 |
| ethernet_base    |                  941.29 |                233.71 |           2 |
| ethernet_base    |                  935.17 |                222.42 |           6 |
| ethernet_base    |                  794.72 |                147.76 |           3 |
| ethernet_base    |                  939.88 |                169.41 |           8 |
| ethernet_base    |                  940.92 |                207.66 |           2 |