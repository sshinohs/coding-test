not_self = []
for ii in range(1,10001):
    ii_str = str(ii)
    len_ii = len(ii_str)
    output = ii
    for jj in range(len_ii):
        output = output + int(ii_str[jj])
    not_self.append(output)

for ii in range(1,10001):
    if ii not in not_self:
        print(ii)