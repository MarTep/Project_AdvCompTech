# Project_AdvCompTech
Project Name: Object Detection

Η εφαρμογή αυτή είναι ένα μικρό API service, που μας επιτρέπει να εισάγουμε εικόνα τοπικά ή από ζωντανές κάμερες κυκλοφορίας και να εντοπίζουμε αντικείμενα σε αυτές

# Windows Installation

Θα χρειαστεί να έχουμε εγκατεστημένη [Python3.6 και μετά](https://www.python.org/downloads/) στον υπολογιστή μας και να βρίσκεται στο path του συστήματος ([Μεταβλητές Περιβάλλοντος](https://datatofish.com/add-python-to-windows-path/).

Στη συνέχεια, ανοίγουμε τη γραμμή εντολών (cmd.exe), και εκτελούμε διαδοχικά  τις εντολές:
```
pip install "fastapi[all]"

pip install requests

pip install opencv-contrib-python
```
Αν υπάρξει πρόβλημα με την opencv δοκιμάστε:
```
pip install opencv-python
```
ή
```
pip install opencv-python-headless
```
# Ubuntu Installation 

# Run with Ubuntu Container
