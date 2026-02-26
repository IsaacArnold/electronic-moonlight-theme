#!/usr/bin/env python3
import plistlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
XCODE_DIR = ROOT / 'xcode'
SRC = XCODE_DIR / 'Electronic Moonlight.xccolortheme'

if not SRC.exists():
    print(f'Error: source theme not found at {SRC}', file=sys.stderr)
    sys.exit(2)

with SRC.open('rb') as f:
    data = plistlib.load(f)

# Locate the DVTSourceTextSyntaxColors dict
key_name = None
for k,v in data.items():
    if k == 'DVTSourceTextSyntaxColors' or k.endswith('DVTSourceTextSyntaxColors'):
        key_name = k
        break

if key_name is None:
    # attempt nested search
    for k,v in data.items():
        if isinstance(v, dict) and 'DVTSourceTextSyntaxColors' in v:
            key_name = 'DVTSourceTextSyntaxColors'
            data = v  # narrow scope
            break

if key_name is None:
    print('Could not find DVTSourceTextSyntaxColors in theme.', file=sys.stderr)
    sys.exit(2)

colors = data[key_name]
if not isinstance(colors, dict):
    print('DVTSourceTextSyntaxColors is not a dict.', file=sys.stderr)
    sys.exit(2)

entries = sorted(colors.keys())
if not entries:
    print('No entries found in DVTSourceTextSyntaxColors.', file=sys.stderr)
    sys.exit(2)

mid = len(entries) // 2
halves = [entries[:mid], entries[mid:]]

out_paths = []
for i, subset in enumerate(halves, start=1):
    out = data.copy() if isinstance(data, dict) else {key_name: {}}
    # ensure we don't accidentally mutate original nested structures
    out_colors = {k: colors[k] for k in subset}
    out[key_name] = out_colors
    out_path = XCODE_DIR / f'Electronic Moonlight-bisect-{i}.xccolortheme'
    with out_path.open('wb') as f:
        plistlib.dump(out, f)
    out_paths.append(out_path)
    print('Wrote', out_path)

print('\nGenerated variant files. Install each in Xcode to test which half triggers the crash.')
print('If one half crashes, rerun with that variant as source to continue bisecting.')
print('Example: python3 scripts/bisect_xcode_theme.py --source xcode/Electronic Moonlight-bisect-1.xccolortheme')

# allow rerun with --source to continue
if '--source' in sys.argv:
    import plistlib
    import sys
    from pathlib import Path
    import copy

    ROOT = Path(__file__).resolve().parents[1]
    XCODE_DIR = ROOT / 'xcode'

    def find_parent_path_for_key(d, target_key, path=None):
        if path is None:
            path = []
        if not isinstance(d, dict):
            return None
        for k, v in d.items():
            if k == target_key:
                return path
            if isinstance(v, dict):
                sub = find_parent_path_for_key(v, target_key, path + [k])
                if sub is not None:
                    return sub
        return None

    def get_by_path(d, path):
        cur = d
        for k in path:
            cur = cur[k]
        return cur

    def set_by_path(d, path, key, value):
        cur = d
        for k in path:
            cur = cur[k]
        cur[key] = value

    def main():
        src = XCODE_DIR / 'Electronic Moonlight.xccolortheme'
        if '--source' in sys.argv:
            idx = sys.argv.index('--source')
            if idx + 1 < len(sys.argv):
                src = Path(sys.argv[idx+1])

        if not src.exists():
            print(f'Error: source theme not found at {src}', file=sys.stderr)
            sys.exit(2)

        with src.open('rb') as f:
            data = plistlib.load(f)

        parent_path = find_parent_path_for_key(data, 'DVTSourceTextSyntaxColors')
        if parent_path is None:
            print('Could not find DVTSourceTextSyntaxColors in theme.', file=sys.stderr)
            sys.exit(2)

        # parent is the dict that contains the key
        parent = get_by_path(data, parent_path) if parent_path else data
        colors = parent.get('DVTSourceTextSyntaxColors')
        if not isinstance(colors, dict):
            print('DVTSourceTextSyntaxColors is not a dict.', file=sys.stderr)
            sys.exit(2)

        entries = sorted(colors.keys())
        if not entries:
            print('No entries found in DVTSourceTextSyntaxColors.', file=sys.stderr)
            sys.exit(2)

        mid = len(entries) // 2
        halves = [entries[:mid], entries[mid:]]

        out_paths = []
        base_name = src.stem
        for i, subset in enumerate(halves, start=1):
            out = copy.deepcopy(data)
            new_colors = {k: colors[k] for k in subset}
            set_by_path(out, parent_path, 'DVTSourceTextSyntaxColors', new_colors)
            out_name = f"{base_name}-bisect-{i}.xccolortheme"
            out_path = src.parent / out_name
            with out_path.open('wb') as f:
                plistlib.dump(out, f)
            out_paths.append(out_path)
            print('Wrote', out_path)

        print('\nGenerated variant files. Install each in Xcode to test which half triggers the crash.')
        print('If one half crashes, rerun with that variant as source to continue bisecting.')
        print(f'Example: python3 {Path(__file__).name} --source xcode/{out_paths[0].name}')

    if __name__ == '__main__':
        main()
