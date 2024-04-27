def pascal_triangle(n):
    if n <= 0:
        return []
    result = [[1]]
    for i in range(2, n+1):
        row = [1] + [result[i-2][j-1] + result[i-2][j] for j in range(1, i)] + [1]
        result.append(row)
    return result
