def init_grid():
  # your ocde here
  
def print_2D(grid):
  # your code here
  
def average_rows(grid):
  # your code here

def average_columns(grid):
  # your code here
  
  
####### DO NOT CHANGE ANYTHING BELOW THIS LINE ##########
# ---------- Main Program --------------

# Generate the random grid
grid = init_grid()

# Calculate the averages
rowAverages = average_rows(grid)
columnAverages = average_columns(grid)

# Print the board
print_2D(grid)

# Print the averages
print("Row averages:    {}".format(rowAverages))
print("Column averages: {}".format(columnAverages))
