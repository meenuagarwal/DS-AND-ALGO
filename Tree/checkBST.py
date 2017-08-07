def checkBST(root):
  # start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # depth-first traversal
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # if this node is invalid, we return false right away
        if (node.data <= lower_bound) or (node.data >= upper_bound):
            return False

        if node.left:
            # this node must be less than the current node
            node_and_bounds_stack.append((node.left, lower_bound, node.data))
        if node.right:
            # this node must be greater than the current node
            node_and_bounds_stack.append((node.right, node.data, upper_bound))

    # if none of the nodes were invalid, return true
    # (at this point we have checked all nodes)
    return True
