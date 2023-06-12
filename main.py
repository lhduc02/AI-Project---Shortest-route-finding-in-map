from io import BytesIO
import pygame
import requests
import math
from queue import PriorityQueue

""" Khai báo """
h = [269, 247, 276, 254, 284, 236, 291, 271, 219, 254, 309, 210, 225, 234, 265, 294, 161, 225, 274, 177, 216, 243, 282, 316, 284, 159, 216, 250, 306, 186, 204, 226, 247, 263, 283, 304, 154, 169, 195, 207, 231, 260, 282, 308, 168, 177, 270, 289, 291, 297, 314, 139, 155, 170, 169, 182, 222, 303, 348, 354, 394, 136, 190, 228, 265, 314, 368, 402, 393, 416, 374, 380, 326, 280, 275, 127, 133, 146, 197, 214, 287, 353, 343, 388, 363, 297, 306, 310, 316, 324, 246, 260, 267, 277, 283, 282, 291, 218, 207, 181, 175, 183, 190, 196, 195, 211, 191, 223, 226, 209, 219, 214, 216, 204, 251, 257, 237, 215, 220, 230, 222, 237, 243, 250, 181, 195, 159, 241, 232, 245, 229, 191, 144, 96, 102, 94, 165, 162, 181, 194, 221, 238, 192, 239, 119, 75, 152, 190, 235, 232, 184, 146, 101, 141, 229, 198, 136, 96, 96, 135, 131, 179, 192, 223, 242, 129, 92, 87, 87, 128, 122, 121, 172, 221, 219, 239, 236, 246, 271, 262, 278, 292, 244, 220, 173, 105, 312, 332, 335, 212, 156, 170, 175, 214, 212, 276, 272, 300, 350, 359, 351, 362, 260, 243, 260, 287, 326, 239, 207]
t = [21, 29, 29, 33, 34, 43, 42, 48, 60, 62, 62, 67, 67, 80, 73, 73, 85, 86, 83, 96, 95, 93, 86, 87, 96, 106, 105, 100, 99, 117, 116, 114, 113, 113, 116, 120, 129, 125, 125, 123, 126, 124, 127, 123, 136, 147, 136, 129, 135, 144, 130, 173, 171, 165, 172, 162, 157, 157, 151, 137, 136, 187, 185, 170, 167, 166, 155, 141, 158, 157, 163, 167, 174, 177, 179, 206, 224, 234, 201, 200, 188, 187, 191, 179, 201, 198, 206, 216, 218, 229, 206, 213, 221, 229, 239, 251, 260, 217, 221, 212, 224, 232, 229, 227, 219, 231, 249, 240, 246, 252, 256, 256, 253, 259, 272, 282, 282, 290, 309, 315, 316, 344, 343, 367, 350, 359, 339, 368, 366, 380, 378, 369, 360, 344, 374, 384, 383, 394, 392, 394, 399, 420, 407, 430, 407, 389, 424, 434, 446, 460, 446, 440, 441, 454, 471, 474, 463, 457, 470, 470, 480, 484, 486, 491, 507, 489, 480, 486, 495, 497, 508, 516, 525, 527, 537, 527, 541, 544, 529, 539, 551, 566, 557, 553, 543, 561, 582, 581, 596, 584, 580, 584, 594, 593, 602, 604, 620, 609, 604, 601, 625, 624, 367, 467, 509, 544, 566, 303, 132]

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10, 10, 11, 12, 12, 13, 15, 15, 16, 17, 17, 18, 18, 19, 19, 20, 23, 24, 25, 26, 26, 27, 29, 30, 31, 32, 33, 33, 35, 36, 36, 37, 37, 38, 39, 40, 42, 42, 43, 43, 44, 45, 45, 46, 46, 47, 48, 49, 50, 50, 52, 54, 54, 56, 57, 57, 58, 59, 60, 61, 61, 62, 63, 63, 64, 65, 66, 66, 67, 68, 68, 69, 70, 71, 72, 72, 73, 73, 74, 74, 75, 76, 77, 78, 79, 79, 80, 81, 81, 82, 82, 83, 84, 85, 86, 86, 87, 87, 88, 88, 89, 90, 91, 92, 92, 93, 94, 95, 96, 97, 98, 99, 99, 101, 102, 103, 104, 106, 106, 107, 108, 109, 109, 110, 110, 111, 111, 112, 112, 114, 115, 115, 116, 118, 119, 119, 119, 119, 120, 120, 120, 121, 121, 121, 123, 124, 124, 125, 125, 125, 126, 127, 128, 128, 129, 130, 131, 131, 132, 134, 135, 135, 137, 137, 138, 139, 140, 140, 142, 142, 143, 144, 145, 145, 147, 147, 148, 148, 149, 150, 150, 151, 152, 153, 154, 154, 155, 156, 157, 157, 159, 160, 160, 161, 162, 162, 163, 165, 166, 166, 168, 169, 170, 171, 172, 172, 173, 173, 174, 175, 176, 177, 178, 179, 179, 179, 180, 181, 182, 182, 183, 184, 184, 186, 187, 187, 188, 189, 191, 192, 192, 194, 194, 196, 199, 199, 200, 203, 204, 205, 206]
arr_nei = [3, 4, 4, 6, 5, 13, 6, 7, 8, 9, 11, 10, 16, 12, 13, 14, 15, 24, 18, 20, 14, 19, 22, 23, 20, 26, 21, 33, 23, 28, 26, 25, 29, 34, 37, 38, 31, 35, 39, 40, 40, 41, 42, 43, 44, 48, 38, 52, 45, 40, 209, 47, 57, 47, 48, 49, 46, 53, 56, 209, 64, 49, 50, 51, 58, 62, 55, 56, 63, 64, 209, 74, 73, 67, 67, 68, 76, 64, 79, 91, 75, 73, 81, 71, 70, 71, 72, 84, 72, 82, 84, 83, 86, 75, 81, 91, 77, 78, 107, 99, 100, 98, 86, 92, 83, 85, 89, 85, 90, 87, 93, 88, 94, 89, 95, 90, 97, 98, 93, 108, 94, 95, 96, 97, 116, 99, 105, 106, 102, 103, 104, 105, 107, 108, 114, 109, 113, 115, 112, 113, 112, 113, 113, 114, 208, 116, 117, 208, 119, 120, 121, 125, 208, 121, 123, 208, 122, 125, 208, 124, 128, 203, 126, 127, 137, 129, 133, 129, 130, 131, 142, 132, 141, 139, 146, 136, 138, 138, 139, 147, 140, 141, 143, 143, 144, 148, 149, 146, 153, 148, 152, 149, 151, 150, 151, 155, 152, 154, 154, 156, 157, 156, 163, 158, 160, 161, 161, 162, 166, 163, 173, 164, 180, 167, 170, 170, 171, 171, 172, 173, 186, 175, 185, 175, 177, 177, 178, 183, 180, 205, 206, 181, 188, 183, 187, 184, 185, 190, 191, 189, 198, 199, 201, 192, 193, 194, 195, 196, 197, 200, 202, 207, 204, 205, 206, 207]


