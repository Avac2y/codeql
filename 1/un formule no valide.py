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

# Exemple de code non sécurisé sans validation ni nettoyage des entrées
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        comment = request.form.get("comment", "")

        # Sortie directe non sécurisée de l'entrée de l'utilisateur
        message = f"username: {username}, comment: {comment}"

    return render_template_string(html_form, message=message)

if __name__ == "__main__":
    app.run(debug=True)

    import html



user_input = '<script>alert("XSS Attack!");</script>'

#Sortie directe des données de utilisateur
print(f"sortie non sécurisée: {user_input}")


try:
    # erreur de simulation
    result = 10 / 0
except Exception as e:
    # Édition de messages erreur détaillés
    print("Une erreur s'est produite:", e)
