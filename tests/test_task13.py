from src.task13 import foreign

def test_example():
    matrix = [[1.0, 2.0], [3.0, 4.0]]
    
    result = foreign.foreign_matrix_power(matrix, 3)
    expected = [[37.0, 54.0], [81.0, 118.0]]

    assert result == expected
