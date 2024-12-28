from vector import VectorCompare, CustomVectorCompare
import argparse
import json

def process_file(file_path):
    """
    Process the input file based on its extension:
    - If it's a .json file, read an array of strings.
    - If it's a .txt file, split the text into sentences.
    """
    if file_path.endswith(".json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list) and all(isinstance(item, str) for item in data):
                    return data
                else:
                    print("Error: JSON file must contain an array of strings.")
                    exit(1)
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            exit(1)
    elif file_path.endswith(".txt"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                # Split the text into phrases based on periods
                phrases = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
                return phrases
        except Exception as e:
            print(f"Error reading TXT file: {e}")
            exit(1)
    else:
        print("Error: Unsupported file type. Supported types are .json and .txt.")
        exit(1)

parser = argparse.ArgumentParser(
    description="Vector Space Model (VSM) with support for .json and .txt files."
)

parser.add_argument(
    "file",
    help="The path to the file to process. Supported extensions: .json (array of strings), .txt (plain text).",
)
parser.add_argument(
    "-c",
    "--custom",
    action="store_true",
    help="Enable custom algorithm",
)
parser.add_argument(
    "-q",
    "--query",
    type=str,
    help="Search term for querying documents",
)

args = parser.parse_args()

# Check if a file path is provided
if not args.file:
    parser.print_help()
    exit()

# Determine which class to use based on the -c flag
v = CustomVectorCompare() if args.custom else VectorCompare()

# Process the input file
documents = process_file(args.file)

index = []
for item in documents:
    index.append(v.concordance(item.lower()))

searchterm = args.query if args.query else input("Enter Search Term: ")
matches = []

for i in range(len(index)):
    relation = v.relation(v.concordance(searchterm.lower()), index[i])
    if relation != 0:
        matches.append((relation, documents[i][:100]))

matches.sort(reverse=True)

for i in matches:
    print(i[0], i[1])
