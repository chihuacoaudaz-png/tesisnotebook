import asyncio
import sys
import json
from notebooklm import NotebookLMClient

async def inspect_all():
    try:
        async with await NotebookLMClient.from_storage() as client:
            notebooks = await client.notebooks.list()
            if not notebooks:
                print("No notebooks found or empty account.")
                return

            print(f"=== Total Notebooks Found: {len(notebooks)} ===")
            for idx, nb in enumerate(notebooks, 1):
                print(f"\n[{idx}] Notebook: {nb.title} (ID: {nb.id})")
                print(f"    Created: {getattr(nb, 'created_at', 'N/A')}")
                
                try:
                    sources = await client.sources.list(nb.id)
                    print(f"    Sources count: {len(sources)}")
                    for s in sources:
                        print(f"      - Source: {s.title} (Type: {getattr(s, 'type', 'N/A')})")
                except Exception as e:
                    print(f"    Sources error: {e}")

                try:
                    notes = await client.notes.list(nb.id)
                    print(f"    Notes count: {len(notes)}")
                    for n in notes:
                        print(f"      - Note: {n.title or 'Untitled Note'}")
                except Exception as e:
                    print(f"    Notes error: {e}")
                    
    except Exception as e:
        print(f"Error connecting to NotebookLM: {e}", file=sys.stderr)

if __name__ == "__main__":
    asyncio.run(inspect_all())
