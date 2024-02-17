# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra: ")).upper().strip()

if letra in "A, E, I, O, U":
    print(f"A letra ´{letra}´ é vogal.")
elif letra in "B, C, D, F, G, J, K, H, L, M, N, P, Q, R, S, T, V, W, Y, X, Z":
    print(f"A letra ´{letra}´ é consoante.")
else:
    print(f"A ´{letra}´ não é letra.")