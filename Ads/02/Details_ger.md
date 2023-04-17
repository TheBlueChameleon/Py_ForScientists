# Python Booster Pack
Dieser Kurs in vier Einheiten hat zum Ziel, fortgeschrittene Konzepte aus Python speziell für das wissenschaftliche Programmieren zu erklären. Die einzelnen Einheiten bestehen aus ca. 90-minütigen Vorlesungen. Optional können im Anschluss beliebige Programmier-Themen diskutiert werden, einschließlich Fragen der Teilnehmer:innen zu ihren jeweiligen Forschungsprojekten.#

Die vorbereiteten Präsentationen bilden abgeschlossene Einheiten. Das bedeutet, dass es möglich ist, an einzelnen Terminen nicht teilzunehmen und dennoch die Folge-Veranstaltung zu besuchen.


## Behandelte Themen

### Projekt-Design und Kapselung
Wissenschaftliche Simulationen modellieren komplexe Wechselwirkungen. Dieses Maß an Komplexität spiegelt sich notwendigerweise auch im Code wider. In dieser ersten Einheit wollen wir uns damit beschäftigen, wie Code dennoch mittels Klassen und Modulen in überschaubare und wartbare Einheiten gegliedert werden kann. Dies geschieht anhand eines Code-Beispiels, das N nicht-wechselwirkende Teilchen in einem frei wählbaren Potential simuliert.

### Einführung in die Metaprogramming
In Python ist es möglich, Code zur Laufzeit zu verändern. Während dies scheinbar ein neues Level an Komplexität einführt, kann so oft die Programmier-Arbeit bedeutend erleichtert werden. Wir lernen hier das Konzept der *Decorators* kennen und betrachten in diesem Kontext auch, wie Python Datenobjekte im Allgemeinen behandelt. Aus diesen Kenntnissen leiten wir Mittel ab, sowohl einfacher lesbaren als auch schneller laufenden Code zu schreiben.

### Iteratoren und das Lazy-Evaluation-Paradigma
Für eine for-Schleife in Python läuft einiger nicht-trivialer Code im Hintergrund. Wir werden hier sowohl erfahren, welche Mechanismen in Kraft treten als auch weshalb Python in dieser Art aufgebaut ist. Weiter lernen wir den Befehl *yiel* und das Konzept *Generator Expressions* kennen. Mit diesen Erkenntnissen wenden wir uns Problemen aus der echten Welt zu und optimieren unseren Geld-zu-Süßigkeiten-Wechselkurs.

### Paralleles Programmieren und Multiprocessing
Wo rohe Gewalt nicht hilft, braucht man mehr davon. Manche Probleme in der wissenschaftlichen Programmierung lassen sich nur durch rohe Rechenleistung lösen. Moderne Computer haben in der Regel mehrere CPUs, die unabhängig voneinander arbeiten können. In dieser Einheit werden wir lernen, wie das *multiprocessing-Modul* genutzt werden kann, um mehrere Teile eines Problems parallel zu lösen. Wir erarbeiten uns zuerst ein Grundvokabular, das so auch im Kontext anderer Sprachen zum Einsatz kommt, und beschäftigen uns dann mit Python-spezifischen Features.


## Voraussetzungen
Willkommen ist jeder mit Grundlagen-Kenntnissen in der Programmiersprache Python. Das schließt insbesondere Studierende, Doktoranden, Angestellte der UR sowie Gäste ein.

Die verwendeten Beispiele sind oft inspiriert von Problemen aus der Physik. Vertrautheit mit Linearer Algebra und Analysis sind daher wünschenswert. Der Fokus wird jedoch auf den Programmier-Aspekten liegen. Teilnehmer mit nicht-naturwissenschaftlichem Hintergrund sollten also den Vorträgen ebenfalls folgen können, auch wenn einzelne Themen einige Herausforderung darstellen werden.

Zu den offenen Diskussionen können Sie gerne Ihren eigenen Rechner/ihre eigenen Codes mitbringen. Ich empfehle, eine aktuelle Version von Python 3 sowie einen Code-Editor Ihrer Wahl zu installieren.

Ich werde meinen Hund zu den Vorträgen mitbringen. Bitte kontaktieren Sie mich, falls Sie allergisch oder durch die Anwesenheit von Hunden anderweitig eingeschränkt sind.

Die Sprache der Vorträge richtet sich danach, womit sich die größte Zahl an Teilnehmer:innen wohl fühlt. Schriftliche Kursmaterialien (z.B. Vortragsfolien oder Beispielcodes) werden in Englisch zur Verfügung gestellt.
Ich selbst spreche Deutsch, Englisch und Französisch. Falls Sie während der Vorträge Fragen lieber in Ihrer Muttersprache stellen möchten, kann ich für Sie übersetzen.


## Outlook
Wenn genügend fortgesetztes Interesse besteht, kann die Vorlesungsreihe weitergeführt werden. Details hierzu werden im Kurs diskutiert; Ziel soll es sein, einen Kompromiss zwischen den Interessen aller Teilnehmer:innen zu finden. Themen, die ich anbieten kann sind unter anderem:

* Effizienz

    Wie erkennt und schreibt man *schnellen* Code?<br>
    Warum gilt Python als langsamer als C und wie umgeht man diese Barriere?

* Thematische Klammer Numerik

    In drei Einheiten werden wir Methoden kennenlernen, um Ableitungen, Integrale und Fourier-Transformationen zu berechnen sowie (partielle) Differentialgleichungen zu lösen und uns mit Rauschunterdrückung beschäftigen. Hierzu nutzen wir numpy und scipy.

* Mehr Metaprogramming

    *Type hints* und *annotations* sind Konzepte, die (normalerweise) keinen direkten Einfluss auf die Ausführung von Code haben, mit deren Hilfe externe Tools aber Fehler in unserer Arbeit finde können oder uns anderweitig das Leben erleichtern. Zusammen mit Decorators kann über diese Mittel automatisch Code generiert werden und so viel Arbeit erspart werden.

* Konstanten und Parameter

    Simulationen müssen oft wiederholt ausgeführt werden, wobei nur einzelne Parameter ausgetauscht werden (z.B. die Stärke eines Magnetfeldes).
    Wir werden hier Möglichkeiten diskutieren, Programme so aufzusetzen dass einzelne Werte schnell und konsistent ersetzt werden können ohne dabei den Code selbst bearbeiten zu müssen.
    In diesem Kontext wenden wir uns auch wieder der Projekt-Struktur zu.

* Was auch immer gewünscht wird

    Mein Ziel ist, den Teilnehmer:innen bei ihren konkreten Problemen zur Seite zu stehen, wo diese auch liegen mögen.
    Ich freue mich daher über Rückmeldungen jedweder Art, und kann auf Anfrage Vorlesungen zu Wunsch-Themen zusammenstellen.
