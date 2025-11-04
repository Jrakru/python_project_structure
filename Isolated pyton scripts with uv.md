#1: uv + PEP 723 inline dependencies**.

---

---

title: Isolated Python Scripts with **uv** + PEP 723
updated: 2025-10-21
tags: [python, tooling, uv, pep-723, scripts, virtualenv, isolation]
summary: Single-file Python scripts declare deps inline and run in their own cached, isolated envs via uv—keeping your main venv pristine.
------------------------------------------------------------------------------------------------------------------------------------------

# Why this

* **Zero pollution:** each script runs in an **isolated env** created from the script’s own inline dependency metadata.
* **Single file, reproducible:** deps + Python version live **inside the script**. No separate `requirements.txt` or project venv needed. ([Astral Docs][1])

---

## Install `uv` (once)

Use the official installer (Linux/macOS):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# then reopen your shell so $PATH picks up uv/uvx
```

(Other methods exist—Homebrew, Windows installer, Docker images—see the uv install docs.) ([Astral Docs][2])

---

## Canonical script template (imports at top)

> House rule: **put all imports at the beginning** when running or testing.

Create `weather_report.py`:

```python
#!/usr/bin/env -S uv run -q
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests==2.32.3",
#   "polars>=1.7"
# ]
# ///

import requests
import polars as pl

def main() -> None:
    r = requests.get("https://httpbin.org/json", timeout=10)
    df = pl.DataFrame([r.json()])
    print(df)

if __name__ == "__main__":
    main()
```

Run it:

```bash
chmod +x weather_report.py
./weather_report.py
# or: uv run weather_report.py
```

* The `# /// script ... ///` block is **PEP 723 inline metadata**. uv reads this to build a temp env per unique dep set and runs the script in it. Your main venv isn’t touched. ([Python Enhancement Proposals (PEPs)][3])

---

## Everyday operations

### Add/change dependencies without hand-editing

```bash
uv add --script weather_report.py "httpx<1"
uv remove --script weather_report.py httpx
```

`uv add --script` edits the inline metadata for you; `uv run` will then use an isolated env with those deps. ([Astral Docs][4])

### Pin the Python interpreter

Inside the header, set:

```toml
# requires-python = "==3.12.*"
```

This makes the script enforce a specific Python line when resolving/running. (Tip: include this for reproducibility.) ([Astral Docs][4])

### Lock (optional but nice for sharing)

Create a lockfile next to the script:

```bash
uv lock --script weather_report.py
```

This writes a script-specific lock, improving repeatability on other machines. ([Astral Docs][4])

### One-off tools (linters/formatters) with **uvx**

Run tools in their **own** isolated envs (no installs into any venv):

```bash
uvx ruff@latest check .
uvx black --version
```

`uvx` is just an alias for `uv tool run`. ([Astral Docs][5])

---

## Caching & refresh

uv caches wheels/env bits to be fast and space-efficient.

* Show cache dir / nuke it:

```bash
uv cache dir
uv cache clean           # all
uv cache clean ruff      # per package
```

* Force revalidation on a run:

```bash
uv run --refresh weather_report.py
```

(Any uv command accepts `--refresh` to re-check cached data.) ([Astral Docs][6])

---

## Tips & patterns

* **Executable scripts on your PATH:** keep scripts in `~/bin` (or symlink from there). The shebang `#!/usr/bin/env -S uv run -q` means you can run them directly. ([Astral Docs][1])
* **Share as a gist/single file:** the inline block carries deps + Python version, so collaborators can run with just `uv`. ([Astral Docs][1])
* **Keep deps minimal:** small dep sets = faster cold starts.

---

## References (for deeper reading)

* uv “Running scripts” guide (shebang + inline deps). ([Astral Docs][1])
* PEP 723: Inline script metadata spec. ([Python Enhancement Proposals (PEPs)][3])
* uv tools/`uvx` overview. ([Astral Docs][5])
* uv cache behavior & commands. ([Astral Docs][6])
* uv CLI reference (script add/lock flags). ([Astral Docs][4])

---

**That’s it.** Drop this in your vault and duplicate the template block whenever you want a fresh, self-contained script that **never** touches your main venv.

[1]: https://docs.astral.sh/uv/guides/scripts/?utm_source=chatgpt.com "Running scripts | uv - Astral Docs"
[2]: https://docs.astral.sh/uv/getting-started/installation/?utm_source=chatgpt.com "Installation | uv - Astral Docs"
[3]: https://peps.python.org/pep-0723/?utm_source=chatgpt.com "PEP 723 – Inline script metadata"
[4]: https://docs.astral.sh/uv/reference/cli/ "Commands | uv"
[5]: https://docs.astral.sh/uv/concepts/tools/?utm_source=chatgpt.com "Tools | uv - Astral Docs"
[6]: https://docs.astral.sh/uv/concepts/cache/?utm_source=chatgpt.com "Caching | uv - Astral Docs"
