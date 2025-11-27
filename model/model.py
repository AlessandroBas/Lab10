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
        self._edges = DAO.read_archi(threshold)
        self._nodes = DAO.read_hub()
        self.G.clear()
        mappa_hub = {hub.id: hub for hub in self._nodes}

        for arco in self._edges:
            h1 = arco.h1
            h2 = arco.h2
            if h1 in mappa_hub:
                self.G.add_node(h1, obj=mappa_hub[h1])
            if h2 in mappa_hub:
                self.G.add_node(h2, obj=mappa_hub[h2])
            peso = arco.valore_medio
            self.G.add_edge(h1, h2, weight=peso)

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return len(self.G.edges)

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return len(self.G.nodes)

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        result = []
        mappa_hub = {hub.id: hub for hub in self._nodes}
        for h1, h2, data in self.G.edges(data=True):
            peso = round(data.get("weight"),2)
            hub1 = mappa_hub[h1]
            hub2 = mappa_hub[h2]
            str =(f"[{hub1} -> {hub2}] -- Guadagno Medio Per Spedizione {peso}$")
            result.append(str)
        return result

