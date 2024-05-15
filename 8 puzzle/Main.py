from Search_Algorithms import AStar_search

#khởi tạo trạng thái ban đầu
n = 3
print("Enter your" ,n,"*",n, "puzzle") 
root = []
for i in range(0,n*n):
    p = int(input())
    root.append(p)

print("The given state is:", root)


#tính toán tổng N    
def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv

#xét xem có giải được trạng thái ban đầu này không: nếu như N lẻ thì không giải được
def solvable(puzzle):
    inv_counter = inv_num(puzzle)
    if (inv_counter %2 ==0):
        return True
    return False


#1,8,2,0,4,3,7,6,5 giải được
#2,1,3,4,5,6,7,8,0 không giải được


if solvable(root):
    print("Solvable, please wait. \n")
    AStar_solution = AStar_search(root, n)
    print('A* Solution is ', AStar_solution[0]) #trả về phương án dịch chuyển
    print('Number of explored nodes is ', AStar_solution[1]) #trả về số trạng thái đã duyệt 
    
else:
    print("Not solvable")