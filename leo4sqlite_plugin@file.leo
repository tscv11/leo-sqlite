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
<v t="tsc.20180211141409.1" a="E"><vh>@settings</vh>
<v t="tsc.20180212181615.1"><vh>@data free-layout-layout</vh></v>
<v t="tsc.20180212181416.1"><vh>@bookmarks</vh>
<v t="tsc.20180212181709.1"><vh>export-blobs</vh></v>
<v t="tsc.20180212181502.1"><vh>leo4sqlite.py</vh></v>
</v>
<v t="tsc.20180211224851.1"><vh>@button view-blob</vh></v>
<v t="tsc.20180211224859.1"><vh>@button extract-blob</vh></v>
<v t="tsc.20180211224516.1"><vh>@button open-blob</vh></v>
<v t="tsc.20180212171515.1"><vh>@button export-blobs</vh>
<v t="tsc.20180212171515.2"><vh>@@button export-blobs</vh></v>
</v>
<v t="tsc.20180212174950.1"><vh>@button import-blobs</vh></v>
<v t="tsc.20180211141409.2"><vh>@data external tools</vh></v>
<v t="tsc.20180211141409.3"><vh>@string sqlite_output_dir = "/home/tsc/Desktop/leo4sqlite-output"</vh></v>
<v t="tsc.20180211141409.4"><vh>@string sqlite_temp_dir = "/home/tsc/Desktop/leo4sqlite-temp"</vh></v>
<v t="tsc.20180211141409.5"><vh>@@file /home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py</vh></v>
<v t="tsc.20180211141409.6"><vh>@@file /home/tsc/Desktop/leo4sqlite/leo4sqlite.py</vh></v>
<v t="tsc.20180211141409.7"><vh>@@file /home/tsc/Desktop/leo4sqlite-file/leo4sqlite@file.py</vh></v>
</v>
<v t="tscv11.20180119175627.1" a="E"><vh>Sqlite3</vh>
<v t="tsc.20180206152253.2" a="E"><vh>@file /home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py</vh></v>
</v>
<v t="tsc.20180211141409.8"><vh>temp</vh></v>
<v t="tsc.20180211141409.9"><vh>data</vh>
<v t="tsc.20180212183140.1" a="E"><vh>@db3 /home/tsc/Desktop/blob_test.db3</vh>
<v t="tsc.20180212183140.2"><vh>@tbl testorama</vh></v>
<v t="tsc.20180212183140.3"><vh>dumb.jpg</vh></v>
<v t="tsc.20180212183140.4"><vh>Screenshot (3).png</vh></v>
<v t="tsc.20180212183140.5"><vh>Screenshot (4).png</vh></v>
<v t="tsc.20180212183140.6"><vh>Spider.ico</vh></v>
<v t="tsc.20180212183140.7"><vh>Screenshot (2).png</vh></v>
<v t="tsc.20180212183140.8"><vh>ly39gCL._.jpg</vh></v>
<v t="tsc.20180212183140.9"><vh>Feather-flying.jpg</vh></v>
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
<t tx="tsc.20180211224516.1">@language python

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
<t tx="tsc.20180211224851.1">@language python

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
<t tx="tsc.20180211224859.1"></t>
<t tx="tsc.20180212171515.1">@language python

'''export table with any text field changes included.'''

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

# for child in parent.children():
    # child_h.append(child.h)
    # child_b = re.split(r'\n', str(child.b))

#conn = sqlite3.connect(blobfile)
#cur = conn.cursor()

keys = []
vals = []

new_row = ''

#child_b = child_b[2:]

for child in parent.children():
    g.es(child.h)

    g.es("\n" + table_name + "\n")
    
    child_b = re.split(r'\n', child.b)
    for line in child_b:
        line = re.sub(r'^.*match=', '', line)
        key_val = re.split(r':\s', line)
        
        i = 0
        for field in key_val:
            if i == 0 and field != "":
                #g.es("key: " + str(field))
                keys.append(field)
            else:
                if i == 1 and field != "":
                    #g.es("val: " + str(field))
                    vals.append(field)
            i += 1
    
