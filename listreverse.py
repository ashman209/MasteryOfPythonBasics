# 11-93 Listing 10.10: listreverse.py
def ref(lst):
    return [] if len(lst) == 0 else ref(lst[1:]) + lst[0:1]

print(ref([1, 2, 3, 4, 5, 6, 7]))
