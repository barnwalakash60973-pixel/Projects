#Time complexity -> O(n^2)
def max_area_water(waterbox):
    cur_area = max_area = 0
    n = len(waterbox)
    for i in range(n):
        wt = 1
        for j in range(i+1, n):
            ht = min(waterbox[i], waterbox[j])
            cur_area = ht * wt
            wt += 1
            max_area = max(cur_area, max_area)
    return max_area

waterbox = [1,8,6,2,5,4,8,3,7]
result = max_area_water(waterbox)
print(result)

#==============================================

#fast approach same problem -> Time complexity - O(n)
def water_box_area(box):
    cur_area = max_area = 0
    lt = wt = ht = 0
    rt = len(box) - 1
    while(rt > lt):
        wt = rt - lt
        ht = min(box[rt], box[lt])
        cur_area = ht * wt
        max_area = max(max_area, cur_area)

        if box[rt] > box[lt]:
            lt += 1
        else:
            rt -= 1
    return max_area

box = [1,8,6,2,5,4,8,3,7]

result = water_box_area(box)

print(result)                   