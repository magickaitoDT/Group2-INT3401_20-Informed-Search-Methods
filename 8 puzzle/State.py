class State:
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0] #hàm mục tiêu
    
    greedy_evaluation = None
    AStar_evaluation = None
    heuristic = None
    def __init__(self, state, parent, direction, depth, cost):
        self.state = state #trạng thái hiện tại
        self.parent = parent #trạng thái gốc
        self.direction = direction
        self.depth = depth

        if parent: #nếu parent được sử dụng
            self.cost = parent.cost + cost

        else:
            self.cost = cost

            
            
    def test(self): #kiểm tra xem trạng thái hiện tại có phải là trạng thái mục tiêu hay không?
        if self.state == self.goal:
            return True
        return False
        
    #tính toán khoảng cách manhattan
    def Manhattan_Distance(self ,n): 
        self.heuristic = 0
        for i in range(1 , n*n):
            distance = abs(self.state.index(i) - self.goal.index(i)) 
            
            #hàm đánh giá
            self.heuristic = self.heuristic + distance/n + distance%n 
            
        self.greedy_evaluation = self.heuristic    
        self.AStar_evaluation = self.heuristic + self.cost #f=g+h
        
        return( self.greedy_evaluation, self.AStar_evaluation)               
                    


    @staticmethod
    
    #loại bỏ các nước di chuyển bất lợi
    def available_moves(x,n): 
        moves = ['Left', 'Right', 'Up', 'Down'] #list này chứa toàn bộ các nước di chuyển có thể xảy ra
        if x % n == 0: #khoảng trống ở cột trái
            moves.remove('Left') #loại bỏ phương án dịch trái
        if x % n == n-1: #khoảng trống ở cột phải
            moves.remove('Right') #loại bỏ phương án dịch phải
        if x - n < 0: #khoảng trống ở hàng trên
            moves.remove('Up') #loại bỏ phương án dịch lên
        if x + n > n*n - 1: #khoảng trống ở hàng dưới
            moves.remove('Down') #loại bỏ phương án dịch xuống

        return moves #trả về phương án dịch chuyển khả thi

    #xét các trạng thái lân cận
    def expand(self , n): 
        x = self.state.index(0)
        moves = self.available_moves(x,n)
        
        children = []#lưu trữ các lân cận
        for direction in moves: #thử các phương án dịch chuyển khả thi có trong moves
            temp = self.state.copy()

            #hoán đổi vị trí
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]
        
        
            children.append(State(temp, self, direction, self.depth + 1, 1)) #thêm các lân cận và truyền thêm các thuộc tính 
        return children #trả về các lân cận có thể đạt được từ trạng thái đang xét 

    
    #xét trạng thái hiện tại và trả về hướng di chuyển, xét đến khi nào không còn parent
    def solution(self):
        solution = [] #lưu trữ các hướng giải quyết
        solution.append(self.direction) #thêm trạng thái hiện tại vào danh sách
        path = self 
        while path.parent != None: #dò ngược lại các parent
            path = path.parent 
            solution.append(path.direction)
        solution = solution[:-1] #xóa đi phần tử cuối
        solution.reverse() #đảo ngược lại list
        return solution #trả về tập phương án
         