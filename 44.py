def is_pent_num(x):
    if ((1/6)*((24 * x + 1)**(1/2) + 1)).is_integer():
        return True;
    return False

pentagon_nums = [n * (3 * n - 1) / 2 for n in range(1, 5000)]
min_diff = 2.0**50
for j in range(0, 4999):
	j_val = pentagon_nums[j]
	for k in range(j + 1, 4999):
		k_val = pentagon_nums[k]
		if is_pent_num(j_val + k_val) and \
				is_pent_num(k_val - j_val) and k_val - j_val < min_diff:
			min_diff = k_val - j_val
print(min_diff)
