import time

N = 100            # rozmiar tablicy
ITERATIONS = 100000  # liczba powtórzeń


def main():
    start = time.perf_counter()

    arr = [0] * N
    swaps = 0
    for _ in range(ITERATIONS):
        # wypełnij tablicę rosnąco: [1, 2, ..., N]
        for i in range(N):
            arr[i] = i + 1

        # sortowanie bąbelkowe malejąco (najgorszy przypadek: każde porównanie to zamiana)
        for i in range(N - 1):
            for j in range(N - 1 - i):
                if arr[j] < arr[j + 1]:
                    tmp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = tmp
                    swaps += 1

    elapsed = time.perf_counter() - start
    print(f"Pierwsze: {arr[0]}, {arr[1]}, {arr[2]} ... ostatnie: {arr[N - 1]}")
    print(f"Zamiany łącznie: {swaps}")
    print(f"Iteracje: {ITERATIONS}, czas: {elapsed * 1_000:.2f} ms")


if __name__ == "__main__":
    main()
