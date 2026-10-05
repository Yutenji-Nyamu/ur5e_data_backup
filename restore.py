#!/usr/bin/env python3
"""Download and unpack successful joint demonstrations (Python 3.12+)."""
import argparse
import json
from pathlib import Path
import shutil
import tarfile
import urllib.request

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--date', action='append', help='YYYY-MM-DD; omit for all dates')
parser.add_argument('--dest', type=Path, default=root)
args = parser.parse_args()
manifest = json.loads((root / 'downloads.json').read_text())
known = {item['date'] for item in manifest['assets']}
if args.date and not set(args.date) <= known:
    parser.error('Unknown date')
dest = args.dest.resolve()
cache = dest / 'downloads'
cache.mkdir(parents=True, exist_ok=True)
for item in manifest['assets']:
    if args.date and item['date'] not in args.date:
        continue
    archive = cache / item['name']
    if not archive.exists() or archive.stat().st_size != item['bytes']:
        temporary = archive.with_suffix('.tar.part')
        print('Downloading', item['name'], flush=True)
        with urllib.request.urlopen(item['url'], timeout=180) as response, temporary.open('wb') as output:
            shutil.copyfileobj(response, output, 1024 * 1024)
        if temporary.stat().st_size != item['bytes']:
            raise RuntimeError('Incomplete download: ' + item['name'])
        temporary.replace(archive)
    print('Extracting', item['name'], flush=True)
    with tarfile.open(archive, 'r:') as source:
        source.extractall(dest, filter='data')
print('Done.')
