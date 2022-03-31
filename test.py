minim = 20
min_x = 1000
min_y = 1000
for x in range(1, 20):
    for y in range(1, 20):
        minim = min(minim, x / 30 + y / 50 + ((4 - x)**2 + (15 - y)**2)**0.5) / 30

print(minim)