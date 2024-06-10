
n = int(input())
cafes = list(map(int, input().split()))
cafes_freq = {}
cafes_last_index = {}
for index, cafe in enumerate(cafes):
    if cafe not in cafes_freq:
        cafes_freq[cafe] = 0
    cafes_freq[cafe] += 1
    cafes_last_index[cafe] = index
max_freq = 0
max_freq_cafe = -1
for cafe, freq in cafes_freq.items():
    if freq > max_freq or (freq == max_freq and cafes_last_index[cafe] < cafes_last_index[max_freq_cafe]):
        max_freq = freq
        max_freq_cafe = cafe
print(max_freq_cafe)

