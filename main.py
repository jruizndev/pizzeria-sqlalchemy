# Importamos librerías
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = 'sqlite:///pomodoro.db'

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

# Definimos el modelo de datos de la base
class Platos(Base):
    __tablename__ = 'platos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_plato = Column(String, nullable=False)

    ingredientes = relationship('Ingredientes', back_populates='rlc_platos', cascade="all, delete-orphan")

    def __repr__(self):
        return f"Plato(id={self.id}, nombre='{self.nombre_plato}')"

class Ingredientes(Base):
    __tablename__ = 'ingredientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_plato = Column(Integer, ForeignKey('platos.id', ondelete="CASCADE"))
    nombre_ingrediente = Column(String, nullable=False)

    rlc_platos = relationship('Platos', back_populates='ingredientes')

    def __repr__(self):
        return f"Ingrediente(id={self.id}, nombre='{self.nombre_ingrediente}', plato_id={self.id_plato})"

# Creamos las tablas en la base de datos
Base.metadata.create_all(engine)

# Configuramos la sesión
SessionLocal = sessionmaker(bind=engine)

# 📌 Funciones CRUD
def crear_plato(nombre, ingredientes):
    """Crea un nuevo plato con sus ingredientes."""
    session = SessionLocal()
    nuevo_plato = Platos(nombre_plato=nombre)
    session.add(nuevo_plato)
    session.commit()  # Guardamos para obtener el ID del plato

    # Agregamos los ingredientes al plato
    for ing in ingredientes:
        nuevo_ingrediente = Ingredientes(nombre_ingrediente=ing, id_plato=nuevo_plato.id)
        session.add(nuevo_ingrediente)

    session.commit()
    session.close()
    print(f"✅ Plato '{nombre}' creado con ingredientes: {ingredientes}")

def leer_platos():
    """Muestra todos los platos y sus ingredientes."""
    session = SessionLocal()
    platos = session.query(Platos).all()

    if not platos:
        print("ℹ️ No hay platos en la base de datos.")
    else:
        for plato in platos:
            print(f"🍽️ {plato.nombre_plato}")
            for ing in plato.ingredientes:
                print(f"   🥗 {ing.nombre_ingrediente}")
    
    session.close()

def actualizar_plato(id_plato, nuevo_nombre):
    """Actualiza el nombre de un plato por su ID."""
    session = SessionLocal()
    plato = session.query(Platos).filter(Platos.id == id_plato).first()
    
    if plato:
        plato.nombre_plato = nuevo_nombre
        session.commit()
        print(f"✅ Plato actualizado a '{nuevo_nombre}'.")
    else:
        print(f"⚠️ No se encontró un plato con ID {id_plato}.")
    
    session.close()

def eliminar_plato(id_plato):
    """Elimina un plato y sus ingredientes por ID."""
    session = SessionLocal()
    plato = session.query(Platos).filter(Platos.id == id_plato).first()
    
    if plato:
        session.delete(plato)
        session.commit()
        print(f"❌ Plato '{plato.nombre_plato}' eliminado.")
    else:
        print(f"⚠️ No se encontró un plato con ID {id_plato}.")
    
    session.close()

# 📌 Ejemplo de uso del CRUD
if __name__ == "__main__":
    # Crear platos
    crear_plato("Pizza Margarita", ["Tomate", "Queso", "Albahaca"])
    crear_plato("Spaghetti Carbonara", ["Pasta", "Huevo", "Queso", "Panceta"])

    # Leer platos
    print("\n📜 Listado de Platos:")
    leer_platos()

    # Actualizar un plato
    actualizar_plato(1, "Pizza Napolitana")

    # Leer platos después de la actualización
    print("\n📜 Platos después de la actualización:")
    leer_platos()

    # Eliminar un plato
    eliminar_plato(2)

    # Leer platos después de la eliminación
    print("\n📜 Platos después de la eliminación:")
    leer_platos()
