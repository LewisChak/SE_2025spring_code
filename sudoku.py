def get_box_range(row, col):
    """获取单元格所在的3x3宫格的起始行和列"""
    return (row // 3) * 3, (col // 3) * 3

def last_remaining_cell_inference(grid):
    """
    实现Last Remaining Cell策略
    :param grid: 9x9数独棋盘，0表示空格
    :return: 9x9的二维数组，每个元素是该单元格的可能数字列表
    """
    # 首先获取所有单元格的候选数字
    candidates = possible_number_inference(grid)
    
    # 检查每个数字(1-9)在行、列、宫中的唯一可能位置
    for num in range(1, 10):
        # 检查行
        for i in range(9):
            possible_cols = [j for j in range(9) if num in candidates[i][j]]
            if len(possible_cols) == 1:
                j = possible_cols[0]
                if grid[i][j] == 0:  # 确保是空格
                    candidates[i][j] = [num]  # 确定为该数字
        
        # 检查列
        for j in range(9):
            possible_rows = [i for i in range(9) if num in candidates[i][j]]
            if len(possible_rows) == 1:
                i = possible_rows[0]
                if grid[i][j] == 0:
                    candidates[i][j] = [num]
        
        # 检查宫
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                possible_positions = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if num in candidates[i][j]:
                            possible_positions.append((i, j))
                if len(possible_positions) == 1:
                    i, j = possible_positions[0]
                    if grid[i][j] == 0:
                        candidates[i][j] = [num]
    
    return candidates

def possible_number_inference(grid):
    """
    实现Possible Number策略，确定每个空格的候选数字
    :param grid: 9x9数独棋盘，0表示空格
    :return: 9x9的二维数组，每个元素是该单元格的可能数字列表
    """
    candidates = [[[] for _ in range(9)] for _ in range(9)]  # 初始化9x9空列表
    
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                candidates[i][j] = []  # 已填数字没有候选
            else:
                # 检查同行
                row_numbers = {grid[i][c] for c in range(9) if grid[i][c] != 0}
                # 检查同列
                col_numbers = {grid[r][j] for r in range(9) if grid[r][j] != 0}
                # 检查同宫
                box_row, box_col = get_box_range(i, j)
                box_numbers = {
                    grid[r][c] 
                    for r in range(box_row, box_row + 3) 
                    for c in range(box_col, box_col + 3) 
                    if grid[r][c] != 0
                }
                
                # 合并所有已存在数字
                existing_numbers = row_numbers | col_numbers | box_numbers
                
                # 可能的数字是1-9中不在existing_numbers的数字
                candidates[i][j] = [num for num in range(1, 10) if num not in existing_numbers]
    
    return candidates

# 示例用法
if __name__ == "__main__":
    # 示例数独，0表示空格
    example_grid = [
        [6, 3, 5, 9, 4, 7, 2, 8, 1],
        [7, 4, 8, 1, 5, 2, 9, 3, 6],
        [2, 1, 9, 0, 0, 3, 5, 4, 0],
        [4, 7, 6, 3, 0, 0, 0, 0, 0],
        [8, 9, 3, 0, 0, 0, 7, 0, 0],
        [1, 5, 2, 0, 0, 0, 0, 9, 3],
        [3, 6, 1, 0, 8, 5, 0, 0, 9],
        [9, 8, 7, 0, 0, 0, 0, 6, 0],
        [5, 2, 4, 0, 1, 9, 0, 0, 0]
    ]
    
    possible_candidates = possible_number_inference(example_grid)
    last_remaining_candidates = last_remaining_cell_inference(example_grid)
    print("Possible Candidates:")
    print(possible_candidates[2][3])  
    print("Last Remaining Candidates:")
    print(last_remaining_candidates[2][3])  