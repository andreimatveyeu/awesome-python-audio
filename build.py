import pandas as pd

def main():
    df = pd.read_csv("dataframe.csv", index_col=[0])

    with open("head.md", "r") as inp:
        out = inp.read()

    for category in df.category.unique():
        _df = df [ df.category == category ]
        out += f"## {category}\n\n"
        for idx, row in _df.iterrows():
            out += f"- [{row.name}]({row.url}): {row.description}\n"
        out += "\n"
    with open("README.md", "w") as outf:
        outf.write(out)

if __name__ == "__main__":
    main()
