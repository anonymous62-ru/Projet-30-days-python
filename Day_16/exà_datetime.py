from datetime import datetime, date

#  Obtenez le jour, mois, année, heure, minute et horodatage actuel
now = datetime.now()
print("Jour :", now.day)
print("Mois :", now.month)
print("Année :", now.year)
print("Heure :", now.hour)
print("Minute :", now.minute)
print("Horodatage (timestamp) :", now.timestamp())

#  Formatez la date actuelle avec le format "%m/%d/%y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%y, %H:%M:%S")
print("Date formatée :", formatted_date)

#  Convertissez "5 décembre 2019" en objet datetime
date_str = "05/12/2019"
converted_date = datetime.strptime(date_str, "%d/%m/%Y")
print("Objet datetime :", converted_date)

#  Calculez le temps restant jusqu’au Nouvel An
today = date.today()
new_year = date(today.year + 1, 1, 1)
delta_to_new_year = new_year - today
print("Jours jusqu'au Nouvel An :", delta_to_new_year.days)

#  Calculez le temps écoulé depuis le 1er janvier 1970
epoch = datetime(1970, 1, 1)
elapsed_since_epoch = now - epoch
print("Temps écoulé depuis le 1er janvier 1970 :", elapsed_since_epoch.days, "jours")

#  Cas d’usage du module datetime
print("\n Pourquoi utiliser datetime ?")
print("- Analyse de séries chronologiques (ventes, trafic, logs)")
print("- Horodatage des activités dans une application")
print("- Ajout automatique de dates aux articles de blog ou newsletters")
