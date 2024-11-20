import sys

n, m = map(int, input().split())

pokemon = {}

for i in range(1,n+1):
    pokemon[f'{i}'] = sys.stdin.readline().strip()

pokemon_ = {k:v for v, k in pokemon.items()}

for _ in range(m):
    q = sys.stdin.readline().strip()
    if q in pokemon.keys():
        print(pokemon[f'{q}'])
    elif q in pokemon_.keys():
        print(pokemon_[f'{q}'])
    