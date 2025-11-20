def get_or_create_thread(victor, thread_key: str):
    existing = victor.find_thread(thread_key)
    if existing:
        return existing
    return victor.create_thread(thread_key)


def record_unresolved(victor, thread_id: str, item):
    victor.store_unresolved_item(thread_id, item)


def summarize_thread(victor, thread_id: str):
    unresolved = victor.get_unresolved_items(thread_id)
    return {
        "thread_id": thread_id,
        "unresolved_count": len(unresolved),
    }
