import mysql.connector
from tkinter import messagebox

def save_data_mysql(name, date, dob, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result):
    try:
        # Establishing a connection to MySQL
        mydb = mysql.connector.connect(host='localhost', user='root', password="")
        mycursor = mydb.cursor()
        print("Connection established!")

        # Create database if it doesn't exist
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Heart_Data")
        mycursor.execute("USE Heart_Data")

        # Create table if it doesn't exist
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(50),
                Date VARCHAR(100),
                DOB VARCHAR(100),
                age VARCHAR(100),
                sex VARCHAR(100),
                Cp VARCHAR(100),
                trestbps VARCHAR(100),
                chol VARCHAR(100),
                fbs VARCHAR(100),
                restecg VARCHAR(100),
                thalach VARCHAR(100),
                exang VARCHAR(100),
                oldpeak VARCHAR(100),
                slope VARCHAR(100),
                ca VARCHAR(100),
                thal VARCHAR(100),
                Result VARCHAR(100)
            )
        """)

        # Insert data into the table
        command = """
            INSERT INTO data (Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, Result)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        mycursor.execute(command, (name, date, dob, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result))
        mydb.commit()

        messagebox.showinfo("Register", "New User Added successfully !!!")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

    finally:
        # Closing database connection
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("Database connection is closed.")

# Example usage
# save_data_mysql('mrunknown', "08/08/2023", "1979", "44", "1", "1", "233", "233", "1", "1", "233", "1", "233.0", "0", "2", "1", "0")
