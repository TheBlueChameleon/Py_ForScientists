# Konzept: Python für Naturwissenschaftler:innen
## Übersicht
Diese Vortragsserie richtet sich an Naturwissenschaftler:innen mit Grundlagen-Kenntnissen in der Programmiersprache Python, die mehr über die Werkzeuge und Techniken lernen möchten um so bessere Codes für ihre Forschungsprojekte zu schreiben.

Die Vorträge dauern ca. 60 bis 90 Minuten und stellen nützliche Pakete, Tools und Programmiertechniken in Python vor. _Optional_ können wir im Anschluss zu jeder Einheit informelle Gespräche über die aktuellen Forschungsfragen und Herausforderungen beim Programmieren unterhalten. Ausgehend von diesen Gesprächen werde ich die Auswahl, Reihenfolge und Tiefe der präsentierten Themen anpassen. Das bedeutet, es gibt einen vorbereiteten Satz von Themen, die präsentiert und diskutiert werden können. Der gesamte Umfang der Vortragsreihe kann jedoch frei nach den Bedrüfnissen und Wünschen der Teilnehmer:innen angepasst werden. Siehe weiter unten für eine Auswahl an Themen, die wir besprechen können.

Es wird zu dieser Vortragsreihe weder eine Übung noch eine Abschlussprüfung geben.

Die einzelnen Vorträge werden häufig als eigenständige Einheiten organisiert sein. Das bedeutet, dass die meisten Präsentationen nicht aufeinander aufbauen. Auch Teilnehmer:innen, die nicht an jedem Abend anwesend sein können, werden von der Reihe profitieren können. Bei entsprechendem Interesse können einzelne Themen aber auch vertieft behandelt werden und daher eine gewisse Vertrautheit mit diesen Themen voraussetzen. Im Zweifel können Sie mich gerne vor jedem Vortrag kontaktieren und die behandelten Themen und nötigen Vorkenntnisse erfragen.


## Voraussetzungen
Willkommen ist jeder mit Grundlagen-Kenntnissen in der Programmiersprache Python. Das schließt insbesondere Studierende, Doktoranden, Angestellte der UR sowie Gäste ein.

Die verwendeten Beispiele sind oft inspiriert von Problemen aus der Physik. Vertrautheit mit Linearer Algebra und Analysis sind daher wünschenswert. Der Fokus wird jedoch auf den Programmier-Aspekten liegen. Teilnehmer mit nicht-naturwissenschaftlichem Hintergrund sollten also den Vorträgen ebenfalls folgen können, auch wenn einzelne Themen einige Herausforderung darstellen werden.

Zu den offenen Diskussionen können Sie gerne Ihren eigenen Rechner/ihre eigenen Codes mitbringen. Ich empfehle, eine aktuelle Version von Python 3 sowie einen Code-Editor Ihrer Wahl zu installieren.

Ich werde meinen Hund zu den Vorträgen mitbringen. Bitte kontaktieren Sie mich, falls Sie allergisch oder durch die Anwesenheit von Hunden anderweitig eingeschränkt sind.

Die Sprache der Vorträge richtet sich danach, womit sich die größte Zahl an Teilnehmer:innen wohl fühlt. Schriftliche Kursmaterialien (z.B. Vortragsfolien oder Beispielcodes) werden in Englisch zur Verfügung gestellt.
Ich selbst spreche Deutsch, Englisch und Französisch. Falls Sie während der Vorträge Fragen lieber in Ihrer Muttersprache stellen möchten, kann ich für Sie übersetzen.


## Themen, die wir behandeln *können*
Unten finden Sie eine (erweiterbare) Liste von Themen, die ich vorstellen kann. Nicht alle von diesen Punkten können einen Abend ausfüllen; über andere könnte eine ganze Vortragsreihe ausgearbeitet werden.
Diese Liste ist also als Inspiration und Grundlage für Diskussionen gedacht. Falls keine Eingaben und Rückmeldungen von Teilnehmenden an mich kommt, werde ich nach eigenem Ermessen Themen aus dieser Auswahl vorstellen.

* Auffrischen der Grundlagen von Python
    + Native Datentypen
    + Klassen und Vererbung
    + Magic Methods
    + Module und Strukturierung von Code
    + Konventionen und Style-Richtlinien
    + Exception Handling

* Fortgeschrittene Python-Konzepte
    + Generators und Lazy Evaluation
    + Iteratoren
    + Decorators
    + Metaklassen
    + Introspection und Meta-Programmierung
    + Type annotations

