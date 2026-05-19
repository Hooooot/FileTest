
def create(name: str, size: int):
    with open(name, "wb") as f:
        f.write(b"\xC8" * size)

create("1mb.bin", 1 * 1024 * 1024)
create("2mb.bin", 2 * 1024 * 1024)
create("3mb.bin", 3 * 1024 * 1024)
create("5mb.bin", 5 * 1024 * 1024)
create("10mb.bin", 10 * 1024 * 1024)
create("20mb.bin", 20 * 1024 * 1024)
create("30mb.bin", 30 * 1024 * 1024)
create("50mb.bin", 50 * 1024 * 1024)
create("100mb.bin", 100 * 1024 * 1024)