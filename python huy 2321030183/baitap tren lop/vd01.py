from pathlib import Path


def prime_divisors(n: int) -> list[int]:
    """Trả về danh sách ước nguyên tố khác nhau của n, theo thứ tự tăng dần."""
    divisors = []
    if n % 2 == 0:
        divisors.append(2)
        while n % 2 == 0:
            n //= 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            divisors.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        divisors.append(n)
    return divisors


def main() -> None:
    input_path = Path(__file__).resolve().parent / "input.txt"
    output_path = Path(__file__).resolve().parent / "output.txt"

    if not input_path.exists():
        print(f"Không tìm thấy tệp dữ liệu: {input_path}")
        return

    lines = input_path.read_text(encoding="utf-8").strip().splitlines()
    results = []

    for line in lines:
        line = line.strip()
        if not line:
            results.append("")
            continue

        try:
            value = int(line)
            if value < 0:
                raise ValueError
        except ValueError:
            results.append("")
            continue

        divisors = prime_divisors(value)
        results.append(" ".join(str(x) for x in divisors))

    output_path.write_text("\n".join(results), encoding="utf-8")
    print(f"Đã ghi kết quả vào: {output_path}")


if __name__ == "__main__":
    main()
