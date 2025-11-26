from database.DB_connect import DBConnect
from model.archi import Archi
from model.spedizione import Spedizione
from model.compagnia import Compagnia
from model.hub import Hub

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def read_spedizione():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        query = """SELECT * FROM spedizione"""
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query)
            for row in cursor:
                spedizione = Spedizione(row["id"],
                                        row["id_compagnia"],
                                        row["numero_tracking"],
                                        row["id_hub_origine"],
                                        row["id_hub_destinazione"],
                                        row["data_ritiro_programmata"],
                                        row["distanza"],
                                        row["data_consegna"],
                                        row["valore_merce"],)
                result.append(spedizione)

        except Exception as e:
            print(f"Errore durante la query read_spedizione: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def read_compagnia():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        query = "SELECT * FROM compagnia"
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query)
            for row in cursor:
                compagnia = Compagnia(row["id"],
                                      row["codice"],
                                      row["nome"],)
                result.append(compagnia)
        except Exception as e:
            print(f"Errore durante la query read_compagnia: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def read_hub():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        query = "SELECT * FROM hub"
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query)
            for row in cursor:
                hub = Hub(row["id"],
                          row["codice"],
                          row["nome"],
                          row["citta"],
                          row["stato"],
                          row["latitudine"],
                          row["longitudine"],)
                result.append(hub)
        except Exception as e:
            print(f"Errore durante la query read_hub: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def read_archi(valore):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        query = """SELECT LEAST (s.id_hub_origine,s.id_hub_destinazione) as h1
                    FROM spedizione
                    GROUP BY id_hub_origine, id_hub_destinazione
                 """
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query,(valore,))
            for row in cursor:
                arco = Archi(row["h1"],
                            row["h2"],
                            row["valore_totale"],
                            row["n_spedizione"],)
                result.append(arco)
        except Exception as e:
            print(f"Errore durante la query read_archi: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result
