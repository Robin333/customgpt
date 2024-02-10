from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get-vector')
def get_vector():
    sql_file_path = 'NICE_Guideline_28_backup.sql'  # The path to your SQL file
    try:
        with open(sql_file_path, 'r', encoding='utf-8') as file:
            sql_content = file.read()  # Reads the entire file content
            # Process the file content as needed, here we just count the lines
            vector = len(sql_content.splitlines())
            return jsonify({"vector": vector})
    except FileNotFoundError:
        return jsonify({"error": "SQL file not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
