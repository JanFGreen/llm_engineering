use std::hint::black_box;
use std::time::Instant;

const N: usize = 100; // rozmiar tablicy
const ITERATIONS: usize = 100000; // liczba powtórzeń

fn main() {
    let start = Instant::now();

    let mut arr = [0i64; N];
    let mut swaps: u64 = 0;
    for _ in 0..ITERATIONS {
        // wypełnij tablicę rosnąco: [1, 2, ..., N]
        for i in 0..N {
            arr[i] = black_box(i as i64 + 1);
        }

        // sortowanie bąbelkowe malejąco (najgorszy przypadek: każde porównanie to zamiana)
        for i in 0..N - 1 {
            for j in 0..N - 1 - i {
                if arr[j] < arr[j + 1] {
                    let tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                    swaps += 1;
                }
            }
        }
        black_box(&arr);
    }

    let elapsed = start.elapsed();
    println!("Pierwsze: {}, {}, {} ... ostatnie: {}", arr[0], arr[1], arr[2], arr[N - 1]);
    println!("Zamiany łącznie: {}", swaps);
    println!("Iteracje: {}, czas: {:.2} ms", ITERATIONS, elapsed.as_secs_f64() * 1_000.0);
}
