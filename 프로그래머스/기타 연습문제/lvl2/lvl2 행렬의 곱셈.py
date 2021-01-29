def solution(arr1, arr2):
    answer = list(list())
    
    for i in range(len(arr1)):
        row_data = list()
        for j in range(len(arr2[0])):
            value = 0
            for k in range(len(arr2)):
                value += arr1[i][k] * arr2[k][j]
            row_data.append(value)
        answer.append(row_data)
        
    return answer