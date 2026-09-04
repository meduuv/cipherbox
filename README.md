# CipherBox

> Local file encryption with a small, explicit interface.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

CipherBox is a local file-encryption utility built around Python's standard library and documented cryptographic primitives.

## Security model

CipherBox is designed for **local encryption and decryption**. It does not connect to remote systems or upload plaintext.

The design emphasizes authenticated ciphertext, streaming file processing and explicit failure handling for corrupted or invalid data.

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

## Design

```text
plaintext file
     ↓
key derivation
     ↓
authenticated encryption
     ↓
.cbox container
```

The reverse path verifies the ciphertext before producing decrypted output.

## Development

```bash
python -m unittest discover -s tests -v
```

## Security note

CipherBox should not be treated as a substitute for a professional cryptographic storage system without independently reviewing its implementation and threat model.

## License

MIT. See [`LICENSE`](LICENSE).

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
