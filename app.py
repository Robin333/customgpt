from flask import Flask, jsonify
app = Flask(__name__)

# Assuming the SQL file is in the same directory as your Flask app
SQL_FILE_PATH = 'NICE_Guideline_28_backup.sql'

@app.route('/get-vector')
def get_vector():
    try:
        with open(SQL_FILE_PATH, 'r', encoding='utf-8') as file:
            # Here you can process your SQL file as needed
            # For example, counting the number of insert statements might be a vector
            content = file.read()
            vector = content.count('INSERT INTO')
            return jsonify({"vector": vector})
    except FileNotFoundError:
        return jsonify({"error": "SQL file not found."}), 404
    except Exception as e:
        # Catch other exceptions, such as encoding errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
