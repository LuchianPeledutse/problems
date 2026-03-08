_, M = tuple(int(num) for num in input().split(" "))
nums = [int(num) for num in input().split(" ")]


def alg(gold_list: list[int], M: int) -> int:
    """
    len(gold_list) 1 <= N <= 100
    max load 1 <= M <= 10_000
    gold_list item 1 <= m_i <= 100
    """
    weight_dict = {weight: 0 for weight in range(0, M + 1)} # O(M) mem
    weight_set = {0} # O(2^N)
    for gold_weight in gold_list: # c_0*2^0 + c_1*2^1 + ... + c_N*2^N O(2^N)
        for weight in list(weight_set): # 2^n
            weight_set.add(weight + gold_weight)
        for weight in weight_set:
            try:
                weight_dict[weight]
                weight_dict[weight] = 1
            except KeyError:
                pass
    return max(list(filter(lambda tup: tup[1] == 1, (key_val for key_val in weight_dict.items()))), key = lambda item: item[0])[0] 


# O(2^N + M) memory
# O(2^N + M) speed

if __name__ == "__main__":
    result = alg(nums, M)
    print(result)