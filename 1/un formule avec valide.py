from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

# 定义一个简单的 HTML 表单
html_form = """
<!doctype html>
<html>
    <body>
        <form method="post" action="/">
            用户名: <input type="text" name="username"><br>
            留言: <textarea name="comment"></textarea><br>
            <input type="submit" value="提交">
        </form>
        <p>{{ message }}</p>
    </body>
</html>
"""

# Fonctions de validation des entrées
def validate_input(input_str):

    # Seuls les caractères alpha et numériques sont autorisés
    if re.match("^[a-zA-Z0-9]*$", input_str):
        return True
    else:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        comment = request.form.get("comment", "")

        # Vérifier si le nom utilisateur correspond aux exigences
        if not validate_input(username):
            message = "Le nom d'utilisateur ne peut contenir que des caractères alphabétiques et numériques !"
        else:
            # Nettoyage du contenu malveillant dans les commentaires pour éviter les XSS
            comment = re.sub(r'[<>]', '', comment)
            message = f"username: {username}, comment: {comment}"

    return render_template_string(html_form, message=message)

if __name__ == "__main__":
    app.run(debug=True)


# Simulation de données malveillantes introduites par utilisateur
user_input = '<script>alert("XSS Attack!");</script>'

#code de sortie
safe_output = html.escape(user_input)

# sortie
print(f"sortie sécurisée: {safe_output}")




try:
    # erreur de simulation
    result = 10 / 0
except Exception as e:
    # Traitement sûr des erreurs
    print("Une erreur s'est produite, veuillez réessayer plus tard.")  # Éviter afficher les détails dune erreur spécifique