@ 
    i = 0
    for col_name in keys:
        col_names.append(col_name)
        col_values.append(vals[i])
        g.es(col_names[i])
        g.es(col_values[i])
        i += 1
    
conn = sqlite3.connect(blobfile)
cursor = conn.cursor()

for col_name in col_names:
    name = col_names[i]
    value = col_values[i]
    cur.execute("UPDATE %s SET %s = %s" % (table_name, name, value)
    
cur.execute("DROP TABLE " + table_name)
    print("\ndropping old table")
    cur.execute("CREATE TABLE " + table_name + " " + sql)
    print("creating new table")</t>
<t tx="tsc.20180212171515.2">@
@@language python

'''export table with any text field changes included.'''

import re
import sqlite3

child_h = []
child_b = []

p = c.p
parent = p.parent()
c.selectPosition(parent)
table_name = c.p.h[5:]

for child in parent.children():
    child_h.append(child.h)
    child_b = re.split(r'\n', str(child.b))
    blobfile = child_b[0]
    #for line in child_b:
        #key_val = re.sub(r'^&lt;.*:\s', '', line)

conn = sqlite3.connect(blobfile)
cur = conn.cursor()

col_cnt = 0        
row_cnt = 0
new_row = ''

for row in cur.execute("select * from %s" % (table_name)):
    g.es(table_name)
    for line in child_b:
        line = re.sub(r'^.*match=', '', line)
        #key_val = re.sub(r'.*:\'&gt;\s', '', line)
        key_val = re.split(r':\s', line)
        #key = re.sub(r'.*:', '', line)
        #val = re.sub(r'^.*:\s', '', key_val) 
        #g.es(key_val[0])
        #g.es(key_val[1])
        for key in key_val:
            g.es(key)
        #new_row = new_row + str(line_key + line_val) + "\n"
        col_cnt += 1
    row_cnt += 1

#g.es(new_row)
     
</t>
<t tx="tsc.20180212174950.1">@language python

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

filepath = blobfile # c._leo4sqlite['db_filename']

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
[]
[]
</t>
<t tx="tsc.20180212181416.1"></t>
<t tx="tsc.20180212181502.1" __bookmarks="7d7100580700000069735f6475706571014930300a732e">#Sqlite3:1--&gt;@file /home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py:0</t>
<t tx="tsc.20180212181615.1">{
    "content": [
        "_leo_pane:bodyFrame",
        {
            "content": [
                "_leo_bookmarks_show:",
                "_leo_pane:outlineFrame",
                "_leo_pane:logFrame"
            ],
            "orientation": 2,
            "sizes": [
                23,
                239,
                276
            ]
        }
    ],
    "orientation": 1,
    "sizes": [
        807,
        547
    ]
}</t>
<t tx="tsc.20180212181709.1" __bookmarks="7d7100580700000069735f6475706571014930300a732e">#@settings:0--&gt;@button export-blobs:5</t>
<t tx="tsc.20180212183140.1"></t>
<t tx="tsc.20180212183140.2">['Words', 'Amount', 'Time', 'Blobs', 'Filename', 'Extension']
['TEXT', 'REAL', 'INTEGER', 'BLOB', 'TEXT', 'TEXT']

</t>
<t tx="tsc.20180212183140.3">Words: '18'
Amount: 'ounce'
Time: 'half past'
</t>
<t tx="tsc.20180212183140.4">Words: '31'
Amount: 1.0
Time: 2
</t>
<t tx="tsc.20180212183140.5">Words: '32'
Amount: 1.0
Time: 2
</t>
<t tx="tsc.20180212183140.6">Words: 'testykulls'
Amount: 1.0
Time: 2
</t>
<t tx="tsc.20180212183140.7">Words: 'baby'
Amount: 2.0
Time: 3
</t>
<t tx="tsc.20180212183140.8">Words: '72'
Amount: 4.0
Time: 5
</t>
<t tx="tsc.20180212183140.9">Words: 'bloborific'
Amount: 15.0
Time: 9
</t>
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
