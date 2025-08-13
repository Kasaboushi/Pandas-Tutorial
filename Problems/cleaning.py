import pandas as pd

# Now, we will move into Data Cleaning problems. 
clean = {
    "Date": ["2020/12/01","2020/12/02","2020/12/03",None,20201204,20201205,"2020/12/03"],
    "Pulse": [110,117,103,109,117,102,103],
    "MaxPulse": [130,145,135,175,148,127,134],
    "Calories": [409.1,479.0,340.0,282.4,406.0,300.0,340.0]
}

# Remove all rows with null values.

# Edit improperly set dates into the correct format.

# The sixth row has an incorrect Calories value. Change the value to 330.3

# There is a duplicate row. Remove it using the built-in methods.

