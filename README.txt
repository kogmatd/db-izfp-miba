[Aufnahme]
 Anregung: SINC-Funktion mi 100kHz
 Sensoren: 1 Sender und 2 Empfänger
 Proben:   siehe Proben.xlsx

[Audiodateien]
 srate = ??, in wav: 22050Hz (Ist falsch!)
 chs   = 1
 enc   = float32 (tme,son), int16(wav), ADC: 12Bit
 len   = 16384 Samples (ch1+ch2)
        einzelne: 32768 oder 65536 Samples (ch3)

[Dateinamen]
 (tme|wav|son|son_long)/(MT[1-8]|OT)_DDDDDD_(tme|wav|son|son_long)/(MT[1-8]|OT)_NNN_ch[123].(tme|wav|son)

  tme:      Originaldateien
            (Möglichst diese Dateien verwenden)
            Import: with open(fn,'rb') as f: arr=np.frombuffer(f.read()[4:],'>f4')

  wav:      Wav-Dateien
            (Nicht für alle Aufnahmen vorhanden!)

  son:      Sonagramme 
            (Dimension  97x1024; Nicht für alle Aufnahmen vorhanden!)
            Import: with open(fn,'rb') as f: arr=np.frombuffer(f.read(),'>f4').reshape(-1,1024)

  son_long: Sonagramme 
            (Dimension 225x1024; Nicht für alle Aufnahmen vorhanden!)
            Import: with open(fn,'rb') as f: arr=np.frombuffer(f.read(),'>f4').reshape(-1,1024)

 MT1-8,OT: Session
 DDDDDD: Datum der Aufnahme

 NNN: Probennummer

 ch1,ch2: Empfängersensor 1 oder 2
 ch3:     Sendersensor (wird ignoriert)


[Beschreibung und Dokumentation]
 - common/doc auf S:
 - Diss Tschöpe, Kapitel 4.3 + Tabelle A.2+3 im Anhang

