from dsf import DisjointSetForest

def slc(graph, d, k):
    nodes = list(graph.nodes)
    dsf = DisjointSetForest(nodes)
    num_clusters = len(nodes)

    edges_sorted = sorted(graph.edges, key=d)

    for u, v in edges_sorted:
        if dsf.in_same_set(u, v):
            continue
        if num_clusters == k:
            break
        dsf.union(u, v)
        num_clusters -= 1

    clusters_dict = {}
    for node in graph.nodes:
        rep = dsf.find_set(node)
        clusters_dict.setdefault(rep, set()).add(node)

    return frozenset(frozenset(cluster) for cluster in clusters_dict.values())
