def check_list(item_list):
    if not item_list:
        return True
    first = item_list[0]
    head = first
    i = 0
    length = len(item_list)
    while i <= length:
        try:
            head = item_list[head]
            i += 1
            if head == first:
                if i == length:
                    return True
                return False
        except:
            return False
