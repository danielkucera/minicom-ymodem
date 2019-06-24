# minicom-ymodem

Pure YMODEM for minicom

## Setup
```
cd /opt
git clone <this_repo>
pip install https://github.com/danielkucera/xmodem/archive/master.zip
```
- open minicom
- press Ctrl+a, o
- navigate to "File transfer protocols"
- add new protocol to J line:
```
+------------------------------------------------------------------------------+                                                          
|     Name             Program                 Name U/D FullScr IO-Red. Multi  |                                                          
| A  zmodem     /usr/bin/sz -vv -b              Y    U    N       Y       Y    |                                                          
| B  ymodem     /usr/bin/sb -vv                 Y    U    N       Y       Y    |                                                          
| C  xmodem     /usr/bin/sx -vv                 Y    U    N       Y       N    |                                                          
| D  zmodem     /usr/bin/rz -vv -b -E           N    D    N       Y       Y    |                                                          
| E  ymodem     /usr/bin/rb -vv                 N    D    N       Y       Y    |                                                          
| F  xmodem     /usr/bin/rx -vv                 Y    D    N       Y       N    |                                                          
| G  kermit     /usr/bin/kermit -i -l %l -b %b  Y    U    Y       N       N    |                                                          
| H  kermit     /usr/bin/kermit -i -l %l -b %b  N    D    Y       N       N    |                                                          
| I  ascii      /usr/bin/ascii-xfr -dsv         Y    U    N       Y       N    |                                                          
| J  Ymodem     /opt/minicom-ymodem/ymodem.py   Y    U    N       Y            |                                                          
| K    -                                                                       |                                                          
| L    -                                                                       |                                                          
| M  Zmodem download string activates... D                                     |                                                          
| N  Use filename selection window...... Yes                                   |                                                          
| O  Prompt for download directory...... No                                    |                                                          
|                                                                              |                                                          
|   Change which setting? (SPACE to delete)                                    |                                                          
+------------------------------------------------------------------------------+          
```
