import unittest
from multired.mred import MultiplexRed


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        m = MultiplexRed("../../sample_data/file_list", verbose=True)
        part = m.compute_partitions()
        m.dump_partitions()
        m.draw_dendrogram()

    def test_simple_approx(self):
        m = MultiplexRed("../../sample_data/file_list", verbose=True, fit_degree=20)
        part = m.compute_partitions_approx()
        m.dump_partitions_approx()
        m.draw_dendrogram_approx()

    def test_approx(self):
        m = MultiplexRed("../../sample_data/file_list")
        m.compute_layer_entropies_approx()
        m.compute_JSD_matrix_approx()
        m.reduce_approx()

    def test_base(self):
        m = MultiplexRed("../../sample_data/file_list")
        m.compute_layer_entropies()
        m.compute_JSD_matrix()
        m.reduce()
        part = m.compute_partitions()
        m.dump_partitions()


if __name__ == '__main__':
    unittest.main()
