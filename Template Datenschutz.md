| x. Titel: Datenbearbeitung                                                                                                     | Module                                                      |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| 1. Begriffe, Grundätze, Systeme                                                                                                | - m_Fachbegriffe<br>- m_Gesetzeskonkurrenzen<br>- m_Systeme |
| 2. Datenkatalog                                                                                                                | - m_Datenkatalog                                            |
| 3. Datenbearbeitungen, Profiling<br>-> 1. Abschnitt : Datenbearbeitung<br>-> 2. Abschnitt : Profiling                          | <br>- m_Bearbeitungen<br>- m_Profiling                      |
| 3. Zugriffsrechte                                                                                                              | - m_Zugriffsrechte                                          |
| 4. Datenbekanntgaben                                                                                                           | - m_Bekanntgaben                                            |
| 5. Einschränzungen von Betroffenenrechten                                                                                      | - m\_Einschränzung\_Betroffenenrechten                      |
| 6. Aufbewahrung, Archivierung, Vernichtung<br>-> 1. Abschnitt : Aufbewahrung<br>-> 2. Abschnitt : Archivierung und Vernichtung | <br>- m_Aufbewahrung<br>- m_Archivierung_und_Vernichtung    |

Beschrieb Grundelemente:
-> `Verantwortliche`
-> `Bearbeitende`
-> `System`
-> `Zweck`
-> `Datentyp`
1. `Datenklasse`
```
Personendaten
-> normale Personendaten
-> besonders schützenswerte Personendaten
Juristische Personendaten
-> normale Daten von juristische Personen
-> besonders schützenswerter Daten von juristischen Personen
```

2. `Datenkategorien`

```
-> besonders schützenswerte Personendaten
(nDSG 5 lit c):
§ Daten über religiöse, weltanschauliche, politische oder gewerkschaftliche Ansichten oder
Tätigkeiten,
§ Daten über die Gesundheit, die Intimsphäre oder die Zugehörigkeit zu einer Rasse oder
Ethnie,
§ genetische Daten,
§ biometrische Daten, die eine natürliche Person eindeutig identifizieren,
§ Daten über verwaltungs- und strafrechtliche Verfolgungen oder Sanktionen,
§ Daten über Massnahmen der sozialen Hilfe
-> besonders schützenswerten Daten juristischer Personen
(RVOG 57r):
§ Daten über verwaltungs- und strafrechtliche Verfolgungen und Sanktionen;
§ Daten über Berufs-, Geschäfts- und Fabrikationsgeheimnisse.
```

3. `Datenunterkategorien`

```
Datenklassen können Datenkategorien haben, welche sollten Datenunterkategorien haben.
```

-> `Datenart`

- Definition
Ein Element von Typ ‘Datenart’ ist eine textliche Umschreibung eines Bestandes von
Personendaten und Daten von juristischen Personen, die in einem bestimmten Kontext anfallen.
- Zentral definieren und Namen geben
Es ist effizient, mehrere Datenarten zentral zu definieren und jeder Datenart einen kurzen,
sprechenden Namen zu geben. Dies erlaubt, später in verschiedenen Kontexten (Bearbeitungen,
Bekanntgaben, Zugriffsrechte, etc) mit 1 Wort auf diese Datenart zu referenzieren, anstatt immer
wieder wortreich den Umfang der bearbeiteten Daten zu umschreiben.
- nicht datenschutzrechtlich definieren – sondern **prozessual**

-> `Bekanntgabenform`

`Kein Zusammenhang von Bekanntgabeform und Normstufe`

Personendaten : 
- § Meldepflicht
- § Spontane Bekanntgabe
- § Datenbekanntgabe auf Anfrage und nach Ermessen der angefragten Behörde
- § Abrufverfahren

~~

