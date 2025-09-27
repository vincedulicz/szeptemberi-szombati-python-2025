
parosok = [x for x in range(1, 21) if x % 2 == 0]

print(parosok)

szavak = ["alma", "körte", "barack"]
nagybetus = [s.upper() for s in szavak]

print(f"eredeti lista: {szavak} | nagybetűs: {nagybetus}")

negyzet_dict = {x: x**2 for x in range(1, 6)}
print(negyzet_dict)

print(negyzet_dict.keys())
print(negyzet_dict.values())
print(negyzet_dict.items())


hossz_dict = {s: len(s) for s in szavak}
print(hossz_dict)


paros_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(paros_dict)