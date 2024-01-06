import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def x_array_to_dict(x_array):
    """
    Converts a list of values to a dictionary with keys x1, x2, x3, ...
    """
    x_dict = {}
    for i, num in enumerate(x_array):
        x_dict[f'x{i+1}'] = num
    return x_dict

def x_dictlist_to_array(x_dict):
    """
    Converts a list of dictionaries of values to list of lists.
    """
    x_list = []
    for x in x_dict:
        x_list.append(list(x.values()))
    return x_list

# invert x_dictlist_to_array function
def x_array_to_dictlist(x_array):
    """
    Converts a list of lists to a list of dictionaries with keys x1, x2, x3, ...
    """
    x_dictlist = []
    for x in x_array:
        x_dict = {}
        for i, num in enumerate(x):
            x_dict[f'x{i+1}'] = num
        x_dictlist.append(x_dict)
    return x_dictlist


def benchmark_function(x1, x2, x3, noise_strength=0.1):
    """
    Returns a benchmark function that takes a dictionary of values and returns a function value.
    Local maxima should be at (0.3, 0.3, 0.3) and (0.7, 0.7, 0.7)
    """
    return (np.exp(-10 * (x1 - 0.3)**2) 
                            + np.exp(-10 * (x2 - 0.3)**2) 
                            + np.exp(-10 * (x3 - 0.3)**2) 
                            + 0.5 * np.sin(4 * np.pi * (x1-0.7)) 
                            + 0.5 * np.sin(4 * np.pi * (x2-0.7)) 
                            + 0.5 * np.sin(4 * np.pi * (x3-0.7))
                            + noise_strength * np.random.randn())

def benchmark_function_scatterplot(noise_strength=0.1):
    # generate some random data
    num_samples = 500
    x1 = np.random.uniform(0, 1, num_samples)
    x2 = np.random.uniform(0, 1, num_samples)
    x3 = np.random.uniform(0, 1, num_samples)
    y = benchmark_function(x1, x2, x3, noise_strength=0.1)

    # Create 3D scatter plot
    scatter = go.Scatter3d(
        x=x1,
        y=x2,
        z=x3,
        mode='markers',
        marker=dict(
            size=6,
            color=y,                # set color to an array/list of desired values
            colorscale='Viridis',   # choose a colorscale
            opacity=0.8,
            colorbar=dict(
                title="y values",
                nticks=10
            )
        ),
        hovertemplate = 
        "<b>x1</b>: %{x}<br>" +
        "<b>x2</b>: %{y}<br>" +
        "<b>x3</b>: %{z}<br>" +
        "<b>y</b>: %{marker.color}<br>" +
        "<extra></extra>"
    )

    # Add title and labels
    layout = go.Layout(scene=dict(xaxis_title='x1',
                                yaxis_title='x2',
                                zaxis_title='x3'),
                    title_text="Interactive 3D Scatter plot with color scale")
    fig = go.Figure(data=[scatter], layout=layout)

    fig.show()


def print_next_query(next_query):
    print("Next query: ", end='')
    for i, num in enumerate(next_query.values()):
        print(f'{num:.6f}', end='')
        if i != len(next_query) - 1:
            print("-", end='')
    print()  # New line at the end.

def plot_scatter_matrix(X_list, y_list, axis_limits={}, next_X={}, next_y=0):
    df = pd.DataFrame(X_list)
    df['y'] = y_list
    df['point_type'] = 'Regular'

    # Create a DataFrame for next query point if next_X is not empty
    next_query_df = pd.DataFrame()
    if next_X:
        next_query_df = pd.DataFrame([next_X])
        next_query_df['y'] = next_y
        next_query_df['point_type'] = 'Next Query'

    # Get all column names starting with 'x'
    dimensions = [col for col in df.columns if col.startswith('x')]

    # Determine the type of plot based on dimensions
    if len(dimensions) == 1:
        fig = px.scatter(df[df.point_type == 'Regular'],
                         x=dimensions[0],
                         y='y',
                         color='y',
                         color_continuous_scale='Viridis')

        # Plot 'Next Query' points if any
        if not next_query_df.empty:
            fig.add_scatter(x=next_query_df[dimensions[0]],
                            y=next_query_df['y'],
                            mode='markers',
                            marker_symbol='x',
                            marker_color='red',
                            name='Next Query')
    
    elif len(dimensions) == 2:
        fig = px.scatter(df[df.point_type == 'Regular'],
                         x=dimensions[0],
                         y=dimensions[1],
                         color='y',
                         color_continuous_scale='Viridis')

        if not next_query_df.empty:
            fig.add_scatter(x=next_query_df[dimensions[0]],
                            y=next_query_df[dimensions[1]],
                            mode='markers',
                            marker_symbol='x',
                            marker_color='red',
                            name='Next Query')
    
    elif len(dimensions) == 3:
        fig = px.scatter_3d(df[df.point_type == 'Regular'],
                            x=dimensions[0],
                            y=dimensions[1],
                            z=dimensions[2],
                            color='y',
                            color_continuous_scale='Viridis')

        if not next_query_df.empty:
            fig.add_scatter3d(x=next_query_df[dimensions[0]],
                            y=next_query_df[dimensions[1]],
                            z=next_query_df[dimensions[2]],
                            mode='markers',
                            marker_symbol='x',
                            marker_color='red',
                            name='Next Query')
    
    else:
        # Scatter matrix for regular points
        fig = px.scatter_matrix(df[df.point_type == 'Regular'],
                                dimensions=dimensions,
                                color='y',
                                color_continuous_scale='Viridis')

        # Overlay scatter matrix for 'Next Query' points if any
        if not next_query_df.empty:
            next_query_fig = px.scatter_matrix(next_query_df,
                                               dimensions=dimensions,
                                               color_discrete_sequence=['red'])  
            
            for i in range(len(next_query_fig.data)):
                fig.add_trace(next_query_fig.data[i])

        # Set custom axis limits if provided
        for i, dim in enumerate(dimensions):
            if dim in axis_limits and len(axis_limits[dim]) == 2:
                # Construct the axis names
                xaxis_name = f'xaxis{str(i + 1)}'
                yaxis_name = f'yaxis{str(i + 1)}'
                fig.update_layout(
                    **{
                        xaxis_name: dict(range=axis_limits[dim]),
                        yaxis_name: dict(range=axis_limits[dim]),
                    }
                )
                                
    # Make the figure square and adjust margins to prevent label overlap
    fig.update_layout(
        autosize=True,
        width=1200,  # You may adjust this based on your display size
        height=1200,  # You may adjust this based on your display size
        margin=dict(l=100, r=100, b=100, t=100, pad=4)
    )

    # Adjust the tick angle and font size to prevent overlap
    for i in range(len(dimensions)):
        fig.update_xaxes(tickangle=45, tickfont=dict(size=10), row=i+1, col=1)
        fig.update_yaxes(tickangle=45, tickfont=dict(size=10), row=1, col=i+1)

    # Add colorbar to the right side of the plot
    fig.update_layout(coloraxis_colorbar=dict(
        title="Function Value",
        thicknessmode="pixels", thickness=40,
        lenmode="pixels", len=400,
        ticks="outside", ticksuffix="",
        dtick=(max(y_list) - min(y_list))/10
    ))

    fig.show()

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