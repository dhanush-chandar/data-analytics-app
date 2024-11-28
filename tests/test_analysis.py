import pytest
import pandas as pd
from unittest.mock import patch

# Define the function in the test file
def test_run_analysis():
    # Load data
    data = pd.read_csv('data/sample.csv')
    
    # Perform analysis (e.g., calculate mean)
    mean_value = data['value'].mean()

    return {'mean': mean_value}

# Mock the pd.read_csv function to simulate loading a CSV
@patch("pandas.read_csv")
def test_run_analysis(mock_read_csv):
    # Define mock data that would be returned by pd.read_csv
    mock_data = pd.DataFrame({
        'value': [10, 20, 30, 40, 50]
    })

    # Set the mock to return the mock data
    mock_read_csv.return_value = mock_data

    # Call the function
    result = run_analysis()

    # Assert that the mean value is calculated correctly
    assert result['mean'] == 30  # (10 + 20 + 30 + 40 + 50) / 5 = 30
