# Count how many instances of each first name in the names.txt file and print the results.
from collections import Counter


def main():
    with open("names.txt", "r", encoding="utf-8") as f:
        names = f.read().splitlines()

    first_names = [name.split()[0].capitalize() for name in names if name]
    counts = Counter(first_names)
    
    with open("name_counts.txt", "w", encoding="utf-8") as f:

        for name, count in counts.most_common():
            f.write(f"{name}: {count}\n")

if __name__ == "__main__":
    main()