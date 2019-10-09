from model.subway_caches import SubwayCache
from controller.subway_control import SubwayControl
import heapq

sub = SubwayCache("北京")
# for i in sub.stations:
#     print(i,sub.stations[i])

b=sub.get_station("巴沟")
c=sub.get_station("知春里")
c-b
print(c.min_line)
# print(b)
# for i in sub.lines:
#     print(i,sub.lines[i])
# q=sub.lines["3号线"]
# w=sub.lines["2号线内环"]
# print(q)
# print(w)
# b={"3":2,"ds":1,"fd":1}
# print({x:x for x in b})

