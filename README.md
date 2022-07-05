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

Τέλος, από τη γραμμή εντολών πηγαίνουμε στο φάκελο του project και εκτελούμε:

```
uvicorn projectapp:app --reload
```
Παράδειγμα:
![Cmd](https://user-images.githubusercontent.com/34692617/177334613-34574074-29a9-45ba-a405-9fc1bc467841.jpg)

Τέλος, η εφαρμογή τρέχει στο  http://127.0.0.1:8000.


# Ubuntu Installation 

# Run with Ubuntu Container
