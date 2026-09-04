# CipherBox

A local file encryption utility built around Python's standard library and clearly documented cryptographic primitives.

## Features

- Password-derived encryption workflow
- Streaming file processing
- Authenticated ciphertext format
- File metadata kept separate from plaintext
- Clear errors for invalid or corrupted data
- No network access

## Usage

```bash
cipherbox encrypt notes.txt notes.cbox
cipherbox decrypt notes.cbox notes.txt
```

Use a strong, unique password and keep an independent backup of important data.

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

Built by Medu: https://guns.lol/meduu
