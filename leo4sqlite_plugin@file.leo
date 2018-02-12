<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="tsc.20180211141409.1"><vh>@settings</vh>
<v t="tsc.20180211195528.1"><vh>@data free-layout-layout</vh></v>
<v t="tsc.20180211224859.1"><vh>@button extract-blob</vh></v>
<v t="tsc.20180211224910.1"><vh>@button insert-blob</vh></v>
<v t="tsc.20180211224851.1"><vh>@button view-blob</vh></v>
<v t="tsc.20180211224516.1"><vh>@button open-blob</vh></v>
<v t="tsc.20180211141409.2"><vh>@data external tools</vh></v>
<v t="tsc.20180211141409.3"><vh>@string sqlite_output_dir = "/home/tsc/Desktop/leo4sqlite-output"</vh></v>
<v t="tsc.20180211141409.4"><vh>@string sqlite_temp_dir = "/home/tsc/Desktop/leo4sqlite-temp"</vh></v>
<v t="tsc.20180211141409.5"><vh>/home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py</vh></v>
<v t="tsc.20180211141409.6"><vh>/home/tsc/Desktop/leo4sqlite/leo4sqlite.py</vh></v>
<v t="tsc.20180211141409.7"><vh>/home/tsc/Desktop/leo4sqlite-file/leo4sqlite@file.py</vh></v>
</v>
<v t="tscv11.20180119175627.1"><vh>Sqlite3</vh>
<v t="tsc.20180206152253.2"><vh>@file /home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py</vh></v>
</v>
<v t="tsc.20180211141409.8"><vh>temp</vh></v>
<v t="tsc.20180211141409.9" a="E"><vh>data</vh>
<v t="tsc.20180211222256.1" a="E"><vh>@db3 /home/tsc/Desktop/blob_test.db3</vh>
<v t="tsc.20180211222256.2" a="E"><vh>@tbl testorama</vh>
<v t="tsc.20180211222256.6"><vh>dumb.jpg</vh></v>
<v t="tsc.20180211222256.11"><vh>Screenshot (2).png</vh></v>
<v t="tsc.20180211222256.15"><vh>Feather-flying.jpg</vh></v>
<v t="tsc.20180211222256.7"><vh>Screenshot (3).png</vh></v>
<v t="tsc.20180211222256.10"><vh>Spider.ico</vh></v>
<v t="tsc.20180211222256.8"><vh>Screenshot (4).png</vh></v>
</v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="tsc.20180211141409.1"></t>
<t tx="tsc.20180211141409.2"># one executable per line

xviewer
gimp-2.8
</t>
<t tx="tsc.20180211141409.3"></t>
<t tx="tsc.20180211141409.4"></t>
<t tx="tsc.20180211141409.5"></t>
<t tx="tsc.20180211141409.6"></t>
<t tx="tsc.20180211141409.7"></t>
<t tx="tsc.20180211141409.8"></t>
<t tx="tsc.20180211141409.9"></t>
<t tx="tsc.20180211195528.1">{
    "content": [
        "_leo_pane:bodyFrame",
        {
            "content": [
                "_leo_pane:outlineFrame",
                "_leo_pane:logFrame"
            ],
            "sizes": [
                309,
                275
            ],
            "orientation": 2
        }
    ],
    "sizes": [
        807,
        547
    ],
    "orientation": 1
}</t>
<t tx="tsc.20180211222256.1"></t>
<t tx="tsc.20180211222256.10">/home/tsc/Desktop/blob_test.db3

Words: 'testykulls'
Amount: 1.0
Time: 2
</t>
<t tx="tsc.20180211222256.11">/home/tsc/Desktop/blob_test.db3

Words: 'baby'
Amount: 2.0
Time: 3
</t>
<t tx="tsc.20180211222256.15">/home/tsc/Desktop/blob_test.db3

Words: 'bloborific'
Amount: 15.0
Time: 9
</t>
<t tx="tsc.20180211222256.2">filepath: /home/tsc/Desktop/blob_test.db3

