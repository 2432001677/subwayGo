import os
import pickle


class Station:  # 站点对象
    def __init__(self, subway, key, inf):
        self.subway = subway  # 地铁系统名
        self.name = key  # 站点名
        self.inf = {x[0]: x[1] for x in inf}  # 线路:(坐标,开通状态)
        self.routes = None

    def __contains__(self, item):
        for line in self.inf.keys():
            if line == item:
                return True
        return False

    def _is_circle(self, route1, route2) -> bool:
        if not self.routes:
            with open(os.getcwd()+"/res/" + self.subway + "/lines.pk", 'rb') as f:
                self.routes = pickle.load(f)
        route1 = [x[0] for x in self.routes[route1]]
        route2 = [x[0] for x in reversed(self.routes[route2])]
        return route1 == route2

    def __sub__(self, other):
        value = 9999
        min_line = None
        for line in self.inf.keys():
            if self.inf[line][1] == 0:
                continue
            if line in other and other.inf[line][1] == 1:
                t = self.inf[line][0] - other.inf[line][0]
                t = t if t > 0 else -t
                if t < value:
                    value = t
                    min_line = line
                elif t == value and self._is_circle(min_line, line):  # 解决要命的特殊情况——环路问题
                    temp = len(self.routes[line]) - value
                    if value <= temp:
                        if self.inf[line][0] - other.inf[line][0] < 0:
                            min_line = line
                    else:
                        value = temp
                        if self.inf[line][0] - other.inf[line][0] > 0:
                            min_line = line
        return value

