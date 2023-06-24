def search(root,key):
    #Base Cases:root is null or key is present:
    if root is None or root.val==key:
        return root

    #key is greater than roots key
    if root.val<key:
        return search(root.right,key)
    #key is smaller than roots key
    return search(root.left,key)
