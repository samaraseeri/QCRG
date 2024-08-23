print("Your suggestion has been submitted successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error: Could not access suggestions file: {e}")
    
    if __name__ == "__main__":
        from flask import Flask, request  # Import Flask for form processing
        app = Flask(__name__)

        @app.route("/", methods=["GET", "POST"])
        def handle_suggestion():
            if request.method == "POST":
                suggestion = request.form.get("suggestion", "")
                if suggestion:
                    append_suggestion(suggestion)
                else:
                    print("No suggestion provided.")
                    return "Suggestion Box"  # Return a simple response (can be customized)
                app.run(debug=True)  # Run the Flask development server~
