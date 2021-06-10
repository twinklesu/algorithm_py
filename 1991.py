def traversal(tree: dict, root: str, order: str):
    if root == '.':
        return ''
    left, right = map(str, tree[root])
    if order == 'pre':
        return root + traversal(tree, left, order) + traversal(tree, right, order)
    elif order == 'in':
        return traversal(tree, left, order) + root + traversal(tree, right, order)
    else:
        return traversal(tree, left, order) + traversal(tree, right, order) + root


def main():
    n = int(input())
    tree = dict()
    for _ in range(n):
        root, left, right = map(str, input().split())
        tree[root] = [left, right]
    print(traversal(tree, 'A', 'pre'))
    print(traversal(tree, 'A', 'in'))
    print(traversal(tree, 'A', 'post'))


main()
