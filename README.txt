**Este programa lee un select con el siguiente formato:
empieza sin lineas en blanco y entre hypers hay una linea en blanco

 2017  1 6 2248 45.5 L  19.943 -71.786  0.0  DOM  3 0.5 1.5LDOM 2.7CDOM 1.9WDOM1
 SPEC AVERAGE  MO 11.9 ST  7.4 OM  2.2 f0 13.3 R0.0988 AL 0.00 WI 20.0 MW  1.9 3
 SPEC SD       MO  0.1 ST  5.5 OM  1.0 f0 3.78 R0.0351 AL      WI      MW  0.1 3
 GAP=300        1.18      10.2     7.3999.9 -0.2799E+02  0.1390E+03 -0.7215E+04E
 SPEC SDDRBH Z MO 11.8 ST0.827 OM  0.8 f0 7.98 R0.1484 AL-0.00 WI 20.0 MW  1.8 3
 SPEC SDDRBH Z T224917 K 0.020 GD  109 VS 3.20 DE 2.60 Q0400.0 QA 0.70 Q1 1.00 3
 SPEC MCDRBH Z MO 12.1 ST 14.2 OM  2.0 f0 16.0 R0.0740 AL-0.00 WI 20.0 MW  2.0 3
 SPEC MCDRBH Z T224848 K 0.020 GD 14.7 VS 3.20 DE 2.60 Q0400.0 QA 0.70 Q1 1.00 3
 SPEC REDRBH Z MO 11.8 ST  7.2 OM  1.0 f0 16.0 R0.0740 AL-0.00 WI 20.0 MW  1.8 3
 SPEC REDRBH Z T2249 4 K 0.020 GD 74.3 VS 3.20 DE 2.60 Q0400.0 QA 0.70 Q1 1.00 3
 2017-01-06-2248-00S.MAN___095                                                 6
 ACTION:UP  18-03-02 17:06 OP:JMLC STATUS:               ID:20170106224845 L   I
 OLDACT:ARG 17-01-06 23:05 OP:jmlc STATUS:               ID:20170106224800     3
 STAT SP IPHASW D HRMM SECON CODA AMPLIT PERI AZIMU VELO AIN AR TRES W  DIS CAZ7
 MCDR BZ EPg      2248 47.35   31                         90   -0.5310 14.7 113 
 MCDR BN ESg      2248 49.82                              90    0.1910 14.7 113 
 MCDR BZ  IAML    2248 49.97       132.1 0.15                          14.7 113 
 REDR BZ EPg      2248 57.22   38                         91   -0.2810 74.3 173 
 REDR BN ESg      2249  6.30                              91   -0.0710 74.3 173 
 REDR BZ  IAML    2249  7.53        17.0 0.20                          74.3 173 
 SDDR BZ EPg      2249  5.55   34                         90    0.9010  119 154 
 SDDR BN ESg      2249 18.61                              90   -0.2110  119 154 
 SDDR BZ  IAML    2249 35.04        16.9 1.85                           119 154 
                                                                                
 2017  1 7 0857 52.1 L  18.994 -67.684 12.1  DOM  3 0.5 3.3LDOM 3.6CDOM 3.1WDOM1
 SPEC AVERAGE  MO 13.7 ST151.2 OM  5.2 f0 12.4 R0.1113 AL 0.00 WI 20.0 MW  3.1 3
 SPEC SD       MO  0.0 ST0.000 OM  3.0 f00.000 R0.0000 AL      WI      MW  0.0 3
 GAP=201        1.31      21.4     7.5999.9  0.1440E+03  0.1188E+05 -0.1650E+05E
 SPEC NADRBH Z MO 13.7 ST151.2 OM  2.2 f0 12.4 R0.1113 AL-0.00 WI 20.0 MW  3.1 3
 SPEC NADRBH Z T 85853 K 0.020 GD  194 VS 3.73 DE 2.83 Q0400.0 QA 0.70 Q1 1.00 3
 2017-01-07-0856-00S.MAN___095                                                 6
 OLDACT:ARG 17-01-07 21:39 OP:jmlc STATUS:               ID:20170107085600     3
 ACTION:UP  18-03-02 17:06 OP:JMLC STATUS:               ID:20170107085752 L   I
 OLDACT:UP  17-01-07 21:47 OP:JMLC STATUS:               ID:20170107085600     3
 OLDACT:UP  17-01-07 21:46 OP:JMLC STATUS:               ID:20170107085600     3
 STAT SP IPHASW D HRMM SECON CODA AMPLIT PERI AZIMU VELO AIN AR TRES W  DIS CAZ7
 SJG  BZ EPg    C  858 22.21   53                         90    0.7510  189 121 
 SJG  BN ESg       858 42.66                              90   -0.5210  189 121 
 NADR BZ EPg       858 27.18   96                         90   -0.7410  232 280 
 NADR BN ESg       858 54.62                              90    0.2110  232 280 
 NADR BZ  IAML     859  0.67       252.6 0.55                           232 280 
 ABDR BZ EPg       858 40.39   76                         90    0.3910  311 267 
 ABDR BN ESg       859 15.35                              90   -0.0910  311 267 
 ABDR BZ  IAML     859 21.35        72.4 0.60                           311 267 

 **Salida 
 la salida es un dummy con todas las magnitudes:

 fecha      hora     lat    lon      dep    edep  gap  rms  ml   mc   mw  comentario
2017-01-06 22:48:45 19.943 -71.786   0.0  999.9  300  0.5  1.5  2.7  1.9 17.9Km al ONO de San Fernando de Montecristi, Oceano Atlantico.