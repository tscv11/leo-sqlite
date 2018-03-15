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
<v t="tsc.20180214164152.1"><vh>@settings</vh>
<v t="tsc.20180214164152.6" a="E"><vh>@buttons</vh>
<v t="tsc.20180216195827.1"><vh>@button export-blobs</vh></v>
<v t="tsc.20180214164152.10"><vh>@button import-blobs</vh>
<v t="tsc.20180214164152.11"><vh>@@button import-blobs</vh></v>
</v>
<v t="tsc.20180214164152.17"><vh>@button view-blob</vh></v>
<v t="tsc.20180214164152.15"><vh>@button open-blob</vh>
<v t="tsc.20180214164152.16"><vh>@@button open-blob</vh></v>
</v>
<v t="tsc.20180307110756.1"><vh>@button export-table</vh></v>
<v t="tsc.20180307110749.1"><vh>@button import-table</vh></v>
</v>
<v t="tsc.20180214164152.2"><vh>@bookmarks</vh>
<v t="tsc.20180219220649.1"><vh>export_blobs</vh></v>
<v t="tsc.20180214164152.3"><vh>import-blobs</vh></v>
<v t="tsc.20180214164152.5"><vh>leo4sqlite.py</vh></v>
</v>
<v t="tsc.20180214164152.18"><vh>@data external tools</vh></v>
<v t="tsc.20180214164152.19"><vh>@string sqlite_output_dir = "/home/tsc/Desktop/leo4sqlite-output</vh></v>
<v t="tsc.20180214164152.20"><vh>@string sqlite_temp_dir = /home/tsc/Desktop/leo4sqlite-temp</vh></v>
<v t="tsc.20180214164152.21"><vh>@@file /home/tsc/Desktop/leo4sqlite/leo4sqlite.py</vh></v>
<v t="tsc.20180214164152.22"><vh>@@file /home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py</vh></v>
<v t="tsc.20180214164152.23"><vh>@@file /home/tsc/Desktop/leo4sqlite-file/leo4sqlite.py</vh></v>
</v>
<v t="tsc.20180315095328.1"><vh>some nodes</vh>
<v t="tsc.20180315095328.2"><vh>node</vh></v>
<v t="tsc.20180315095328.3" a="E"><vh>n2</vh>
<v t="tsc.20180315095328.4"><vh>n3</vh></v>
<v t="tsc.20180315095328.5"><vh>n4</vh></v>
</v>
</v>
<v t="tscv11.20180119175627.1"><vh>Sqlite3</vh>
<v t="tsc.20180206152253.2" descendentVnodeUnknownAttributes="7d710058010000003071017d7102580b0000005f5f626f6f6b6d61726b7371037d7104580700000069735f6475706571054930300a7373732e"><vh>@file /home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py</vh></v>
</v>
<v t="tsc.20180214164224.1"><vh>sqlite-temp</vh></v>
<v t="tsc.20180314214021.1"><vh>sqlite-data</vh></v>
<v t="tsc.20180315084817.1"><vh>more nodes</vh>
<v t="tsc.20180315095254.1"><vh>node</vh></v>
<v t="tsc.20180315095256.1" a="E"><vh>n2</vh>
<v t="tsc.20180315095300.1"><vh>n3</vh></v>
<v t="tsc.20180315095303.1"><vh>n4</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="tsc.20180214164152.1"></t>
<t tx="tsc.20180214164152.10">@language python

c.executeMinibufferCommand('sqlite-import-blobs')
</t>
<t tx="tsc.20180214164152.11">@
@@language python

#import_blobs(self, c, p, col_nums, col_names, col_types, blob_col):
#table_name = c._leo4sqlite['table_name']

import re
import sqlite3

child_h = []
child_b = []
col_names = []
col_values = []

p = c.p
parent = p.parent()
c.selectPosition(parent)
table_name = c.p.h[5:]

for child in parent.children():
    child_h.append(child.h)
    child_b = re.split(r'\n', str(child.b))
    blobfile = child_b[0]

filepath = blobfile

num_cols = 0
for col in col_nums:
    num_cols = num_cols + 1

filename_col = num_cols - 2

g.es("\nimporting blob table: " + table_name + "\n")
                
delim = ", "
new_row = ""

#p.b = p.b + "filepath: " + str(filepath) + "\n\n"
p.b = p.b + str(col_names) + "\n"
p.b = p.b + str(col_types) + "\n\n"

conn = sqlite3.connect(filepath)
cursor = conn.cursor()

for row in cursor.execute("SELECT * FROM " + table_name):

    cx = 0 
    if row != "":
        cols = re.split(delim, str(row))

        #ix = 0
        for col in cols:
            if col != "" and col_types[cx] != "BLOB":
                if cx == 0: col = col[1:]
                new_row = new_row + col_names[cx] + ": " + col + "\n"
                cx = cx + 1
            new_row = re.sub(r'[\"]', " ", str(new_row))   
         
        if cx &lt; 3:                    
            p = p.insertAsLastChild()
            cx = 0
        else:
            p = p.insertAfter()
            
        c.selectPosition(p)
        p.h = row[filename_col] + row[extension_col]
        #p.b = p.b + str(filepath) + "\n\n"
        p.b = p.b + str(new_row[:-1]) + "\n"
        new_row = ""

g.es("done\n")
c.redraw()
headline = ("@tbl " + table_name)    
tbl_node = g.findNodeAnywhere(c, (headline))
c.selectPosition(tbl_node)
</t>
<t tx="tsc.20180214164152.15">@language python

