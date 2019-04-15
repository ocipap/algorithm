arr = [-1]*26
s = input()
for i in range(0, len(s)):
    if arr[ord(s[i]) - 97] == -1 :
        arr[ord(s[i]) - 97] = i

arr = list(map(str, arr))
print(" ".join(arr))