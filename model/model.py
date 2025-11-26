from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self._edges = DAO.read_spedizione()
        self._nodes = DAO.read_hub()
        self.G.clear()

        for hub in self._nodes:
            self.G.add_node(hub.id,obj=hub)

        tratte = {}
        for s in self._edges:
            key = tuple((s.id_hub_origine, s.id_hub_destinazione))
            tratte[key].append(s.valore_merce)
        for (h1,h2), valori in tratte.items():
            media=sum(valori)/len(valori)
            if media >= threshold:
                self.G.add_edge(h1,h2, peso=media)


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return

