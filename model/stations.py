import os
import pickle


class Station:  # 站点对象
    def __init__(self, subway, key, inf):
        self.subway = subway  # 地铁系统名
        self.name = key  # 站点名
        self.inf = {x[0]: x[1] for x in inf}  # 这个站点所属的线路:(坐标,开通状态)
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
        for r in self.routes.keys():  # 判定是否同一环
            if r == k:
                continue
            r2 = [x[0] for x in reversed(self.routes[r])]
            for i in route:
                if not (i in r2):
                    break
            else:
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
        return value

    def is_open(self) -> bool:
        for (route, j) in self.inf.items():
            if j[1] == 1:
                return True
        return False

    def get_past_stations(self, other):
        self - other
        route, s = self.min_line, []
        route_inf = self.routes[self.min_line]
        route_stations = [x[0] for x in route_inf]

        if self.inf[route][0] < other.inf[route][0]:
            s.extend(route_stations[self.inf[route][0]:other.inf[route][0]])
            s.append(other.name)
        else:
            if self._is_circle(self.min_line):
                s.extend(route_stations[self.inf[route][0]:])
                s.extend(route_stations[:other.inf[route][0] + 1])
            else:
                s.extend(route_stations[other.inf[route][0]:self.inf[route][0]])
                s.append(self.name)
                s = list(reversed(s))
        res = route + ": " + "->".join(s)

        return res
