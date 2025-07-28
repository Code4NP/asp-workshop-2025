from flask import Flask, jsonify
import json
import gzip 

app = Flask(__name__)


def load_bgc_json_data_into_memory():
    BGC0000001 = "data/mibig_data/BGC0000001.5.json.gz"
    BGC0000002 = "data/mibig_data/BGC0000002.5.json.gz"
    with gzip.open(BGC0000001, "rt") as f:
        bgc1 = json.load(f)
    with gzip.open(BGC0000002, "rt") as f:
        bgc2 = json.load(f)
    # Combine the data from both BGCs
    return {"BGC0000001": bgc1, "BGC0000002": bgc2}


COMBINED_DATA = load_bgc_json_data_into_memory()


@app.route("/bgc/quality/<bgc_id>", methods=["GET"])
def get_quality(bgc_id):
    """
    Function to get the quality of a BGC.
    """
    # to test with curl:
    # curl -X GET http://localhost:5000/bgc/quality/BGC0000001
    try:
        bgc_data = COMBINED_DATA[bgc_id]
        quality = bgc_data.get("quality", "Quality data not available")
        return jsonify({"bgc_id": bgc_id, "quality": quality}), 200
    except KeyError:
        return jsonify({"error": "BGC not found"}), 404


# @app.route # need to fix this line
def get_bgc_status():
    pass  # and replace this "pass" with code


# @app.route # need to fix this line
def get_bgc_biosynthetic_gene_names():
    pass  # and replace this "pass" with code


# @app.route # need to fix this line
def get_bgc_compound_name_structure_and_activities():
    pass  # and replace this "pass" with code





if __name__ == "__main__":
    app.run(debug=True)
