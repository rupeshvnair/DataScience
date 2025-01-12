'''
I have 25 horses. What is the least number of races i need to make to get the top 3 horses.
'''

def find_top_3_horses():
    """
    Determines the least number of races required to identify the top 3 horses out of 25.
    Assumes 5 horses can race at a time.
    """
    groups = [[f"H{i*5+j*1}" for j in range(5) ]for i in range(5)]
    race_results = {i:sorted(groups) for i, group in enumerate(groups)}
    races = []
    for i in range(5):
        races.append(sorted(race_results[i]))
    return races

data = find_top_3_horses()
print(data)