Meldepflicht (= Behörde muss melden. Kein Ermessen):
- § Die Behörde ist verpflichtet, im Einzelfall Personendaten bekanntzugeben. Sie hat keinen Ermessensspielraum. Deshalb muss die Norm erwähnen, dass die Bekanntgabe obligatorisch ist; beispielsweise mittels «teilt (wem) mit».
- § Zu erfüllen ist die Meldepflicht von Amtes wegen oder im Einzelfall auf schriftliche Anfrage. Deshalb muss die Norm erwähnen, ob die Behörde nur auf Anfrage hin oder von sich aus Daten bekanntgeben muss.
- § Der Datenschutzleitfaden des BJ empfiehlt diese Standard-Wendung: «die Behörde übermittelt von Amtes wegen ..»
Spontane Bekanntgabe (= von sich aus. Behörde kann, muss aber nicht bekanntgeben):
- § Behörde darf im Einzelfall spontan Personendaten bekanntgeben. Sie ist jedoch nicht dazu verpflichtet.
- § Um Verwechslung mit Meldepflicht zu vermeiden, muss die Regelung erwähnen, dass die Mitteilung fakultativ ist. Dies erfolgt mittels «kann», «ist ermächtigt» oder «hat das Recht».
- § Der Datenschutzleitfaden des BJ empfiehlt diese Standard-Wendung: «die Behörde kann […] spontan melden»
Datenbekanntgabe auf Anfrage und nach eigenem Ermessen der angefragten Behörde:
- § Behörde entscheidet auf Anfrage, ob sie – im Rahmen des Gesetzes und ihres Ermessensspielraums – dem Gesuch stattgibt. Die Bekanntgabe erfolgt im Einzelfall.
- § Um Verwechslung mit der spontanen Bekanntgabe zu vermeiden, muss die Regelung erwähnen, dass Daten nur auf schriftliche Anfrage bekannt gegeben werden können.
- § Um Verwechslung mit der Meldepflicht zu vermeiden, muss die Regelung erwähnen, dass die Datenbekanntgabe dem Ermessen unterliegt. Dies erfolgt durch Wendungen wie «kann / ist ermächtigt / hat das Recht, Personendaten bekannt zu geben».
- § Der Datenschutzleitfaden des BJ empfiehlt diese Standard-Wendung: «die Behörde kann in besonderen Fällen und auf schriftlichen und begründeten Antrag hin […]»
Abrufverfahren (= Selbstbedienung oder gemeinsamer Systembetrieb):
- § Definition
  Ein Abrufverfahren liegt vor, wenn mehrere Verwaltungsstellen dasselbe Informationssystem betreiben oder wenn Dritte nach dem Prinzip der Selbstbedienung Zugriff auf die Daten des Systems haben. Kennzeichnend ist, dass die Bekanntgabe erfolgt, ohne dass das für die Bearbeitung verantwortliche Bundesorgan die Daten bekanntgeben muss oder auch nur bemerkt, dass auf die Daten zugegriffen wurde (Selbstbedienungsprinzip).
- § Diese Art nur nutzen, wenn unbedingt nötig
  Ein Abrufverfahren soll nur errichtet werden, wenn es Dritten für deren Aufgabenerfüllung unabdingbar ist. Blosse Praktikabilitätsgründe genügen nicht. Diese Form des Datenaustauschs ist vor allem dann vorzusehen, wenn Dritte häufig auf die Personendaten zugreifen müssen. Die rechtlichen Grundlagen für den Betrieb eines Abrufverfahrens für ein System der Bearbeitung von Personendaten haben umso genauer zu sein, je schwerer der Eingriff in die Persönlichkeitsrechte ist. Die Schwere der Verletzung beurteilt sich nach der Art und der bearbeiteten Daten und dem Zweck der Datenbearbeitung.
- § Zugriffsart
  Das BJ wünscht zudem, dass die Zugriffsart weiter spezifiziert wird: Liegt ein «Vollzugriff» oder ein «Indexzugriff» vor. Das BJ bleibt aber die Erklärung schuldig, was damit gemeint ist; auch konnten keine Muster gefunden werden, welche diese Differenzierung machen. Unabhängig davon gilt das generelle Prinzip, dass ein Empfänger nur in dem Umfang Zugriff auf die Daten haben soll, die er zur Erfüllung seiner Aufgaben benötigt (und Empfängerseitig auch nur jene Personen Zugriff haben, die diese Daten für ihre Funktion benötigen – und nicht ein ganzes Amt pauschal).
- § Um Verwechslung mit anderen Bekanntgabeformen zu vermeiden, kann die Regelung erwähnen, dass Daten mittels «Abrufverfahren» oder «Online-Zugriff» bekannt gegeben werden.
- § Der Datenschutzleitfaden des BJ empfiehlt diese Standard-Wendung:
  «die Behörde kann einen Online-Zugriff gewähren [oder hat online Zugriff]»