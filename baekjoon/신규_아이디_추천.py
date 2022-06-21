def stage_1(id):
    rec_id = id.lower()
    return rec_id

def stage_2(id):
    rec_id = ''
    count = 0
    while count < len(id):
        if id[count] == '-':
            rec_id += id[count]
        elif id[count] == '_':
            rec_id += id[count]
        elif id[count] == '.':
            rec_id += id[count]
        elif ord(id[count]) >= ord('0') and ord(id[count]) <= ord('9'):
            rec_id += id[count]
        elif ord(id[count]) >= ord('a') and ord(id[count]) <= ord('z'):
            rec_id += id[count]
        count += 1
    return rec_id

def stage_3(id):
    rec_id = id[0]
    for i in range(1,len(id)):
        if rec_id[-1] != '.' or id[i] != '.':
            rec_id += id[i]
    return rec_id


new_id = "...!@BaT#*..y.abcdefghijklm" 
origin_id = new_id[:]
st1_id = stage_1(origin_id)
print('st1:' + str(st1_id))
st2_id = stage_2(st1_id)
print('st2:' + str(st2_id))
st3_id = stage_2(st2_id)
print('st3:' + str(st3_id))
print(st3_id[3])
answer = 0