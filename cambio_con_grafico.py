import random
import matplotlib.pyplot as plt

premi = [0, 1, 5, 10, 20, 50, 75, 100, 200, 500, 5000, 10000, 15000, 20000, 30000, 50000, 75000, 100000, 200000, 300000]
num_volte = 200000 # Numero di volte che vuoi ripetere il gioco
conteggio_premi_migliori = 0 # Conteggio delle volte in cui cambiare il pacco ha portato a un premio più alto
conteggio_cambi = 0 # Conteggio delle volte in cui il giocatore ha cambiato il pacco
vittorie = []
percentuali_vittorie = []
medie = []

for numero_pacchi_rimanenti in range(17):
    conteggio_premi_migliori = 0
    vittorie = []
    for i in range(num_volte):
        indice_mio_pacco = random.randrange(len(premi))
        premio_mio_pacco = premi[indice_mio_pacco]
        lista_pacchi_rimanenti = list(range(len(premi)))
        lista_pacchi_rimanenti.remove(indice_mio_pacco)
        pacchi_rimanenti = lista_pacchi_rimanenti[-3:] # Prendi i 3 pacchi più a destra
        lista_pacchi_rimanenti = lista_pacchi_rimanenti[:-3] # Rimuovi i 3 pacchi scelti dalla lista dei pacchi rimanenti
        pacchi_rimanenti += random.sample(lista_pacchi_rimanenti, numero_pacchi_rimanenti) # Scegli altri x pacchi in modo casuale
        premi_rimanenti = [premi[i] for i in pacchi_rimanenti]
        premi_circolanti = premi_rimanenti + [premio_mio_pacco]
        premi_circolanti = sorted(premi_circolanti)
        indice_nuovo_pacco = random.randrange(len(premi_rimanenti))
        premio_nuovo_pacco = premi_rimanenti[indice_nuovo_pacco]
        conteggio_cambi += 1 # Incrementa il contatore dei cambi
        if premio_nuovo_pacco > premio_mio_pacco:
            conteggio_premi_migliori += 1
            vittorie.append(premio_nuovo_pacco)
        else:
            vittorie.append(premio_nuovo_pacco)

    percentuale_vittorie = (conteggio_premi_migliori / num_volte) * 100
    media = sum(vittorie) / len(vittorie)
    percentuali_vittorie.append(percentuale_vittorie)
    medie.append(media)

fig, ax1 = plt.subplots()
ax1.plot(range(4,21), percentuali_vittorie)
ax1.set_title('Percentuale di vittorie e media dei premi al variare del numero di pacchi rimanenti al momento del cambio')
ax1.set_xlabel('Numero di pacchi rimanenti')
ax1.set_ylabel('Percentuale di premi migliori quando si cambia')
ax1.axhline(y=50, color='r', linestyle='--')

for x,y in zip(range(4,21), percentuali_vittorie):
    ax1.annotate(f'{y:.2f}', (x,y), textcoords="offset points", xytext=(0,10), ha='center')

ax2 = ax1.twinx()
ax2.plot(range(4,21), medie, color='g')
ax2.set_ylabel('Media dei premi cambiando')

for x,y in zip(range(4,21), medie):
    ax2.annotate(f'{y:.2f}', (x,y), textcoords="offset points", xytext=(0,-15), ha='center')

fig.tight_layout()
plt.show()
