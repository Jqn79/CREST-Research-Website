from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2copy.html")

@app.route("/get_sensor_data", methods=["GET"])
def get_sensor_data():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CREST@TAMUK2023",
        database="new_schema7"
    )

    # Create a cursor to execute queries
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve data from the database
    cursor.execute("SELECT * FROM new_schema7.`sensor_data - copy`")

    # Fetch the data from the cursor
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return the data as a JSON response
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
