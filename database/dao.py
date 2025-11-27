from database.DB_connect import DBConnect
from model.archi import Archi
from model.hub import Hub

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def read_hub():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        query = """ SELECT * FROM hub """
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
        query = """SELECT 
                     LEAST(s.id_hub_origine, s.id_hub_destinazione) AS h1,
                     GREATEST(s.id_hub_origine, s.id_hub_destinazione) AS h2,
                     AVG(s.valore_merce) AS valore_medio
                   FROM spedizione s
                   GROUP BY h1, h2
                   HAVING valore_medio >= %s """
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(query,(valore, ))
            for row in cursor:
                arco = Archi(row["h1"],
                            row["h2"],
                            row["valore_medio"],)
                result.append(arco)
        except Exception as e:
            print(f"Errore durante la query read_archi: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result
