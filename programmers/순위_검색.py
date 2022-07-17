def solution(info, query):
    
    table = [['-', 'cpp', 'java', 'python'], ['-', 'backend', 'frontend'],
             ['-', 'junior', 'senior'], ['-', 'chicken', 'pizza']]
    
    info_dict = {}
    
    code = [0,0,0,0]
    for i in range(4):
        code[0] = str(i)
        for j in range(3):
            code[1] = str(j)
            for m in range(3):
                code[2] = str(m)
                for n in range(3):
                    code[3] = str(n)
                    code_str = ''.join(code)
                    info_dict[code_str] = []
                    
    
    for row in info:
        row = row.split(' ')
        code_arr = []
        for i in range(len(table)):
            code_arr.append(['0', str(table[i].index(row[i]))])
        code = [0,0,0,0]
        for i in range(2):
            code[0] = code_arr[0][i]
            for j in range(2):
                code[1] = code_arr[1][j]
                for m in range(2):
                    code[2] = code_arr[2][m]
                    for n in range(2):
                        code[3] = code_arr[3][n]
                        code_result = ''.join(code)
                        if code_result in info_dict:
                            info_dict[code_result].append(int(row[4]))
                        else:
                            info_dict[code_result] = [int(row[4])]
    
    for key in info_dict.keys():
        info_dict[key] = sorted(info_dict[key])
    
    answer = []
    for quer in query:
        quer = quer.split(' and ')
        temp = quer[3].split(' ')
        quer.pop()
        quer.append(temp[0])
        score = int(temp[1])
        code_query = ''
        
        for i in range(len(table)):
            code_query += str(table[i].index(quer[i]))
        
        info_dict[code_query]
        
        arr = info_dict[code_query]
        
        st = 0
        tmp = len(arr)
        ed = tmp - 1
        
        while st <= ed:
            mid = (st + ed) // 2
            
            if score <= arr[mid]:
                tmp = mid
                ed = mid - 1
            else:
                st = mid + 1
        
        answer.append(len(arr) - tmp)
            
        
    return answer
    
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))