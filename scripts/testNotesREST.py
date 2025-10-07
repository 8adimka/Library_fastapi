"""
Простой нагрузочный тестер для /notes/ API.
Usage:
    python scripts/testNotesREST.py --url http://localhost:8000 --ops 1000 --add_ratio 0.7 --workers 10

Добавления составляют --add_ratio долю от общего числа операций; остальные операции — удаления (по существующим id).
"""

import argparse
import queue
import random
import threading
import time

import requests

parser = argparse.ArgumentParser()
parser.add_argument("--url", default="http://localhost:8000")
parser.add_argument("--ops", type=int, default=1000)
parser.add_argument("--add_ratio", type=float, default=0.7)
parser.add_argument("--workers", type=int, default=10)
args = parser.parse_args()

API_ADD = args.url.rstrip("/") + "/notes/"
API_LIST = API_ADD
API_DELETE = args.url.rstrip("/") + "/notes/{id}/"

ops_queue = queue.Queue()

# prepare operations
num_adds = int(args.ops * args.add_ratio)
num_deletes = args.ops - num_adds

for _ in range(num_adds):
    ops_queue.put("add")
for _ in range(num_deletes):
    ops_queue.put("del")

created_ids = []
ids_lock = threading.Lock()


def worker():
    while not ops_queue.empty():
        try:
            op = ops_queue.get_nowait()
        except queue.Empty:
            return
        if op == "add":
            data = {
                "note": "n-" + str(random.randint(1, 1_000_000)),
                "description": "d",
            }
            try:
                r = requests.post(API_ADD, json=data, timeout=5)
                if r.status_code == 201:
                    nid = r.json().get("id")
                    with ids_lock:
                        created_ids.append(nid)
            except Exception:
                pass
        else:  # delete
            with ids_lock:
                if created_ids:
                    nid = created_ids.pop(random.randrange(len(created_ids)))
                else:
                    nid = None
            if nid:
                try:
                    requests.delete(API_DELETE.format(id=nid), timeout=5)
                except Exception:
                    pass
        ops_queue.task_done()


threads = []
start = time.time()
for _ in range(args.workers):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
print(f"Done {args.ops} ops in {end - start:.2f}s")
