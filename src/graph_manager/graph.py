from typing import Tuple, List
import numpy as np
import h5py
import matplotlib.pyplot as plt


class Graph:
    def __init__(self,
                 nodes: List[int],
                 edges: List[Tuple[int, int]]):
        # check input
        node_set = set(nodes)
        if len(node_set) != len(nodes):
            raise ValueError('Duplicate nodes!')
        for src_dst in edges:
            src, dst = src_dst
            if src not in node_set:
                raise ValueError('Invalid node!')

        # create graph
        self._map = {node: [] for node in nodes}
        for edge in edges:
            self._map[edge[0]].append(edge[1])

    @property
    def nodes(self) -> List[int]:
        return list(self._map.keys())

    @property
    def node_count(self) -> int:
        return len(self.nodes)

    @property
    def edges(self) -> List[Tuple[int, int]]:
        edges = []
        for src in self.nodes:
            for dst in self._map[src]:
                edges.append((src, dst))
        return edges

    @property
    def edge_count(self) -> int:
        return len(self.edges)

    def save(self, filename: str):
        h = h5py.File(filename, 'w')
        h.create_dataset('nodes', data=np.array(self.nodes, dtype=int))
        h.create_dataset('edges', data=np.array(self.edges, dtype=int))
        h.close()

    @classmethod
    def from_file(cls, filename: str):
        with h5py.File(filename, 'r') as h5file:
            return Graph(nodes=h5file['nodes'][:].tolist(),
                         edges=h5file['edges'][:].tolist())

    def draw(self, filename: str):
        out_degrees = [len(self._map[node]) for node in self.nodes]
        max_degree = max(out_degrees)
        x = range(max_degree + 1)
        bins = np.zeros(max_degree + 1, dtype=int)
        for degree in out_degrees:
            bins[degree] += 1
        plt.bar(x, bins)
        plt.xlabel('out degree')
        plt.xticks(x)
        plt.ylabel('node count')
        plt.yticks(range(0, max(bins), 5))
        plt.title('Out degree histogram')
        plt.savefig(filename)



