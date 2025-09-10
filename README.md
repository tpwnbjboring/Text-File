# Find Longest Word in a Text File

This Python script finds the longest word in a given text file.

## Usage

```bash
python find_longest_word.py <filename>
```

- `<filename>` is the path to the text file you want to analyze.

## Example

Suppose you have a file named `sample.txt`:

```
The quick brown fox jumps over the lazy dog.
```

Run:

```bash
python find_longest_word.py sample.txt
```

Output:

```
The longest word is: jumps
```

## Notes

- The script ignores common punctuation attached to words.
- If the file does not exist, an error message will be shown.

## License

MIT
