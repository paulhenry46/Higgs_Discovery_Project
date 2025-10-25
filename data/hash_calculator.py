import zlib
import sys

def calculate_adler32(filepath):
    """Calculates the Adler-32 checksum of a file."""
    # Initialize Adler-32 checksum
    adler_value = 1

    try:
        with open(filepath, 'rb') as f:
            while True:
                # Read 64KB block by block
                data = f.read(65536)
                if not data:
                    break
                # Update the checksum with the new block of data
                adler_value = zlib.adler32(data, adler_value)

            # Ensure the value is treated as an unsigned 32-bit integer
            if adler_value < 0:
                adler_value += 2**32

            # Print the result in hexadecimal format (e.g., 'c09d0234')
            print(f"{adler_value:08x}")

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    calculate_adler32(sys.argv[1])
