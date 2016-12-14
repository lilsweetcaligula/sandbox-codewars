# return True if the two binary trees rooted and a and b are equal in value and structure
# return False otherwise
def compare(a, b):
    if a == b == None:
        return True
    elif a == None or b == None:
        return False
    return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right)
