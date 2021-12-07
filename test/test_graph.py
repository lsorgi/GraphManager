from graph_manager.graph import Graph
import pytest
import os


@pytest.fixture(scope="function")
def tmp_folder(tmp_path_factory):
    return tmp_path_factory.mktemp('graph_test_tmp_data')


def test_graph_constructor_return_valid_obj():
    nodes = [1, 4, 6]
    edges = [(1, 4), (1, 6)]
    graph = Graph(nodes=nodes, edges=edges)
    assert isinstance(graph, Graph)


def test_graph_constructor_fails_for_duplicate_nodes():
    with pytest.raises(ValueError):
        nodes = [1, 1, 6]
        edges = [(1, 4), (1, 6)]
        graph = Graph(nodes=nodes, edges=edges)


def test_graph_constructor_fails_for_invalid_edge():
    with pytest.raises(ValueError):
        nodes = [1, 4, 6]
        edges = [(1, 4), (2, 6)]
        graph = Graph(nodes=nodes, edges=edges)


def test_graph_save_to_file(tmp_folder):
    nodes = [1, 4, 6]
    edges = [(1, 4), (1, 6)]
    graph = Graph(nodes=nodes, edges=edges)
    filename = os.path.join(tmp_folder, 'graph.h5')
    graph.save(filename)
    assert os.path.isfile(filename)


def test_graph_load_from_file(tmp_folder):
    nodes = [1, 4, 6]
    edges = [(1, 4), (1, 6)]
    graph = Graph(nodes=nodes, edges=edges)
    filename = os.path.join(tmp_folder, 'graph.h5')
    graph.save(filename)

    graph_cpy = Graph.from_file(filename)
    assert isinstance(graph, Graph)

    assert graph.edges == graph_cpy.edges
    assert graph.nodes == graph_cpy.nodes


def test_graph_histogram(tmp_folder):
    nodes = [1, 4, 6, 8, 9, 10]
    edges = [(1, 4), (1, 6), (1, 8), (4, 6), (10, 1)]
    graph = Graph(nodes=nodes, edges=edges)
    filename = os.path.join(tmp_folder, 'out_degree.png')
    graph.draw(filename)
    assert os.path.isfile(filename)
