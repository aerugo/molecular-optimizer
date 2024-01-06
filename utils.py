import numpy as np

# Query and observation functions

def get_all_observations(df, fnc):
    '''
    df is a dataframe with columns x1, x2, ..., xn and y.
    Outputs the dataframe as list of dictionaries of observations of format:
    [{X: {'x1': 0.42434, 'x2': 0.385025, 'x3': 0.359904, 'x4': 0.411092}, Y: 0.607759}, ...]
    '''
    observations = []
    for i in range(len(df)):
        observation = {}
        observation['X'] = df.iloc[i, :-1].to_dict()
        observation['Y'] = df.iloc[i, -1]
        observations.append(observation)
    print(f'function_{fnc} = {observations}')

# Find closest point in a list of points to a reference point
    
def find_closest_point(reference_point, points_list):
    # Extract all points into a numpy array for efficient computation
    points_array = np.array([list(point.values()) for point in points_list])
    ref_point_array = np.array(list(reference_point.values()))

    # Compute the Euclidean distances from the reference point to all other points
    distances = np.sqrt(((points_array - ref_point_array) ** 2).sum(axis=1))

    # Find the index of the closest point
    closest_point_index = np.argmin(distances)

    # Return the closest point in the original format
    return closest_point_index