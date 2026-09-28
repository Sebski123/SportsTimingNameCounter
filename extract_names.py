from pathlib import Path

from bs4 import BeautifulSoup


def extract_names(page_html):
    """Return the names from the main table in the page HTML."""
    soup = BeautifulSoup(page_html, "html.parser")
    table = soup.select_one("#mainBody div:nth-of-type(2) div:nth-of-type(1) div div table")
    if not table:
        return []

    names = []
    for span in table.select("tr td:nth-of-type(2) a span"):
        value = span.get_text(" ", strip=True)
        if value:
            names.append(value)
    return names


def main():
    pages_dir = Path(__file__).resolve().parent / "pages"
    if not pages_dir.exists():
        print(f"No saved pages directory found at: {pages_dir}")
        return

    for page_path in sorted(pages_dir.iterdir()):
        if not page_path.is_file():
            continue

        page_html = page_path.read_text(encoding="utf-8", errors="ignore")
        names = extract_names(page_html)
        print(f"Page: {page_path.name}")
        with open("names.txt", "a", encoding="utf-8") as f:
            for name in names:
                f.write(name + "\n")



if __name__ == "__main__":
    main()


