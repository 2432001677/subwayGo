import os
import pickle


class Station:  # 站点对象
    def __init__(self, subway, key, inf):
        self.subway = subway  # 地铁系统名
        self.name = key  # 站点名
        self.inf = {x[0]: x[1] for x in inf}  # 线路:(坐标,开通状态)
        self.routes = None
        self.min_line = ""
        self.circle = {}

    def __contains__(self, item):
        for line in self.inf.keys():
            if line == item:
                return True
        return False

    def _is_circle(self, route) -> bool:
        k = route
        if not self.routes:
            with open(os.getcwd() + "/res/" + self.subway + "/lines.pk", 'rb') as f:
                self.routes = pickle.load(f)
        route = [x[0] for x in self.routes[route]]
        for r in self.routes.keys():
            r2 = [x[0] for x in reversed(self.routes[r])]  # 判定是否同一环
            if route == r2:
                self.circle[k] = r
                self.circle[r] = k
                return True
        return False

    def __sub__(self, other):
        value = 9999
        self.min_line = ""
        for line in self.inf.keys():
            if self.inf[line][1] == 0 or line == self.min_line:
                continue
            if line in other and other.inf[line][1] == 1:
                t = self.inf[line][0] - other.inf[line][0]
                if self._is_circle(line):
                    if t < 0:
                        t = -t
                        if 2 * t > len(self.routes[line]):
                            t = len(self.routes[line]) - t
                            if t < value:
                                value = t
                                self.min_line = self.circle[line]
                        else:
                            if t < value:
                                value = t
                                self.min_line = line
                    else:
                        if 2 * t > len(self.routes[line]):
                            t = len(self.routes[line]) - t
                            if t < value:
                                value = t
                                self.min_line = line
                        else:
                            if t < value:
                                value = t
                                self.min_line = self.circle[line]
                else:
                    t = t if t > 0 else -t
                    if t < value:
                        value = t
                        self.min_line = line
                # elif t == value and self._is_circle(self.min_line, line):  # 解决要命的特殊情况——环路问题
                #     temp = len(self.routes[line]) - value
                #     if value <= temp:
                #         if self.inf[line][0] - other.inf[line][0] < 0:
                #             self.min_line = line
                #     else:
                #         value = temp
                #         if self.inf[line][0] - other.inf[line][0] > 0:
                #             self.min_line = line
        return value

    def is_open(self) -> bool:
        for (route, j) in self.inf.items():
            if j[1] == 1:
                return True
        return False

    def get_past_stations(self, other):
        num = self - other
        print(num,self.min_line)
        rs = []
        for route in self.inf.keys():
            if route in other:
                rs.append(route)
        if len(rs) == 1:
            routes = rs[0]
        else:
            t = self.inf[rs[0]][0] - other.inf[rs[0]][0]
            if t < 0:
                if -2 * t <= len(self.routes):
                    rs = rs[0]
                else:
                    rs = rs[1]
