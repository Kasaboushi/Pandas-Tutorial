import pandas as pd
# First, create a series from the list below. Then, print it to make sure it works properly.
# After that, try to print individual elements.

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# Next, try to make a DataFrame. To start, create a DataFrame from test.csv and print it. Try pd.read_csv()
# dict is a sample dictionary that you can use as well. Create a second dataframe with dict.

dict = {"A":[1,2,3,4,5], "B":["a","b","c","d","e"], "C":["I","love","learning","Pandas","!"]}

# Use df.loc[] to return the first row. Print the result.

# Use df.loc[] to return the first three rows. Print the result.

# Try df.head() and df.tail()

# Print all rows with A values greater than 3 using a conditional.

# Print all names of the rows and columns



# Now, we will move into Data Cleaning problems. 
clean = {
    "Date": ["2020/12/01","2020/12/02","2020/12/03",None,20201204,20201205],
    "Pulse": [110,117,103,109,117,102],
    "MaxPulse": [130,145,135,175,148,127],
    "Calories": [409.1,479.0,340.0,282.4,406.0,300.0]
}