c.executeMinibufferCommand('sqlite-open-blob')
</t>
<t tx="tsc.20180214164152.16">@
@@language python

'''open the blob whose node is currently selected using an external tool'''        

import re
import sqlite3
import subprocess
import PyQt5
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QInputDialog, QDesktopWidget
    
table_node = p.parent()
c.selectPosition(table_node)
table_name = table_node.h
table_name = re.sub(r'^.*@tbl\s', '', str(table_name))

filename = p.h
lines = re.split(r'\n', p.b)
blobfile = lines[0]
blob_col = 3

sqlite_temp_dir = c.config.getString('sqlite_temp_dir')
if not sqlite_temp_dir:
    raise NoTempDirectory


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

    p = subprocess.Popen([ext_tool, filepath])</t>
<t tx="tsc.20180214164152.17">@language python

''' view the selected blob as a temporary file that can be deleted automatically when Leo closes. This is controlled with a @settings tree node as follows: @bool delete_temp_files = 1: yes | 0: no '''

import re
import sqlite3
import subprocess
import PyQt5
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QInputDialog, QDesktopWidget
    
img_types = ['.png', '.jpg', '.bmp', '.gif']
vid_types = ['.mp4', '.avi', '.wmv', '.flv', '.mov', '.mkv']

#prev_nd = c.p.v
table_node = p.parent()
c.selectPosition(table_node)
table_name = table_node.h
table_name = re.sub(r'^.*@tbl\s', '', str(table_name))
g.es(table_name)
#c.selectPosition(prev_nd)

lines = re.split(r'\n', p.b)
filename = p.h
g.es(filename)
fn_len = len(p.h) - 4
extension = filename[fn_len:]
g.es(extension)
blobfile = lines[0]
g.es(blobfile)
blob_col = 3

temp_dir = c.config.getString("sqlite_temp_dir")
if not temp_dir:
    raise NoTempDirectory    
temp_dir = temp_dir[1:-1]

ext_tools = g.findNodeAnywhere(c, '@data external tools')
tools = re.split(r'\n', ext_tools.b)
tools = tools[2:-1]
    
conn = sqlite3.connect(blobfile)
cursor = conn.cursor()

fn_no_ext = filename[:-4]
g.es(fn_no_ext)

filepath = temp_dir + "/" + filename

ablob = []

with open(filepath, "wb") as output_file:               
    cursor.execute("select * from %s where Filename = ?" % (table_name), [fn_no_ext]) 
    ablob = cursor.fetchone()
    output_file.write(ablob[blob_col])
    cursor.close()
    
    if extension in img_types: 
        ph2b =  (r"@image " + filename)
        g.es(ph2b)
    if extension in vid_types:
        ph2b =  (r"@movie " + filename)
        g.es(ph2b)
        
    p = g.findNodeAnywhere(c, "temp")
    c.selectPosition(p)
    
    for child in p.children():
        if child.h == ph2b:
            c.selectPosition(child)
            c.executeMinibufferCommand('vr-show')
            raise NodeExists()
            break
    
    p = p.insertAsLastChild()
    c.selectPosition(p)
    p.h = ph2b
    p.b = filepath
    
    c.executeMinibufferCommand('vr-show')
    c.redraw()
    p = p.parent() 
    c.redraw()    
</t>
<t tx="tsc.20180214164152.18"># one executable per line

xviewer
gimp-2.8
</t>
<t tx="tsc.20180214164152.19"></t>
<t tx="tsc.20180214164152.2"></t>
<t tx="tsc.20180214164152.20"></t>
<t tx="tsc.20180214164152.21"></t>
<t tx="tsc.20180214164152.22"></t>
<t tx="tsc.20180214164152.23"></t>
<t tx="tsc.20180214164152.3" __bookmarks="7d7100580700000069735f6475706571014930300a732e">#@settings:0--&gt;@buttons:2--&gt;@button import-blobs:0</t>
<t tx="tsc.20180214164152.5" __bookmarks="7d7100580700000069735f6475706571014930300a732e">#Sqlite3:1--&gt;@file /home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py:0</t>
<t tx="tsc.20180214164152.6"></t>
<t tx="tsc.20180214164224.1"></t>
<t tx="tsc.20180216195827.1">@language python

c.executeMinibufferCommand('sqlite-export-blobs')
</t>
<t tx="tsc.20180219220649.1" __bookmarks="7d7100580700000069735f6475706571014930300a732e">#Sqlite3:1--&gt;@file /home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py:0--&gt;export_blobs:10</t>
<t tx="tsc.20180307110749.1">@language python

c.executeMinibufferCommand('sqlite-import-table')
</t>
<t tx="tsc.20180307110756.1">@language python

c.executeMinibufferCommand('sqlite-export-table')
</t>
<t tx="tsc.20180314214021.1"></t>
<t tx="tsc.20180315084817.1"></t>
<t tx="tsc.20180315095254.1"></t>
<t tx="tsc.20180315095256.1"></t>
<t tx="tsc.20180315095300.1"></t>
<t tx="tsc.20180315095303.1"></t>
<t tx="tsc.20180315095328.1"></t>
<t tx="tsc.20180315095328.2"></t>
<t tx="tsc.20180315095328.3"></t>
<t tx="tsc.20180315095328.4"></t>
<t tx="tsc.20180315095328.5"></t>
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
