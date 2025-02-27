from PyPDF2 import PdfMerger
import os

# Verzeichnis mit den PDFs
pdf_liste = ["datei1", "datei2", "usw"] # welche Dateien sollen zusammengefügt werden? bitte hier eintragen
ziel_datei = "namen_angeben.pdf" # Name der Zieldatei
quellordner = "C://hier/Quellordner/angeben"  # Quellordner, wo die PDFs liegen
zielordner = "C://hier/Quellordner/angeben" # Zielordner, wo die zusammengefügte Pdf abgelegt wird
zielpfad = os.path.join(zielordner, ziel_datei)  # erstellt einen vollständigen Dateipfad, indem sie den Ordnerpfad (zielordner) mit dem Dateinamen (ziel_datei) kombiniert.

# Funktion, um PDFs aus einer Liste zusammenzuführen
def pdfs_zusammenfuegen(pdf_liste, quellordner, zielpfad):
    # Erstelle ein PdfMerger-Objekt, das für das Zusammenführen der PDFs zuständig ist
    merger = PdfMerger()

    # für jede Datei, die in der Liste übergeben wurde:
    for pdf in pdf_liste:
        pdf_pfad = os.path.join(quellordner, pdf + ".pdf")  # Automatische Endung .pdf hinzufügen
        if os.path.exists(pdf_pfad):  # Prüfen, ob Datei existiert
            merger.append(pdf_pfad) # wenn ja, dann zum merger hinzufügen
        else:
            print(f"❌ Datei nicht gefunden: {pdf_pfad}") # Fehlermeldung, wenn Datei nicht gefunden

    merger.write(zielpfad) # Die zusammengefügte PDF im angegebenen Zielpfad speichern
    merger.close()



# Funktion ausführen (3 Parameter werden übergeben: 1)die Liste mit den PDFs, 2)der Quellordner, wo sie liegen 3) Zielpfad, wo die gemergte Datei gespeichert wird
pdfs_zusammenfuegen(pdf_liste, quellordner, zielpfad)