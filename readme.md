# Comment créer l'exécutable keylogger à partir du script python ?

-- Se rendre d'abord dans le dossier cloné avec l'explorateur de fichiers et remplacer, dans la barre du chemin vers le dossier courant, par ```powershell```.

-- Dans la ligne de commande du powershell, taper ```python -m PyInstaller -w -F keyripper.py --icon=icon.ico```.

-- Attention ! Si PyInstaller n'est pas installé, la commande ci-dessus ne fonctionnera pas. Donc, pour l'installer, taper dans une console cmd : ```pip install pyinstaller```

-- Une fois que tout est crée, c'est parfait ! Vous n'avez plus qu'à faire une copie de l'exécutable dans le dossier "dist" et à le coller n'importe ou dans votre ordinateur. Il suffit ensuite de l'exécuter une fois et de commencer à taper des caractères dans une page google. Après 100 caractères, des touches clavier sont envoyés au mail de l'attaquant (votre propre mail), et ceci tous les 100 caractères tapés.

## Ce que je vous conseille de faire (avec le CONSENTEMENT des victimes !!!)

-- Il y a néanmoins un problème avec cet exécutable, une fois que la victime éteint son ordinateur et le rallume, le processus est tué, et on ne reçoit plus de touches via gmail. Ce que vous pouvez faire pour qu'à chaque démarrage l'exécutable s'exécute dans le pc de votre victime : 

- taper Windows + R
- Ecrire shell:startup
- Copier-Coller l'exécutable dans ce dossier

-- De cette manière, à chaque redémarrage, l'exécutable s'ouvre automatiquement sans que la victime s'en rende compte, et vous continuerez normalement à recevoir des mails en permanence, youpi ! 

-- DISCLAIMER : Ce projet a pour but l'éducation, et non pas la promotion de logiciels/techniques malveillantes. Merci d'utiliser ce script avec caution et de ne l'utiliser qu'avec des personnes qui ont le CONSENTEMENT !