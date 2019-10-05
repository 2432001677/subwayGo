from model.caches import SubwayCache

sub=SubwayCache("北京")
# for i in sub.stations:
#     print(i,sub.stations[i])
# for i in sub.lines:
#     print(i,sub.lines[i])
q=sub.lines["2号线外环"]
w=sub.lines["2号线内环"]
print(q)
print(w)

