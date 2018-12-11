# HW2
## pcsII_homework

This is an assignment for my PCS II class.
The goal is to time `quick_sort` algorithm and `merge_sort` on randomly generated lists of length 10, 100, 1000, 10000… 
`sort_time()` will time `quick_sort` and `merge_sort` on the same data, i.e. sorting the same list.
For each list length (10, 100, 1000…) we time the algorithms of 5 different lists and get an average.
Finally, the times for the various test are plotted against each other on the top plot in a normal scale and on the bottom plot on a log scale.


As we can see from the [plot](https://raw.githubusercontent.com/Amedeoxa/HW2/master/time_plot.png), `quick_sort` is consistently faster than `merge_sort`, but always by the same fraction. 
Infact as we now both quick_sort and merge_sort both have an average-case performance of **O(n log(n))**.
This is clear from the lower plot in log scale.