def khoang_cach(x1, x2, y1, y2):
    return math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0
    previous = {v: None for v in range(graph.v)}
    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                        previous[neighbor] = current_vertex
    return D, previous

def get_shortest_path(previous, target):
    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = previous[current_node]
    return list(reversed(path))


# Tạo graph
graph = Graph(210)
for i in range(len(arr)):
    a, b = arr[i], arr_nei[i]
    graph.add_edge(a, b, khoang_cach(h[a-1], h[b-1], t[a-1], t[b-1]))


""" Show map để chọn 2 điểm """
pygame.init()
size = [440, 660]
screen = pygame.display.set_mode(size)
link = "https://pbs.twimg.com/media/FxQz1h1aQAIRp94?format=png&name=900x900"
response = requests.get(link)
img = pygame.image.load(BytesIO(response.content))
img = pygame.transform.scale(img, (440, 660))
screen.blit(img, (0, 0))
pygame.display.set_caption("AI Project - Shortest route finding in map")

done = False
clock = pygame.time.Clock()


tung = []
hoanh = []

count, mem_a, mem_b, kc_a, kc_b = 0, 0, 0, 200, 200
min_a = []
min_b = []
path = []
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.WINDOWCLOSE:
            done = True
        if count >= 2:
            break
        
        if event.type == pygame.MOUSEBUTTONUP:
            if count >= 2:
                break
            hoanh.append(event.pos[0])
            tung.append(event.pos[1])
            count += 1
        
        if count == 2:
            path.append((hoanh[0], tung[0]))
            for i in range(208):
                min_a.append(khoang_cach(hoanh[0], h[i], tung[0], t[i]))
                min_b.append(khoang_cach(hoanh[1], h[i], tung[1], t[i]))
                mem_a = min_a.index(min(min_a))
                mem_b = min_b.index(min(min_b))
            
            D, previous = dijkstra(graph, mem_a+1)
            shortest_path = get_shortest_path(previous, mem_b+1)
            
            for i in shortest_path:
                i = int(i)
                path.append((h[i-1], t[i-1]))
            path.append((hoanh[1], tung[1]))
            #print(path)
            pygame.draw.lines(screen, (69, 98, 212), False, path, 5)
        
        elif event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
pygame.quit()

