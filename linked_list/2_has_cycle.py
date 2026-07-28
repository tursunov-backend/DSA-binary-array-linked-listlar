

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    ll = build_linked_list([1, 2, 3, 4])
    print(has_cycle(ll))  # -> False

    # Sikl hosil qilish misoli:
    ll2 = build_linked_list([1, 2, 3])
    ll2.next.next.next = ll2  # oxirini boshiga ulaymiz
    print(has_cycle(ll2))  # -> True
