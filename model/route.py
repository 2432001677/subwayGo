"""
为选择起点终点时提供线路下的站点名列表
为查询路线详情提供站点坐标,站点名及其开通状态
"""


class Route:
    def __init__(self, routes):
        self.routes = routes
        self.routes_name = list(routes)

    def get_stations_name(self, index):
        return [x[0] for x in self.routes.get(self.routes_name[index])]

    def get_pos(self, index):
        list = [str(x[1] + 1) for x in self.routes.get(self.routes_name[index])]
        list[0] = "始"
        list[-1] = "终"
        return list

    def get_stations_name_status(self, index):
        return [(x[0], "是" if x[2] == 1 else "否") for x in self.routes.get(self.routes_name[index])]
