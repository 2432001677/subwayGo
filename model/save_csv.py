import csv


def read_sub():  # 输入线路名，开通状态，站点
    list = input().split()
    return list[0], list[1], list[2:]


def create_csv(name, sum_csv):
    path = "../res/" + name + ".csv"
    with open(path, 'w', encoding="utf-8", newline='') as f:
        csv_write = csv.writer(f)
        for key in sum_csv:
            row = [key, sum_csv[key]]
            csv_write.writerow(row)


if __name__ == '__main__':
    subway = input("输入地铁系统名")
    n = int(input("输入条数"))
    station_map = {}
    for i in range(n):
        name, status, list = read_sub()
        for j, sta in enumerate(list):
            if sta in station_map:
                station_map[sta] += " " + name + "," + str(j) + "," + status
            else:
                station_map[sta] = name + "," + str(j) + "," + status
    create_csv(subway, station_map)
