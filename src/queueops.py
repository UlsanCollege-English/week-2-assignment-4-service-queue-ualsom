from typing import List, Tuple, Optional

def take_next(queue: List[str]) -> Tuple[Optional[str], List[str]]:
    """Return (next_name, remaining_queue).
    If queue is empty, return (None, []).
    """
    if not queue:
        return None, []
    # Return first element and the rest as a new list
    return queue[0], queue[1:]


def move_to_back(queue: List[str], name: str) -> List[str]:
    """Return a new queue where the first occurrence of `name` is moved to the back.
    If `name` is not present, return the queue unchanged (new list).
    """
    if name not in queue:
        return queue[:]  # return a copy to avoid mutation

    idx = queue.index(name)
    # Move that element to the back
    return queue[:idx] + queue[idx+1:] + [name]


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    """Return an interleaved queue: q1[0], q2[0], q1[1], q2[1], ...
    After the shorter queue runs out, append the rest.
    """
    result = []
    len1, len2 = len(q1), len(q2)
    min_len = min(len1, len2)

    # Interleave common length
    for i in range(min_len):
        result.append(q1[i])
        result.append(q2[i])

    # Append remainder from longer queue
    if len1 > len2:
        result.extend(q1[min_len:])
    else:
        result.extend(q2[min_len:])

    return result