* Python Packages
    + Konfiguration ohne Code-Änderung -- Kommandozeilen-Parameter und Konfigurations-Dateien
        - argparse -- Kommandozeilen-Parameter
        - configparser -- Konfigurations-Dateien

    + Numerik-Pakete
        - numpy -- Schnelle Operationen auf (mehrdimensionalen) Arrays
        - pandas -- Analyse auf großen Datenreihen in tabellarischem Format (basierend auf numpy)
        - scipy -- Implementierung von häufig gebrauchten mathematischen Konzepten wie Fourier-Transformation, Integration, finden von Extremwerten und Nullstellen, ...
        - tensorflow and keras -- machine learning

    + Datenaustausch und Dateiformate
        - pickle -- Python-eigenes Dateiformat zum schnellen Speichern und Laden beliebiger Strukturen in anderen Python-Projekten
        - json -- Ein menschenlesbares Dateiformat zum Austausch mit anderen Programmen (auch nicht-Python-Projekte)
        - toml -- Ein menschenlesbares Dateiformat zum Austausch mit anderen Programmen (auch nicht-Python-Projekte)
        - csv -- Ein menschenlesbares Dateiformat für tabellarische Daten, das auch in Tabellenkalkuationsprogrammen wie MS Excel oder Libre Office Calc geladen werden kann
        - xml -- En (mehr oder minder) menschenlesbares Dateiformat zum Austausch komplexer, textbasierender und hierarchisch geordneter Information

    + Multitasking
        - multiprocessing -- paralleles Rechnen auf mehreren Prozessoren
        - threading -- "Multitasking in einem einzigen Prozessor"
        - asyncio -- Single-Thread Multitasking

    + Interaktion mit dem Betriebssystem
        - subprocess -- Andere Programme von Python aus starten sowie deren Ein- und Ausgaben verwalten
        - os -- Betriebssystem- und Dateisystem-Funktionen
        - glob -- Rekursives Durchwandern des Dateisystem und Pattern Matching auf Dateinamen

    + Internet und Netzwerke
        - urllib -- Informationen aus dem Internet in den Arbeitsspeicher laden
        - ftplib -- Kommunikation mit einem FTP-Server
        - imaplib -- Emails senden und empfangen ("das moderne Protokoll")
        - poplib -- Emails senden und empfangen ("das ältere Protokoll")

    + Zeit
        - time -- Messen von allgemeinen Zeiten, Umgang mit Zeitdifferenzen
        - timeit -- Laufzeit Messen

    + Visualisierung
        - matplotlib -- Die Standard-Methode zum Erstellen von Plots
        - seaborn -- Basierend auf der matplotlib und pandas; erlaubt aufwändige Plots schneller zu erstellen
        - pillow -- Bildmanipulation

    + Verschiedenes
        - tkinter -- Graphische User-Interfaces
        - itertools -- Hilfsfunktionen zum Umgang mit Listen und anderen Iterables
        - functools -- Hilfsfunktionen zur Transformation von Funktionen
        - unittest -- Automatisiertes Testen von Code auf Korrektheit
        - sys -- Python "unter der Motorhaube"
        - re -- RegExes: Pattern Matching auf Strings
        - collections -- Weitere Datencontainer
        - pprint (pretty print) --  Formatierte Textausgabe mit minimalem Aufwand
        - graphlib -- Arbeit mit Graphen (Struktur im Mathematischen Sinne, Knoten und Verbindungen)

* Allgemeine Konzepte aus der Informatik
    + Text-Darstellung im Speicher/Encoding, Unicode und UTF
    + Dateisysteme
    + Landau-Notation/Big O Notation
    + git, github und gitlab -- Versionskontrolle, Zusammenarbeit und Backups
    + IDEs -- PyCharm (und IntelliJ), QtCreator für Python, Eclipse, Spyder
    + Generieren automatischer Dokumentationen


## Beispiel-Themenauswahl
Die folgende Auswahl aus den oben genannten Themen basiert auf meiner persönlichen Wahrnehmung (Dinge, die ich oft verwende oder gerne früher gekannt hätte):

* Projektstruktur
    - Am Beispiel: mehrere nicht-interagierende Partikel in einer Potentiallandschaft
    - Abbildung einer physikalischen Welt in Datenstrukturen
    - Kapselung in Klassen und Modulen

* Schneller Code
    - Komplexitätsanalyse, Landau-Notation
    - Profiling
    - numpy

* Empfehlung für die weiteren Einheiten
    - SciPy: Integration, Fourier-Analyse, Kurven anfitten, gewöhnliche und partielle Differentialgleichungen
    - Python-Konzepte: Iteratoren, Decorators, Magic Methods, Type Annotations
    - IT-Konzepte: Unittests, Git repositories, Generieren automatischer Dokumentationen
    - pandas: Queries auf Data-Frames
    - Parallelisierung: Multitasking auf mehreren Prozessoren
    - argparse und configparser: Simulationsparameter von der Kommandozeile und aus Konfigurationsdateien lesen
