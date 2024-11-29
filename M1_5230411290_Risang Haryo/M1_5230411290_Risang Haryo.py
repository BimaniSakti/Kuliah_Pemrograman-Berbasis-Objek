# luas bangun ruang 2d (Segitiga)
luasSegitiga = lambda a=float, t=float : (a*t)/2

# Volume bangun ruang 3d (Prisma Segitiga)
volumePrisma = lambda a=float, t=float, T=float : luasSegitiga(a, t) * T 

print(f"Luas Segitiga           : {luasSegitiga(2, 4)}")
print(f"Volume Prisma Segitiga  : {volumePrisma(2, 4, 9)}")