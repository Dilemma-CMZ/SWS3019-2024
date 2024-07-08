def point_in_polygon(point, polygon):
    """
    判断一个点是否在多边形内部
    
    参数:
    point (tuple): 待测点的坐标 (x, y)
    polygon (list): 多边形顶点坐标列表 [(x1, y1), (x2, y2), ...]
    
    返回:
    bool: True 表示点在多边形内部, False 表示点在多边形外部
    """
    x, y = point
    inside = False
    
    # 遍历多边形的每条边
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        
        # 检查射线是否与边相交
        if (p1[1] > y) != (p2[1] > y):
            at = (p2[0] - p1[0]) * (y - p1[1]) / (p2[1] - p1[1]) + p1[0]
            if at > x:
                inside = not inside
    
    return inside

# 多边形顶点坐标
polygon = [(0, 0), (0, 10), (5, 5), (10, 10), (11, 10), (11, 1)]

# 测试点坐标
point1 = (5, 6)  # 在多边形内部
point2 = (5, 4) # 在多边形外部
point3 = (8, 0.73)
point4 = (8, 0.71)

print(point_in_polygon(point1, polygon))  # True
print(point_in_polygon(point2, polygon))  # False
print(point_in_polygon(point3, polygon))  # False
print(point_in_polygon(point4, polygon))  # True