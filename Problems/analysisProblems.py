import pandas

dict = {
    "A":[1,2,3,4,1,5,2,7,0,3,9,2,4,3,5,6,7,3,1,6,8,8,2],
    "B":[12,43,69,50,50,50,50,34,69,23,10,2,3,24,35,85,86],
    "C":[126,126,126,157,124,159,94,289,39,173]
}

# Create a DataFrame, then find the mean, median and mode of each row.
# A: Mean: 4.0   Median: 3   Mode: 2
# B: Mean: 40.88235294117647  Median: 43   Mode: 50
# C: Mean: 141.3   Median: 126  Mode: 126