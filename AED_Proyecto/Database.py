# coding=utf-8
from neo4j import GraphDatabase, basic_auth


class Database(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)


    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

    def write(self, _id, type, arguments):
        result = ""
        argumentsList = []
        if type is not None:
            result += "CREATE (" + _id + ":" + type + ")\n"
            counter = 0
            for oneArgument in arguments:
                argumentsList.append(arguments[oneArgument])
                result += "SET " + _id + "." + oneArgument + " = $arguments[" + str(counter) + "]" + "\n"
                counter += 1
        with self._driver.session() as session:
            session.write_transaction(self._create, argumentsList, result)

    def connect(self, type1, type2, variableName1, variable1, VariableName2, variable2, linkName):
        result = "MATCH (a:" + type1 + "),(b:" + type2 + ")\nWHERE a." + variableName1 + "= $variable1 AND b." + VariableName2 + "= $variable2\nCREATE (a)-[:" + linkName + "]->(b)"
        with self._driver.session() as session:
            session.write_transaction(self._connect, result, variable1, variable2)

    def delete(self, nodeType, key, value):
        result = "MATCH (a:" + nodeType + ")\nWHERE a." + key + "= $value\nDETACH DELETE (a)"
        with self._driver.session() as session:
            session.write_transaction(self._delete, result, value)

    def deleteLink(self, type1, type2, variableName1, variable1, VariableName2, variable2, linkName):
        result = "MATCH (a:" + type1 + "),(b:" + type2 + ")\nWHERE a." + variableName1 + "= $variable1 AND b." + VariableName2 + "= $variable2\nMATCH (a)-[r:" + linkName + "]->(b)\nDELETE r"
        with self._driver.session() as session:
            session.write_transaction(self._deleteLink, result, variable1, variable2)

    def upgrade(self, nodeType, key, value, newValue):
        result = "MATCH (a:" + nodeType + ")\nWHERE a." + key + "= $value\nSET a." + key + "= $newValue"
        with self._driver.session() as session:
            session.write_transaction(self._upgrade, result, value, newValue)

    def getNode(self, nodeType, key, value):
        result = "MATCH (a:" + nodeType + ")\nWHERE a." + key + "=$value\nRETURN a"
        with self._driver.session() as session:
            return session.write_transaction(self._getNode, result, value)

    def getNodesByOther(self, nodeType, key, value, link):
        result = "MATCH (a:" + nodeType + ")\nWHERE a." + key + "=$value\nMATCH (a)-[:" + link + "]->(m)<-[:" + link + "]-(r)\nRETURN r"
        with self._driver.session() as session:
            return session.write_transaction(self._getNodes, result, value)

    def getAllType(self, nodeType):
        result = "MATCH (a:" + nodeType + ")\nRETURN a"
        with self._driver.session() as session:
            return session.write_transaction(self._Default, result)

    def getDefault(self):
        result = "MATCH (n) return n"
        with self._driver.session() as session:
            resultado = session.write_transaction(self._Default, result)
            return resultado

    def setDefault(self):
        if (self.getDefault().single() == None):
            result = """
            CREATE (Compu:Carrera{titulo:"Compu"})
            """
            with self._driver.session() as session:
                return session.write_transaction(self._Default, result)

    def getNodesByLink(self, nodeType, key, value, link):
        result = "MATCH (a:" + nodeType + ")\nWHERE a." + key + "=$value\nMATCH (a)-[:" + link + "]->(m)\nRETURN m"
        with self._driver.session() as session:
            return session.write_transaction(self._getNodes, result, value)

    # Este método es la base para nuestro sistema de recomendaciones. Esto debido a que hace el query en Neo4j
    # primero sobre un parámetro. Luego, sobre el resultado de ese query hace el query siguiente con otro parámetro y
    # así sucesivamente hasta llegar a un resultado que esté conectado por todos los parámetros en el que el primer
    # parámetro es de mayor importancia y el último de menos.
    def recommend(self, course, role_model, activity):
        result = """MATCH (c:Carrera)<-[:lleva]-(:Clase {nombre: '%s'}),
        (c)<-[:lleva]-(:Persona {nombre: '%s'}),
        (c)<-[:lleva]-(:gusto {nombre: '%s'})
     RETURN (c)""" % (course, role_model, activity)
        with self._driver.session() as session:
            return session.read_transaction(self._Default, result)

    #Este es el método para crear una nueva carrera con vínculo a un curso, persona y actividad ya existentes.
    def createCareer(self, faculty, career_name, course, role_model, activity):
        with self._driver.session() as session:
            session.write_transaction(self.create_career_wLinks, faculty,career_name,course,role_model,activity)

    @staticmethod
    def create_career_wLinks(tx, faculty, career_name, course, role_model, activity):
        result = tx.run("""MATCH (class:Clase {nombre: $course})
MATCH (activity:gusto {nombre: $activity})
MATCH (person:Persona {nombre: $role_model})
CREATE (c: Carrera {facultad: $faculty, nombre: $career_name})
CREATE (class) -[:lleva]->(c)
CREATE (activity) -[:lleva]->(c)
CREATE (person) -[:lleva]->(c)
RETURN c.nombre""",faculty=faculty, career_name=career_name,course=course,role_model=role_model,activity=activity)

    # Este es el método para eliminar una carrera con todos los vículos que tenía.
    def deleteCareer(self, career_name):
        with self._driver.session() as session:
            session.write_transaction(self.delete_career_wLinks, career_name)

    @staticmethod
    def delete_career_wLinks (tx, career_name):
        result = tx.run("""MATCH (n:Carrera {nombre: $career_name})
MATCH (:Clase)-[c:lleva]->(n)
MATCH (:Persona)-[p:lleva]->(n)
MATCH (:gusto)-[g:lleva]->(n)
Delete c,p,g,n""", career_name=career_name)

    @staticmethod
    def _getRecomendation(tx, result, course, role_model, activity):
        return tx.run(result, course, role_model, activity)

    @staticmethod
    def _Default(tx, result):
        return tx.run(result)

    @staticmethod
    def _getNodes(tx, result, value):
        return tx.run(result, value)

    @staticmethod
    def _getNode(tx, result, value):
        return tx.run(result, value)

    @staticmethod
    def _upgrade(tx, result, value, newValue):
        result = tx.run(result, value, newValue)

    @staticmethod
    def _deleteLink(tx, result, variable1, variable2):
        result = tx.run(result, variable1, variable2)

    @staticmethod
    def _delete(tx, result, value):
        result = tx.run(result, value)

    @staticmethod
    def _connect(tx, result, variable1, variable2):
        result = tx.run(result, variable1, variable2)

    """This method is used by write"""

    @staticmethod
    def _create(tx, arguments, result):
        result = tx.run(result, arguments)
