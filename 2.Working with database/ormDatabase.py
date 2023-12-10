from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)

class CarDatabase:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_car(self, make, model):
        car = Car(make=make, model=model)
        self.session.add(car)
        self.session.commit()

    def retrieve_cars(self):
        cars = self.session.query(Car).all()
        return cars

    def update_car_model(self, car_id, new_model):
        car = self.session.query(Car).filter_by(id=car_id).first()
        if car:
            car.model = new_model
            self.session.commit()
            print("Car model updated successfully!")
        else:
            print(f"Car with ID {car_id} not found.")

    def delete_car(self, car_id):
        car = self.session.query(Car).filter_by(id=car_id).first()
        if car:
            self.session.delete(car)
            self.session.commit()
            print("Car deleted successfully!")
        else:
            print(f"Car with ID {car_id} not found.")

    def close_connection(self):
        self.session.close()

def main():
    database = CarDatabase('sqlite:///ormDatabase.db')  # Use your preferred database URL

    while True:
        print("\nChoose an operation:")
        print("1. Add car")
        print("2. Retrieve cars")
        print("3. Update car model")
        print("4. Delete car")
        print("5. Exit")

        choice = input("Enter the number corresponding to the operation: ")

        if choice == '1':
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            database.add_car(make, model)
            print("Car added successfully!")

        elif choice == '2':
            cars = database.retrieve_cars()
            print("\nCars in the database:")
            for car in cars:
                print(f"ID: {car.id}, Make: {car.make}, Model: {car.model}")

        elif choice == '3':
            car_id = int(input("Enter car ID to update model: "))
            new_model = input("Enter new model: ")
            database.update_car_model(car_id, new_model)

        elif choice == '4':
            car_id = int(input("Enter car ID to delete: "))
            database.delete_car(car_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    database.close_connection()
    print("Program terminated.")

if __name__ == "__main__":
    main()