['Words', 'Amount', 'Time', 'Blobs', 'Filename', 'Extension']
['TEXT', 'REAL', 'INTEGER', 'BLOB', 'TEXT', 'TEXT']

</t>
<t tx="tsc.20180211222256.6">/home/tsc/Desktop/blob_test.db3

Words: '18'
Amount: 'ounce'
Time: 'half past'
</t>
<t tx="tsc.20180211222256.7">/home/tsc/Desktop/blob_test.db3

Words: '31'
Amount: 1.0
Time: 2
</t>
<t tx="tsc.20180211222256.8">/home/tsc/Desktop/blob_test.db3

Words: '32'
Amount: 1.0
Time: 2
</t>
<t tx="tsc.20180211224516.1">@language python

import re
import sqlite3
import subprocess
import PyQt5
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QInputDialog, QDesktopWidget
    
'''open the blob whose node is currently selected using an external tool'''        

table_node = p.parent()
c.selectPosition(table_node)
table_name = table_node.h
table_name = re.sub(r'^.*@tbl\s', '', str(table_name))

lines = re.split(r'\n', p.b)
filename = p.h
blobfile = lines[0]

blob_col = 3

sqlite_temp_dir = c.config.getString('sqlite_temp_dir')

if not sqlite_temp_dir:
    raise NoTempDirectory

sqlite_temp_dir = sqlite_temp_dir[1:-1]

p = g.findNodeAnywhere(c, '@data external tools')
tools = re.split(r'\n', p.b)
tools = tools[2:-1]
c.selectThreadBack()
c.redraw()

title = 'leo4sqlite - open blob - choose tool'
dlg = QInputDialog()
dlg.setWindowTitle(title)
qtRectangle = dlg.frameGeometry()
centerPoint = QDesktopWidget().availableGeometry().center()
qtRectangle.moveCenter(centerPoint)
dlg.move(qtRectangle.topLeft())

dlg.setStyleSheet('padding: 3px; background: white');
ext_tool, okPressed = dlg.getItem(dlg, "leo4sqlite","select external tool:", tools, 0, False)

conn = sqlite3.connect(blobfile)
cursor = conn.cursor()

cursor.execute("select * from %s where Filename = ?" % (table_name), [filename])
row = cursor.fetchone()

filepath = (sqlite_temp_dir + '//' + filename)
filename = filename[:-4]

with open(filepath, "wb") as output_file:        
    cursor.execute("select * from %s where Filename = ?" % (table_name), [filename])        
    ablob = cursor.fetchone()
    output_file.write(ablob[blob_col])
    cursor.close()

    p = subprocess.Popen([ext_tool, filepath])
</t>
<t tx="tsc.20180211224851.1"></t>
<t tx="tsc.20180211224859.1"></t>
<t tx="tsc.20180211224910.1"></t>
<t tx="tscv11.20180119175627.1">**leo4sqlite.py plugin**

*This node belongs at the top level of 'leoPlugins.leo'*

|
         
**Notes**

 | 1. This script needs to be streamlined and polished, which I intend to do (in the end I'm a perfectionist). Any suggestions toward that end are welcome!
 
**Issues**
 
 | 3. Data types - column affinity, manifest type, storage type

**Ideas**
    
 | 1. Recent files for blob command dialogs?
 |

**The commands currently added by the plugin are:**

 | sqlite-make-template"
 | sqlite-import-table
 | sqlite-export-table
 | sqlite-open-blob
 | sqlite-view-blob
 | sqlite-insert-blob
 | sqlite-extract-blob
 | sqlite-reset-temp
 | sqlite-clear-data
 | sqlite-purge-files
 |
 
I want to make this the best plugin I can rather than rushing to finish it. Leo deserves no less! Please provide any feedback you can, and don't hesitate to suggest improvements! :-)</t>
</tnodes>
</leo_file>
