from State import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue

def AStar_search(given_state , n):
    frontier = PriorityQueue() #xác định độ ưu tiên trong hàng chờ
    explored = [] #mảng dùng để lưu trữ các trường hợp đã xét
    counter = 0
    root = State(given_state, None, None, 0, 0)
    evaluation = root.Manhattan_Distance(n) #tính toán hàm đánh giá A* cho trạng thái xuất phát
    frontier.put((evaluation[1], counter, root)) #dựa theo hàm đánh giá A*

    while not frontier.empty(): #khi vẫn còn trạng thái cần xét 
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state) #thêm nút hiện tại vào close
        
        if current_node.test(): #kiểm tra xem trạng thái hiện tại có phải là trạng thái đích hay không
            return current_node.solution(), len(explored) #trả về lời giải và số lượng trạng thái đã duyệt 

        children = current_node.expand(n) #xét các lân cận của nút vừa xét
        for child in children:
            if child.state not in explored: #nếu lân cận đó chưa được đưa vào close
                counter += 1 #tăng thêm bộ đếm
                evaluation = child.Manhattan_Distance(n) #sử dụng hàm đánh giá A* cho lân cận
                frontier.put((evaluation[1], counter, child)) #thêm lân cận vào frontier
    return