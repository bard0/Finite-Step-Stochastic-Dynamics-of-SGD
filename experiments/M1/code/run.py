from pathlib import Path

def main():
    here = Path(__file__).resolve().parent
    parts = sorted((here / "source").glob("source_*.pyfrag"))
    if not parts:
        raise RuntimeError("No source fragments found")
    source = "".join(p.read_text(encoding="utf-8") for p in parts)
    code = compile(source, str(here / "archived_public_run.py"), "exec")
    namespace = {"__name__": "__main__", "__file__": str(here / "archived_public_run.py")}
    exec(code, namespace, namespace)

if __name__ == "__main__":
    main()
