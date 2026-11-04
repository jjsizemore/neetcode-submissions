class TreeNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
        else:
            cur = self.root
            while True:
                if cur.key == key:
                    cur.val = val
                    return
                elif cur.key < key:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = TreeNode(key, val)
                        return
                else:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = TreeNode(key, val)
                        return

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if cur.key == key:
                return cur.val
            elif cur.key < key:
                cur = cur.right
            else:
                cur = cur.left
        return -1

    def findMin(self, node: TreeNode) -> TreeNode:
        cur = node
        while cur and cur.left:
            cur = cur.left
        return cur if cur else None

    def getMin(self) -> int:
        min_node = self.findMin(self.root)
        return min_node.val if min_node else -1

    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val if cur else -1


    def remove(self, key: int) -> None:
        # must be able to remove a node that has branches below it
        # means if we have the node in our left or right,
        # must switch pointer to that nodes right or left ptr if exists, otherwise the other one
        self.root = self.removeHelper(self.root, key)

        
    # Returns new root node of subtree after key removal
    def removeHelper(self, cur: TreeNode, key: int) -> Optional[TreeNode]:
        if not cur:
            return None
        
        if key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        elif key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        else:
            if not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left
            else:
                min_node = self.findMin(cur.right)
                cur.key = min_node.key
                cur.val = min_node.val
                cur.right = self.removeHelper(cur.right, min_node.key)
        return cur


    def getInorderKeys(self) -> List[int]:
        res = []

        stack = []

        cur = self.root
        while cur or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            res.append(cur.key)

            cur = cur.right
        
        return res